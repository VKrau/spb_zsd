# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:21:54 2018

@author: VK
"""
import simplejson
import re
import sys
import csv
from datetime import datetime, timedelta
import time
from urllib.request import urlopen


class TravelCalculate:

    def __init__(self, api_key=""):
        self.__api_key = api_key

    def set_api_key(self, key):
        self.__api_key = key

    @staticmethod
    def __csv_reader(file_name):
        csv_file = file_name
        data = []
        with open(csv_file, "r") as r_obj:
            reader = csv.reader(r_obj, delimiter=";")
            for row in reader:
                data.append(row)
            return data

    @staticmethod
    def __csv_writer(first_run=False, data=None):
        if first_run:
            with open("output.csv", "w", newline="") as w_obj:
                writer = csv.writer(w_obj)
                writer.writerow(["date", "day_of_week", "time", "origin_coord",
                                 "destination_coord", "origin_name",
                                 "destination_name", "distance(m.)", "distance",
                                 "duration(s.)", "duration", "duration_in_traffic(s.)",
                                 "duration_in_traffic", "avoid"])
        else:
            with open("output.csv", "a", newline="") as w_obj:
                writer = csv.writer(w_obj)
                for i in data:
                    writer.writerow([time.strftime("%d.%m.%Y"), time.strftime("%A"),
                                     time.strftime("%H:%M"), i[0], i[1], i[2][0], i[2][1],
                                     i[2][2]["value"], i[2][2]["text"],
                                     i[2][3]["value"], i[2][3]["text"],
                                     i[2][4]["value"], i[2][4]["text"], i[3]])

    @staticmethod
    def __status_result(result):
        if result == "REQUEST_DENIED":
            print("Google Answer: REQUEST_DENUED")
            sys.exit()
        if result == "OVER_QUERY_LIMIT":
            print("Google Answer: OVER_QUERY_LIMIT")
            sys.exit()

    def calculate(self, orig, dest, avoid=[], traffic_model="best_guess"):
        api_key = self.__api_key
        if avoid:
            avoid = re.sub(r",", "|", avoid)
        url = "".join(str("https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s\
                  &destinations=%s\
                  &mode=driving\
                  &avoid=%s\
                  &language=en\
                  &traffic_model=%s\
                  &departure_time=now\
                  &key=%s" %
                          (orig, dest, avoid, traffic_model, api_key)).split())
        try:
            result = simplejson.load(urlopen(url))
        except IOError:
            print("Connection Error with Google Maps API!")
            sys.exit()
        self.__status_result(result)
        try:
            distance = result["rows"][0]["elements"][0]["distance"]
            duration = result["rows"][0]["elements"][0]["duration"]
            if api_key:
                duration_in_traffic = result["rows"][0]["elements"][0]["duration_in_traffic"]
            else:
                duration_in_traffic = {"text": "need api-key", "value": "need api-key"}
        except:
            print("Error! Please enter the correct coordinates or parameters!")
            sys.exit()
        print("-------------------------------")
        print("From: %s %s" % (result["origin_addresses"][0], orig))
        print("To: %s %s" % (result["destination_addresses"][0], dest))
        print("Distance: %s. (%s m.)" % (distance["text"], distance["value"]))
        print("Duration: %s. (%s sec.)" % (duration["text"], duration["value"]))
        if duration_in_traffic:
            print("Duration in traffic: %s. (%s sec.)" % (duration_in_traffic["text"],
                                                          duration_in_traffic["value"]))
        return result["origin_addresses"][0], result["destination_addresses"][
            0], distance, duration, duration_in_traffic

    def calculate_from_file(self, file_with_coord, avoid_options=[], query_time=[], duration=0):
        time_out = datetime.now()
        if duration > 0:
            time_out = time_out + timedelta(hours=duration)
        elif duration == 0 and query_time:
            if int(time.strftime("%H")) > max(query_time):
                time_out = time_out + timedelta(days=1)
            time_out = time_out.replace(hour=max(query_time), minute=1, second=0)
        self.__csv_writer(first_run=True)
        content = self.__csv_reader(file_with_coord)
        query_results = []
        while True:
            if duration >= 0 and query_time:
                if datetime.now() <= time_out:
                    content = self.__csv_reader(file_with_coord)
                    query_results.clear()
                    if int(time.strftime("%H")) in query_time and int(time.strftime("%M")) == 0:
                        for i in content[1:]:
                            for j in avoid_options:
                                query_results.append([i[0], i[1], self.calculate(orig=i[0], dest=i[1], avoid=j), j])
                        self.__csv_writer(data=query_results)
                        time.sleep(60)
                else:
                    break
            else:
                for i in content[1:]:
                    for j in avoid_options:
                        query_results.append([i[0], i[1], self.calculate(orig=i[0], dest=i[1], avoid=j), j])
                self.__csv_writer(data=query_results)
                break
            time.sleep(5)

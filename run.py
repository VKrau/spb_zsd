# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 09:13:53 2018

@author: VK
"""
from __future__ import absolute_import
from __future__ import print_function
import csv
import travel_calc
from datetime import datetime, timedelta
import time
query_time=[17,18,19]
duration = 48 #Hours
key = "YOUR API-KEY"

def csv_reader(file_name):
    csv_file = file_name
    data = []
    with open(csv_file, "r") as r_obj:    
        reader = csv.reader(r_obj, delimiter=";")
        for row in reader:
            data.append(row)
        return data

def csv_writer(first_run=False,data=None):
    #with open("output.csv", "wb") as w_obj: - for Python 2
    #This is for Python 3:
    if first_run:
        with open("output.csv", "w", newline="") as w_obj:
            writer = csv.writer(w_obj)
            writer.writerow(["date", "day_of_week", "time", "origin_coord",
                             "destination_coord", "origin_name",
                             "destination_name", "distance(m.)", "distance", 
                             "duration(s.)", "duration", "duration_in_traffic(s.)",
                             "duration_in_traffic", "avoid_tolls?"])
    else:
        #with open("output.csv", "ab") as w_obj: - for Python 2
        #This is for Python 3:
        with open("output.csv", "a", newline="") as w_obj:
            writer = csv.writer(w_obj)
            for i in data:
                writer.writerow([time.strftime("%d.%m.%Y"), time.strftime("%A"),
                                 time.strftime("%H:%M"), i[0], i[1], i[2][0], i[2][1],
                                 i[2][2]["value"], i[2][2]["text"],
                                 i[2][3]["value"], i[2][3]["text"],
                                 i[2][4]["value"], i[2][4]["text"], i[3]])
    
if __name__ == "__main__":
    time_out = datetime.now() + timedelta(hours=duration)
    csv_writer(first_run=True)
    while(True):
        if datetime.now()<time_out:
            content = csv_reader("coord.csv")
            query_results = []
            if int(time.strftime("%H")) in query_time and int(time.strftime("%M"))==0:
                for i in content[1:]:
                    query_results.append([i[0],i[1],travel_calc.calculate(orig=i[0], dest=i[1], api_key=key), "No"])
                    query_results.append([i[0],i[1],travel_calc.calculate(orig=i[0], dest=i[1], avoid="tolls", api_key=key), "Yes"])
                csv_writer(data=query_results)
                time.sleep(5)
        else:
            break
        
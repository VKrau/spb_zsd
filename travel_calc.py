# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:21:54 2018

@author: VK
"""
from __future__ import absolute_import
from __future__ import print_function
import simplejson
import re
import sys
import argparse
if sys.version[0]=="3":
    from urllib.request import urlopen
else:
    from urllib import urlopen

def status_result(result):
    if result=="REQUEST_DENIED":
        print("Google Answer: REQUEST_DENUED")
        sys.exit()
    if result=="OVER_QUERY_LIMIT":
        print("Google Answer: OVER_QUERY_LIMIT")
        sys.exit()
        
def calculate(orig, dest, avoid="", traffic_model="best_guess", api_key=""):
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
        if sys.version[0]<"3":
            result = simplejson.load(urlopen(url))
        else:
            result = simplejson.load(urlopen(url))
    except IOError:
        print("Connection Error with Google Maps API!")
        sys.exit()
    status_result(result)
    try:
        distance = result["rows"][0]["elements"][0]["distance"]
        duration = result["rows"][0]["elements"][0]["duration"]
        duration_in_traffic = ""
    except:
        print("Error! Please enter the correct coordinates or parameters!")
        sys.exit()
    if "duration_in_traffic" in result["rows"][0]["elements"][0]:
        duration_in_traffic = result["rows"][0]["elements"][0]["duration_in_traffic"]
    print("-------------------------------")
    print("From: %s %s" % (result["origin_addresses"][0], orig))
    print("To: %s %s" % (result["destination_addresses"][0], dest))
    print("Distance: %s. (%s m.)" % (distance["text"], distance["value"]))
    print("Duration: %s. (%s sec.)" % (duration["text"], duration["value"]))
    if duration_in_traffic:
        print("Duration in traffic: %s. (%s sec.)" % (duration_in_traffic["text"],
              duration_in_traffic["value"]))
    return result["origin_addresses"][0], result["destination_addresses"][0], distance, duration, duration_in_traffic

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--orig", required=True, help="The starting point for\
                        calculating travel distance and time")
    parser.add_argument("--dest", required=True, help="One or more locations to\
                        use as the finishing point for calculating travel\
                        distance and time")
    parser.add_argument("--avoid", default="", help="Introduces restrictions to\
                        the route. The following restrictions are supported:\
                        highways, tolls, ferries, indoor")
    parser.add_argument("--traffic_model", default="best_guess", help="Specifies the assumptions to use\
                        when calculating time in traffic. The traffic_model\
                        parameter may only be specified for requests where the\
                        travel mode is driving, and only if the request includes an\
                        API key or a Google Maps APIs Premium Plan client ID.\
                        The available values for this parameter are:\
                        best_guess(default), pessimistic, optimistic")
    parser.add_argument("--key", default="", help="Your application's API key. This key\
                       identifies your application for purposes of quota\
                       management")
    calculate(parser.parse_args().orig,
               parser.parse_args().dest,
               parser.parse_args().avoid,
               parser.parse_args().traffic_model,
               parser.parse_args().key)
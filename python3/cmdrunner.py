# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 09:13:53 2018

@author: VK
"""
from __future__ import absolute_import
from __future__ import print_function

import travel_calc
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--orig", required=False, help="The starting point for\
                        calculating travel distance and time")
    parser.add_argument("--dest", required=False, help="One or more locations to\
                        use as the finishing point for calculating travel\
                        distance and time")
    parser.add_argument("--file", help="Specify a file with coordinates")
    parser.add_argument("--avoid", action="store", default="", help="Introduces restrictions to\
                        the route. The following restrictions are supported:\
                        highways, tolls, ferries, indoor")
    parser.add_argument("--traffic_model", default="best_guess", help="Specifies the assumptions to use\
                        when calculating time in traffic. The traffic_model\
                        parameter may only be specified for requests where the\
                        travel mode is driving, and only if the request includes an\
                        API key or a Google Maps APIs Premium Plan client ID.\
                        The available values for this parameter are:\
                        best_guess(default), pessimistic, optimistic")
    parser.add_argument("--query_time", help="Time when the request will be executed")
    parser.add_argument("--duration", default=0, help="Duration of monitoring in hours.\
                        If the parameter is 0 (default), it will be executed once")
    parser.add_argument("--key", default="", help="Your application's API key. This key\
                        identifies your application for purposes of quota\
                        management")

    runner = travel_calc.TravelCalculate()
    if parser.parse_args().file == "":
        runner.calculate(parser.parse_args().orig,
                         parser.parse_args().dest,
                         parser.parse_args().avoid,
                         parser.parse_args().traffic_model,
                         parser.parse_args().key)
    else:
        list_query_time = list(map(lambda x: int(x), parser.parse_args().query_time.split(",")))
        runner.calculate_from_file(file_with_coord=parser.parse_args().file,
                                   avoid_options=parser.parse_args().avoid.split(","),
                                   query_time=list_query_time,
                                   duration=int(parser.parse_args().duration))

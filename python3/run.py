# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 09:13:53 2018

@author: VK
"""
import travel_calc

if __name__ == "__main__":
    runner = travel_calc.TravelCalculate()
    runner.set_api_key("") # <- YOUR API-KEY
    runner.calculate_from_file("coord.csv", ["", "tolls"], [17, 18, 19], duration=8)
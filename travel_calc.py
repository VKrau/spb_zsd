# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:21:54 2018

@author: VK
"""
from __future__ import absolute_import
from __future__ import print_function
import simplejson
import urllib
import re
import sys
import argparse

def start_calc(orig, dest, avoid=''):
    #orig_coord = 59.97241,30.2133597
    #dest_coord = 59.9177427,30.2103535
    orig_coord = orig
    dest_coord = dest
    if avoid:
        avoid = re.sub(r',', '|', avoid)
    url = ''.join(str("http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s\
              &destinations=%s\
              &mode=driving\
              &avoid=%s\
              &language=en" %
             (orig_coord, dest_coord, avoid)).split())
    try:
        result = simplejson.load(urllib.urlopen(url))
    except IOError:
        print("Connection Error with Google Maps API!")
        sys.exit()
    try:
        distance = result['rows'][0]['elements'][0]['distance']
        driving_time = result['rows'][0]['elements'][0]['duration']
    except:
        print("Error! Please enter the correct coordinates or parameters!")
        sys.exit()
    print("From: %s %s" % (result['origin_addresses'][0], orig_coord))
    print("To: %s %s" % (result['destination_addresses'][0], dest_coord))
    print("Distance: %s. (%s m.)" % (distance['text'], distance['value']))
    print("Driving Time: %s. (%s sec.)" % (driving_time['text'], driving_time['value']))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--orig', required=True, help='Coordinates of the starting point')
    parser.add_argument('--dest', required=True, help='Coordinates of the finish point')
    parser.add_argument('--avoid', help='Avoid the highway, toll, ferries, indoor')
    start_calc(parser.parse_args().orig,
               parser.parse_args().dest,
               parser.parse_args().avoid)
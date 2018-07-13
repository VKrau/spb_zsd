# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:21:54 2018

@author: VK
"""
from __future__ import absolute_import
from __future__ import print_function
import simplejson
import urllib
import sys
import re

def coord2text(coord):
    return ",".join(map(lambda x: str(x), coord))

def start_calc(orig, dest):
    #orig_coord = 59.97241,30.2133597
    #dest_coord = 59.9177427,30.2103535
    orig_coord = orig
    dest_coord = dest
    url = str("http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&mode=driving&language=en-EN&sensor=false" % 
             (coord2text(orig_coord), coord2text(dest_coord)))
    
    result = simplejson.load(urllib.urlopen(url))
    distance = result['rows'][0]['elements'][0]['distance']
    driving_time = result['rows'][0]['elements'][0]['duration']
    
    print("From: %s %s" % (result['origin_addresses'][0], orig_coord))
    print("To: %s %s" % (result['destination_addresses'][0], dest_coord))
    print("Distance: %s. (%s m.)" % (distance['text'], distance['value']))
    print("Driving Time: %s. (%s sec.)" % (driving_time['text'], driving_time['value']))
    
if __name__ == "__main__":
    argv_string = ' '.join(sys.argv[1:])
    orig = re.findall(r'--orig (\w+.\w+,\w+.\w+)', argv_string)
    dest = re.findall(r'--dest (\w+.\w+,\w+.\w+)', argv_string)
    try:
        start_calc(orig, dest)
    except:
        print("Please enter the correct coordinates!")
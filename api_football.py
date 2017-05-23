# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:42:57 2017

@author: smadvani
"""
# http.client = py3 version
#import http.client
import httplib
import json

def fixtures():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '7d8ec6405f2f43bca384af37191f7eba', 'X-Response-Control': 'minified' }
    connection.request('GET', '/v1/competitions/426/fixtures/', None, headers )
    response = json.loads(connection.getresponse().read().decode())
    return response

print fixtures()["fixtures"]


  


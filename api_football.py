# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:42:57 2017

@author: smadvani
initial def structure from api examples
"""
# http.client = py3 version
#import http.client
import httplib
import json


def leagues():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '7d8ec6405f2f43bca384af37191f7eba', 'X-Response-Control': 'minified' }
    connection.request('GET', '/v1/competitions/', None, headers )
    #response returns a list of dictionaries
    response = json.loads(connection.getresponse().read())
    return response

def fixtures(league_id):
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '7d8ec6405f2f43bca384af37191f7eba', 'X-Response-Control': 'minified' }
    connection.request('GET', '/v1/competitions/'+str(league_id)+'/fixtures/', None, headers )
    response = json.loads(connection.getresponse().read())
    return response

lgdict = {}
lg =[]
for i in leagues():
    #lgdict = dict.fromkeys('id',)
    # lg = list of lists
    lg.append([i['id'], i['year'], i['league'], i['caption']])
    #print i['id'],'    ', i['year'],'    ', i['league'],'    ', i['caption']
#print lg
#print lgdict

#print lg[0]

for i in lg:
#    print i  ## returns each list
    if unicode(i[3]) == 'Premier League 2017/18':
       lg_id = i[0]
       
    
#print lg_id
    
#print '/v1/competitions/'+str(lg_id)+'/fixtures/'
fixture_redux = []
dict1 = {}
for i in fixtures(lg_id)['fixtures']:
    fixture_redux.append([i['homeTeamName'], i['matchday'], i['awayTeamName'], i['date'], i['result']])
print fixture_redux
    
        


  


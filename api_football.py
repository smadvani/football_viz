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

#! start postgres with: sudo service postgresql start
def cnxn():
    db = 'football_viz'
    usr = 'sadvani'
    host = 'localhost'
    port = '5432'
    pw = 'pg95'
    cs = "dbname=%s user=%s password=%s host=%s port=%s" %(db,usr,pw,host,port)
    return cs

#print connect()
#try:
#    con = pg.connect(connect())
#    print 'connected'
#    con.close()
#except:
#    print 'connection failed'

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
    
def teams(league_id):
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '7d8ec6405f2f43bca384af37191f7eba', 'X-Response-Control': 'minified' }
    connection.request('GET', '/v1/competitions/'+str(league_id)+'/teams/', None, headers )
    response = json.loads(connection.getresponse().read())
    return response

  
#print fixtures(445)
    
#print '/v1/competitions/'+str(lg_id)+'/fixtures/'
#fixture_redux = []
#dict1 = {}
#for i in fixtures(lg_id)['fixtures']:
#    fixture_redux.append([i['homeTeamName'], i['matchday'], i['awayTeamName'], i['date'], i['result']])
#print fixture_redux
# 
#for league in leagues():
#    print league['year']
        


  


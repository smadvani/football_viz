# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 21:01:30 2017

@author: smadvani
run weekly during season
"""

import api_football as gts
import psycopg2 as pg

def pop_res(): #insert at beginning of season
    con = pg.connect(gts.cnxn())
    cur = con.cursor()
    sel_ids = "select l.api_id as lg_id, f.api_id as fx_id from league as l inner join fixtures as f on f.league_id = l.id where date_played is null"
    cur.execute(sel_ids)
    apids = cur.fetchall()
    league_fixture = {}
    lg = ''
    #fix == ''
    for apid in apids:
        if apid[0] != lg:
            lg = apid[0]
            fix_list = []
            fix_list.append(apid[1])
            league_fixture[apid[0]] = fix_list
        else:
            fix_list.append(apid[1])
            league_fixture[apid[0]] = fix_list
#    print league_fixture
    for league in league_fixture:
        results = gts.fixtures(league)
        for match in league_fixture[league]:
            #match = the api id for the match - set up to get the result 
            
if __name__ == "__main__":
    pop_res()
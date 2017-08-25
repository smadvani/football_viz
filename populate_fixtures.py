# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:12:38 2017

@author: smadvani
use to populate db tables
"""

import api_football as gts
import psycopg2 as pg



def pop_lg():
#    lgdict = {}
    lg =[]
    for i in leagues():
        #lgdict = dict.fromkeys('id',)
        # lg = list of lists
        lg.append([i['id'], i['year'], i['league'], i['caption']])
        #print i['id'],'    ', i['year'],'    ', i['league'],'    ', i['caption']
    #print lg
    #print lgdict
    
    
    con = pg.connect(cnxn())
    insrt = 'insert into league (name, api_id) values'
    
    for i in lg:
        lg_nm = (i[3].replace('2017/18','')).replace('2017','').strip().encode('utf-8').decode('ascii','ignore')
        apid = i[0]    
        insrt = insrt+"('"+ lg_nm+"',"+str(apid)+"),"
        #print i  ## returns each list
    #    if unicode(i[3]) == 'Premier League 2017/18':
    #       lg_id = i[0]
    insrt = insrt[:-1]+';'
    #print insrt
    cur = con.cursor()
    
    cur.execute(insrt)
    con.commit()
    con.close()
    
def pop_team():
    
    con = pg.connect(gts.cnxn())
    cur = con.cursor()
    sel_lg = "select api_id, id from league;"
    cur.execute(sel_lg)
    apiid = cur.fetchall()
    for i in apiid:
        insrt = 'insert into teams (name, short_name) values'
        teams = gts.teams(i[0])
        for team in teams['teams']:
            nm = "'"+team['name'].encode('utf-8').decode('ascii','ignore')+"'"
            if team['shortName'] is None:
                sn = 'null'
            else:
                sn = "'"+team['shortName'].encode('utf-8').decode('ascii','ignore')+"'"
            insrt = insrt+"("+nm+", "+sn+"), "
        insrt = insrt[:-2]+';'
#        print insrt
        cur = con.cursor()
        cur.execute(insrt)
        con.commit()
        con.close()
        #print gts.teams(i[0])
        #print gts.fixtures(i[0])['fixtures'][0]


def pop_fix():
    a = 1
#    fix = gts.fixtures(443)
#    lgs = gts.leagues()
    #for i in apiid:
#    print gts.fixtures(i[0])
    
if __name__ == "__main__":
    pop_lg()
    pop_team()
    pop_fix()
         
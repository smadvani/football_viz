# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 20:12:38 2017

@author: smadvani
use to populate db tables - run once a year when tables are updated.  Aug 1?
populate results should look at 
"""

import api_football as gts
import psycopg2 as pg
import string as st
import datetime as dt



def pop_lg():
#    lgdict = {}
    lg =[]
    for i in gts.leagues():
        #lgdict = dict.fromkeys('id',)
        # lg = list of lists
        lg.append([i['id'], i['year'], i['league'], i['caption']])
        #print i['id'],'    ', i['year'],'    ', i['league'],'    ', i['caption']
    #print lg
    #print lgdict
    
    
    con = pg.connect(gts.cnxn())
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
    #b/c teams are in multiple leagues, teams is not giving a unique list - FIX
    con = pg.connect(gts.cnxn())
    cur = con.cursor()
    sel_lg = "select api_id, id from league;"
    cur.execute(sel_lg)
    teamname = []
    apiid = cur.fetchall()
    for i in apiid:
        insrt = 'insert into teams (name, short_name) values'
        teams = gts.teams(i[0])
        #! one element does not have team - only do if there is the key "team"
        if 'teams' in teams:
            #print teams
            for team in teams['teams']:
                if team['name'] not in teamname:
    #                print team['id']
    #                print team['name'].encode('utf-8').decode('ascii','ignore')
                    nm = "'"+team['name'].encode('utf-8').decode('ascii','ignore')+"'"
                    if team['shortName'] is None or team['shortName']=="":
                        sn = 'null'
                    else:
                        #! Kaiserslautern has short name of "K'lautern"
                        sn = "'"+st.replace(team['shortName'].encode('utf-8').decode('ascii','ignore'), "K'l", "Kl")+"'"
                    insrt = insrt+"("+nm+", "+sn+"), "
                teamname.append(team['name'])
                #print team['name']
                #print teamname
            insrt = insrt[:-2]+';'
            #print insrt
            cur = con.cursor()
            cur.execute(insrt)
            con.commit()
    con.close()
        #print gts.teams(i[0])
        #print gts.fixtures(i[0])['fixtures'][0]
        
def pop_season():
    con = pg.connect(gts.cnxn())
    cur = con.cursor()
    for league in gts.leagues():
        sel_seas = "select season from season;"
        cur.execute(sel_seas)
        seasons = cur.fetchall()
        #print len(seasons), str(league['year'])
        if len(seasons)==0 or league['year'] not in seasons[0][0]:
                insrt= 'insert into season (season) values ('+league['year']+');'
                cur = con.cursor()
                cur.execute(insrt)
                con.commit()
    con.close()

def pop_season_team_leag():
    con = pg.connect(gts.cnxn())
    cur = con.cursor()
    sel_lg = "select api_id from league"
    cur.execute(sel_lg)
    apids = cur.fetchall()
    insrt = "insert into league_team (league_id, team_id, season_id) values "
    for league in apids:
        #print league[0]
        lg_api_id = league[0]
        #print lg_api_id
        teams = gts.teams(lg_api_id)
#        print '-----'+str(lg_api_id)+'---------'        
#        print teams
        if 'teams' in teams:
            for team in teams['teams']:
                #print team['name']
                nm = "'"+team['name'].encode('utf-8').decode('ascii','ignore')+"'"
                #print nm                
                insrt = insrt + "((select id from league where api_id = "+str(lg_api_id)+"),(select id from teams where name = "+nm+"), (select id from season where season = '2017'))," 
    insrt = insrt[:-1]+';'
    #print insrt
    cur.execute(insrt)
    con.commit()
    con.close()
    
def pop_fix(): #insert at beginning of season
    con = pg.connect(gts.cnxn())
    cur = con.cursor()
    sel_lg = "select api_id from league"
    cur.execute(sel_lg)
    apids = cur.fetchall()
    fix_list = []
    for league in apids:
        #print int(league[0])
        fix = gts.fixtures(int(league[0]))
        if 'error' not in fix:
            fix_list.append(fix['fixtures'])
    #print fix_list[1]
    insrt_fx = 'insert into fixtures (api_id, league_id, home_team_id, away_team_id, scheduled_date) values '
    for fixture in fix_list:
        for fix in fixture:
            #convert time to timestamp format for PG
            sch_date = (fix['date'].replace('T', ' '))[:-4]
            insrt_fx = insrt_fx + "("+str(fix['id']) + ", (select id from league where api_id = "+str(fix['competitionId'])+"), (select id from teams where name = '"+ fix['homeTeamName'].encode('utf-8').decode('ascii','ignore')+"'), (select id from teams where name = '"+ fix['awayTeamName'].encode('utf-8').decode('ascii','ignore')+"'), '" + sch_date+"'),"
    insrt_fx = insrt_fx[:-1]+';'    
#    print insrt_fx
    cur.execute(insrt_fx)
    con.commit()
    con.close()
    

    
if __name__ == "__main__":
    pop_lg()
    pop_season()    
    pop_team()
    pop_season_team_leag()
    pop_fix()
         
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:26:01 2017

@author: smadvani
can not create or drop in tnacnt block - create outside of script then run other ddl
"""
import psycopg2 as pg

def cnxn():
    db = 'football_viz'
    usr = 'sadvani'
    host = 'localhost'
    port = '5432'
    pw = 'pg95'
    cs = "dbname=%s user=%s password=%s host=%s port=%s" %(db,usr,pw,host,port)
    return cs

def create_db():
    con = pg.connect(cnxn())
    cur = con.cursor()
    ddl_file = open('//home/smadvani/Documents/development/football_viz/football_viz_ddl.sql', 'r')
    cur.execute(ddl_file.read())
    con.commit()   
    con.close()
    
def test_create():
    tst_sql = "select distinct table_name from information_schema.columns where table_schema = 'public';"
    con = pg.connect(cnxn())
    cur = con.cursor()
    cur.execute(tst_sql)
    tbls = cur.fetchall()
    print tbls
    
if __name__ == "__main__":
    create_db()
    test_create()

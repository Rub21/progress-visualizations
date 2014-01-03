#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


con = lite.connect('jacksonville.sqlite')    

with con:
    
    con.row_factory = lite.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM mapathon WHERE user='ediyes'")

    rows = cur.fetchall()
    
    for row in rows:
        print "%s %s %s" % (row["timestamp"], row["user"], row["version"])
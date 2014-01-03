#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


con = lite.connect('jacksonville.sqlite')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM mapathon WHERE user='ediyes'")

    rows = cur.fetchall()
    print rows

    #for row in rows:
        #print row
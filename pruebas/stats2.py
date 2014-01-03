#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('jacksonville.sqlite')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM mapathon WHERE user='ediyes'")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0]
#!/usr/bin/python

import sqlite3 as lite
import prettytable

con = lite.connect('jacksonville.sqlite')    

with con:
    
    con.row_factory = lite.Row       
    cur = con.cursor() 
    cur.execute("SELECT user, count(*) as v1 FROM mapathon group by user order by   v1 desc") # or SELECT user FROM mapathon group by user order by user
    rows = cur.fetchall()
    table =  prettytable.PrettyTable(["User", "Nodes V=1", "Nodes V>1"])
    for row in rows:
        user=row["user"]
        #print user
        #get version =1 by user
        cur.execute("SELECT count(*) as version1 FROM mapathon WHERE user=:user and version =1", {"user": user}) 
        con.commit() 
    	row_v1= cur.fetchone()    	
    	row_v1=row_v1[0] 
    	#get version !=1  by user
        cur.execute("SELECT count(*) as version1 FROM mapathon WHERE user=:user and version !=1", {"user": user}) 
        con.commit() 
    	row_vx = cur.fetchone()
    	row_vx=row_vx[0]
    	table.add_row([user,row_v1, row_vx])
    print table

        
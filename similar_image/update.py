#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json
from jubatus.recommender import client
from jubatus.recommender import types
import MySQLdb

NAME = "";

if __name__ == "__main__":

    recommender = client.recommender("localhost",9199)

    # Clear previous data.
    recommender.clear(NAME)

    # Update data.
    connector = MySQLdb.connect(host="localhost",db="jubatus_sample",user="root",passwd="")
    cursor = connector.cursor()
    cursor.execute("select * from plus_info_1")
    result = cursor.fetchall()

    print "============= Update"
    for row in result: 
        userid = row[0]
        fromuserid = row[3]
        if userid != 1 and userid != fromuserid:
            print "============= userid:" + str(userid)
            imageid = str(row[1])
            datum = types.datum( [], [[str(userid), float(1)]] )
            recommender.update_row(NAME, imageid, datum)


    cursor.close()
    connector.close()


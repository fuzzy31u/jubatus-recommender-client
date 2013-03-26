#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, json
from jubatus.recommender import client
from jubatus.recommender import types
import MySQLdb

NAME = "";

if __name__ == "__main__":

    recommender = client.recommender("localhots",9199)

    # Clear previous data.
    recommender.clear(NAME)

    # Update data.
    connector = MySQLdb.connect(host="localhost",db="jubatus_sample",user="root",passwd="")
    cursor = connector.cursor()
    cursor.execute("select * from plus_info_1")
    result = cursor.fetchall()

    print "============= Update"
    for row in result: 
        userid = str(row[0])
#        imageid = str(row[1])
#        print "user_id -- " + userid
#        print "image_id -- " + imageid
        datum = types.datum( [], [[str(row[1]), float(1)]] )
        recommender.update_row(NAME, userid, datum)


    cursor.close()
    connector.close()


#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from jubatus.recommender import client
from jubatus.recommender import types
import MySQLdb

if __name__ == "__main__":

    recommender = client.recommender("localhost",9199)

    # Analyze
    connector = MySQLdb.connect(host="localhost",db="jubatus_sample",user="root",passwd="")
    cursor = connector.cursor()
    cursor.execute("select * from plus_info_1 limit 1000")
    result = cursor.fetchall()

    list = []
    for row in result:
        imageid = row[1]                            
        if imageid not in list and row[0] != 1:
            print "============= Analyze"
            list.append(imageid)

            sr = recommender.similar_row_from_id("", str(imageid) , 10);
            print "image ", str(imageid),  " is similar to :", sr

    cursor.close()
    connector.close()

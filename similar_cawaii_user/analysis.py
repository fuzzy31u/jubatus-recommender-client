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
    cursor.execute("select * from plus_info_1")
    result = cursor.fetchall()

    list = []
    for row in result:
        userid = row[0]                            
        if userid not in list:
            print "============= Analyze"
            list.append(userid)

            sr = recommender.similar_row_from_id("", str(userid) , 3);
            print "user ", str(userid),  " is similar to :", sr

    cursor.close()
    connector.close()

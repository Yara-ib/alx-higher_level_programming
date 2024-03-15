#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


connection = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    charset='utf8'
    )

cur = connection.cursor()
cur.execute('SELECT * FROM `states` ORDER BY `id`')
output = cur.fetchall()
for row in output:
    print(row)

cur.close()
connection.close()

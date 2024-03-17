#!/usr/bin/python3
"""
    Script that takes in an argument &
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    cur = connection.cursor()
    sql_query = 'SELECT * FROM `states` WHERE BINARY name = %s ORDER BY id'
    cur.execute(sql_query, (argv[4],))

    for row in cur.fetchall():
        print(row)

    cur.close()
    connection.close()

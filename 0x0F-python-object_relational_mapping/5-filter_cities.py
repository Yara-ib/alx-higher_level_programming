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
    cur.execute(
        'SELECT cities.name FROM `cities`'
        'JOIN `states`'
        'ON cities.state_id = states.id WHERE BINARY states.name = "{}"'
        'ORDER BY cities.id'
        .format(argv[4])
    )

    rows = cur.fetchall()
    for idx, row in enumerate(rows):
        if idx == len(rows) - 1:
            print(row[0])
        else:
            print(row[0], end=", ")

    cur.close()
    connection.close()

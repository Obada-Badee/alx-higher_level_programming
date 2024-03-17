#!/usr/bin/python3
"""
a script that takes in a state as an argument and lists all cities
script should take 4 arguments:
    mysql username, mysql password, database name and state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    query = "SELECT cities.name FROM cities\
             INNER JOIN states ON cities.state_id = states.id\
             WHERE states.name=%s\
             GROUP BY cities.id"
    cursor.execute(query, (argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()

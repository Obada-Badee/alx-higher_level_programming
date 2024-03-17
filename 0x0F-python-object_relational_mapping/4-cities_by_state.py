#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
parameters given to script: username, password, database
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states WHERE cities.state_id=states.id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()

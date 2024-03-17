#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
parameters given to script: username, password, database, state
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
    query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(query, (argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()

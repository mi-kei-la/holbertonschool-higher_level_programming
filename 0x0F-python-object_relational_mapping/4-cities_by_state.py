#!/usr/bin/python3
"""Fetch all states and cities from database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect("localhost", username, password, db_name)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities LEFT JOIN states \
                   ON states.id = cities.state_id")
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()

#!/usr/bin/python3
"""This module makes a MySQL query."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    sql = "SELECT * FROM states \
           WHERE states.name LIKE 'N%' \
           ORDER BY states.id ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()

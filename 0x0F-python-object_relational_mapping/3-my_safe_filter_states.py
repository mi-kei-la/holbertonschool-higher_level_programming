#!/usr/bin/python3
"""This module makes a MySQL query."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    search = argv[4]
# Open connection to database.
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
# MySQL Query.
    sql = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    for row in results:
        print(row)
# Close the connections.
    cursor.close()
    db.close()

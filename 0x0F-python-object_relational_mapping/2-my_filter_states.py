#!/usr/bin/python3
"""This module makes a MySQL query."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Open connection to database.
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
# MySQL Query.
    sql = "SELECT * FROM states \
           WHERE name = '{}' \
           ORDER BY states.id ASC;".format(argv[4])
# Execute query.
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        if row[1] == argv[4]:
            print(row)
# Close the connections.
    cursor.close()
    db.close()

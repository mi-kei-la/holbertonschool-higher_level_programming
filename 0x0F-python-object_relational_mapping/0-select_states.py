#!/usr/bin/python3
"""This module makes a MySQL query."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
# Open connection to database.
    db = MySQLdb.connect("localhost", username, password, db_name)
    cursor = db.cursor()
# MySQL Query.
    sql = "SELECT * FROM {}.states \
           ORDER BY states.id ASC;".format(db_name)
# Execute query.
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
# Close the connections.
    cursor.close()
    db.close()

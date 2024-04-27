#!/usr/bin/env python3

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: ./<script-name>.py [username] [password] "
              "[database] [state]")
        sys.exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4], ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

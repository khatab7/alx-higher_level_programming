#!/usr/bin/env python3

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./<script-name>.py [username] [password] [database]")
        sys.exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT a.id, a.name, b.name "
                "FROM cities a "
                "RIGHT JOIN states b "
                "ON a.state_id = b.id "
                "ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

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
    cur.execute("SELECT b.name "
                "FROM states a "
                "LEFT JOIN cities b "
                "ON a.id = b.state_id "
                "WHERE a.name = %s "
                "ORDER BY b.id ASC",
                (sys.argv[4], ))
    query_rows = cur.fetchall()
    query_len = len(query_rows)
    for i in range(query_len):
        if i < query_len - 1:
            print(query_rows[i][0], end=', ')
        else:
            print(query_rows[i][0])
    cur.close()
    db.close()

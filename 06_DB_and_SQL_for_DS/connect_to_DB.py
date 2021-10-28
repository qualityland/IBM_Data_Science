## Objects:
# - Connection          - Cursor

## Connection methods:
#   cursor()            rollback()
#   commit()            close()

## Cursor methods:
#   callproc()          fetchall()
#   execute()           nextset()
#   executemany()       arraysize()
#   fetchone()          close()
#   fetchmany()

from dbmodule import connect

# create connection object
conn = connect('databasename', 'username', 'pswd')

# create cursor object
cur = conn.cursor()

# run queries
cur.execute('select * from mytable')
results = cur.fetchall()

# free resources
cur.close()
conn.close()

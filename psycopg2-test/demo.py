# python-postgresql DBAPI
import psycopg2

# establishing connection to the database
 
connection = psycopg2.connect('dbname=example')

# start of session
# `cursor` starts up an interface to enable begin of transactions

cursor = connection.cursor()

# delete table to prevent duplication
cursor.execute('DROP TABLE IF EXISTS table2')

# start of transactions: ie small units of work, using SQL commands
cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT false
    );
''')

cursor.execute(' INSERT INTO table2 (id, completed) VALUES (1, true);')


#string interpolation/composition
#method1
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, True))

#method2
#string interpolation using named variables
cursor.execute('INSERT INTO table2 (id, completed)' + 
' VALUES ( %(id)s, %(completed)s);', {
    'id': 3,
    'completed': False
})

#method3
data = {
    'id': 4,
    'completed': False
}

SQL = 'INSERT INTO table2 (id, completed) VALUES ( %(id)s, %(completed)s);'

cursor.execute(SQL, data)

## fetching and displaying data in tabel2
# to fetch all
cursor.execute('SELECT * FROM table2')

result = cursor.fetchall()
#print('fetch all:' ,result)

#fetch one
result2 = cursor.fetchone()
#print('fetch one: ', result2)

#fetch many: will fetch only the first 2
result3 = cursor.fetchmany(3)
print('fetch many: ', result3)

# End of transaction where new records are saved 
# in the DB (table2)
connection.commit() 

# end of session
connection.close()
cursor.close()


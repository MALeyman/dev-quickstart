# https://github.com/atkindel/dbutils/blob/master/dbutils.py

import mysql.connector
from contextlib import contextmanager
from functools import wraps

class Database:
    def __init__(self, username, password, db, host='127.0.0.1', port=3306):
        self.username = username
        self.password = password
        self.db = db
        self.host = host
        self.port = port
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            database=db,
            autocommit=True
        )
        self.cursors = []

    @contextmanager
    def cursor(self):
        curs = self.connection.cursor(dictionary=True)
        self.cursors.append(curs)
        yield curs
        for cursor in self.cursors:
            cursor.close()
        self.connection.close()

def query(cursor, query, fetchall=False):
    cursor.execute(query)
    results = cursor.fetchall() if fetchall else (row for row in cursor)
    return results if fetchall else results

def insert(cursor, table, cols, vals):
    placeholders = ', '.join(['%s'] * len(cols))
    query = f"INSERT INTO {table} ({', '.join(cols)}) VALUES ({placeholders})"
    status = cursor.execute(query, vals)
    return status

def with_db(dbcfg):
    def db_call(f):
        @wraps(f)
        def db_wrap(*args, **kwargs):
            with Database(**dbcfg) as db:
                with db.cursor() as cursor:
                    return f(db, cursor, *args, **kwargs)
        return db_wrap
    return db_call

class InstanceException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def dev_only(f):
    @wraps(f)
    def dev_wrap(*args, **kwargs):
        if 'DEV_INSTANCE' in globals() and globals()['DEV_INSTANCE']:
            return f(*args, **kwargs)
        else:
            raise InstanceException("Method is disabled for instances not in development.")
    return dev_wrap

if __name__ == '__main__':
    import os
    dbcfg = {
        'username': 'unittest',
        'password': 'unittest',
        'db': 'unittest',
        'host': os.environ.get('DB_HOST', '127.0.0.1'),
        'port': int(os.environ.get('DB_PORT', '3306'))
    }

    # Test queries
    print("Testing query()")
    with mysql.connector.connect(**dbcfg) as conn:
        with conn.cursor(dictionary=True) as cursor:
            for result in query(cursor, 'SELECT * FROM unittest.unittest'):
                print(result)
    
    # Test inserts
    print("Testing insert()")
    with mysql.connector.connect(**dbcfg) as conn:
        with conn.cursor() as cursor:
            status = insert(cursor, table='unittest.unittest', cols=['b'], vals=['unittest'])
            assert status

    # Test decorator
    print("Testing @with_db")
    @with_db(dbcfg)
    def get_results(db, cursor, query_text):
        with db.cursor() as cursor:
            for row in query(cursor, query_text):
                print(row)
    get_results('SELECT * FROM unittest.unittest')

    @with_db(dbcfg)
    def insert_many(db, cursor, table, cols, vals):
        for row in vals:
            status = insert(cursor, table, cols, row)
            print("Inserted another row.")
    rows = [['u'], ['n'], ['i'], ['t'], ['t'], ['e'], ['s'], ['t']]
    insert_many(table='unittest.unittest', cols=['b'], vals=rows)


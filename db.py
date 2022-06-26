import sqlite3
from sqlite3 import Error
import os


def _create_connection(db_file):
    """ 
        create a database connection to a SQLite database 
        Sqlite version 2.6.0
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        return False

def _create_table(conn, create_table_sql):
    """ 
        create a table from to tanegelo_test.db
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("created")
    except Error as e:
        print(e)

def create_database():
    path = os.getcwd() + r"\tanegelo_test.db"
    conn = _create_connection(path)

    if conn is not None:
        sql_create_data = """ CREATE TABLE IF NOT EXISTS data (
                                            id integer PRIMARY KEY,
                                            total_time real NOT NULL,
                                            time_average real NOT NULL,
                                            time_min real NOT NULL,
                                            time_max real NOT NULL
                                        ); """

        _create_table(conn, sql_create_data)
    else:
        print("Error! cannot create the database connection.")

create_database()
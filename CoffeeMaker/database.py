import sqlite3

from tables import Description

CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT COLLATE NOCASE, method TEXT, rating INTEGER);"
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES(?, ?, ?);"
GET_ALL_BEAN = "SELECT * FROM beans"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
EXISTS (WHERE name = ?)
ORDER BY rating DESC
LIMIT 1; """
GET_METHODS_TO_RATING = "SELECT method, AVG(rating) from beans GROUP BY method;"
DELETE_BEANS = "DELETE FROM beans WHERE name = ?"

def connect():
    return sqlite3.connect("date.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def add_bean(connection, name, method, rating):
    with connection:
        connection.execute(INSERT_BEAN, (name, method, rating))

def get_all_beans(connection):
    with connection:
        # if connection.execute(GET_ALL_BEAN).fetchall() == 0:
        #     return f"NULL"
        return connection.execute(GET_ALL_BEAN).fetchall()

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

def get_best_prepartion_for_bean(connection, name):
    with connection:
        # if connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)) == 0:
        #     return f"NULL"    
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()



def get_methods_to_ratings(connection):
    with connection:
        return connection.execute(GET_METHODS_TO_RATING).fetchall()

def delete_bean(connection, name):
    with connection:
        connection.execute(DELETE_BEANS, (name,))
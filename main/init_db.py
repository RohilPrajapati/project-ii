import os
import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host="localhost",
        database="solver",
        user='postgres',
        password='prajapati')
    return conn

if __name__ == '__main__':
    conn = get_db_connection()
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # create table for projects
    cur.execute('DROP TABLE IF EXISTS users;')
    cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                    'username varchar (150) NOT NULL UNIQUE,'
                                    'email varchar(150) NOT NULL UNIQUE,'
                                    'password varchar(255) NOT NULL,'
                                    'is_active boolean default TRUE);'
                                    
                                    )

    conn.commit()

    cur.close()
    conn.close()
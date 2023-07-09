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
    cur.execute('DROP TABLE IF EXISTS users cascade;')
    cur.execute('CREATE TABLE users (id SERIAL  PRIMARY KEY ,'
                                    'username varchar (150) NOT NULL UNIQUE,'
                                    'email varchar(150) NOT NULL UNIQUE,'
                                    'password varchar(255) NOT NULL,'
                                    'is_active boolean default TRUE);'
                                    )
    conn.commit()

    # hash = test
    h_password = 'pbkdf2:sha256:600000$qPDtVk3cuipq41jN$7dbb775e25ac9ccfa17f05ada3a6f2d995529278cecdfac45457191c1b558335'
    
    # create the first user
    cur.execute(f"Insert Into users (id,username,email,password,is_active) values (1,'test_user','test_user@gmail.com','{h_password}','t');")
    conn.commit()


    # create query table for store the query for visualzier
    cur.execute('DROP TABLE IF EXISTS query cascade;')
    cur.execute('CREATE TABLE query (id SERIAL  PRIMARY KEY ,'
                                    'algo varchar (150) NOT NULL,'
                                    'equation varchar(150) NOT NULL,'
                                    'a_val int NOT NULL,'
                                    'b_val int,'
                                    'user_id int,'
                                    'FOREIGN KEY(user_id)  REFERENCES users(id) ON DELETE SET NULL);'
                                    )

    conn.commit()

    cur.close()
    conn.close()
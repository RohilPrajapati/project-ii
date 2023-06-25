from main.init_db import get_db_connection
import psycopg2.extras

def create_user(username,email,password,is_active=True):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, email, password,is_active)'
            'VALUES (%s, %s, %s,%s)',
                (
                username,
                email,
                password,
                is_active
             )
            )
    conn.commit()
    cur.close()
    conn.close()

def fetch_user(username):
    conn = get_db_connection()
    with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
        SQL = f"Select * from users where username='{username}'"
        curs.execute(SQL)
        print(f"Select * from users where username='{username}'")
        result = curs.fetchone()
    return result

def fetch_users():
    conn = get_db_connection()
    with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
        SQL = f"Select * from users order by id asc"
        curs.execute(SQL)
        result = curs.fetchall()
    return result

def fetch_user_by_id(id):
    conn = get_db_connection()
    with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
        SQL = f"Select * from users where id='{id}'"
        curs.execute(SQL)
        user = curs.fetchone()
    return user

def toggle_status_user(id):
    conn = get_db_connection()
    with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
        print(id)
        SQL = f"Select * from users where id='{id}'"
        curs.execute(SQL)
        user = curs.fetchone()
        if user['is_active']:
            SQL = f"Update users set is_active='f' where id='{id}'"
        else:
            SQL = f"Update users set is_active='t' where id='{id}'"
        curs.execute(SQL)
        conn.commit()
        # result = curs.fetchone()
    return None
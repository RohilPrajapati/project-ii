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

def insert_query(algo,eqn,a,b,user_id=None):
    conn = get_db_connection()
    with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
        if user_id:
            check_sql = f'select * from query where user_id = {user_id} order by id desc LIMIT 1'
            curs.execute(check_sql)
            query = curs.fetchone()
            print(query)
            # print(query['algo'] != algo and query['equation'] != eqn and query['a_val'] != a and query['a_val'] != b)
            if query:
                if query['algo'] != algo or query['equation'] != eqn or query['a_val'] != int(a) or query['b_val'] != int(b):  
                    sql = f"Insert into query(algo,equation,a_val,b_val,user_id) values ('{algo}','{eqn}',{a},{b},{user_id});"
                    curs.execute(sql)
                    conn.commit()
    return None

def fetch_user_history(user_id):
    conn = get_db_connection()
    with conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as curs:
        SQL = f"Select * from query where user_id='{user_id}' order by id desc limit 10"
        curs.execute(SQL)
        query = curs.fetchall()
    return query 
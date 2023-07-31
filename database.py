import sqlite3


async def db_start():
    global db, cursor
    db = sqlite3.connect('user.db')
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, task TEXT, deadline TEXT);")
    db.commit()


async def add_task(task: str, deadline: str, user_id: int):
    cursor.execute("INSERT INTO users (id, task, deadline) VALUES({},'{}','{}');".format(user_id, task, deadline))
    db.commit()


async def get_user_tasks(user_id: int):
    return cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id)).fetchall()


async def delete_task(task_name: str, user_id: int):
    cursor.execute("DELETE FROM users WHERE id ={} AND task = '{}'".format(user_id, task_name))
    db.commit()

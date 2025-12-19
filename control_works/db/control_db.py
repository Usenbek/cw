import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_PUR)
    print("База данных подключена!")
    conn.commit()
    conn.close()


def add_pur(pur):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT, (pur,))
    conn.commit()
    pur_id = cursor.lastrowid
    conn.close()
    return pur_id


def get_pur(filter):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter == "Купленные":
        cursor.execute(queries.SELECT_PUR_BUY)
    elif filter == "Не купленные":
        cursor.execute(queries.SELECT_PUR_NOT) 
    else:
        cursor.execute(queries.SELECT)
    conn.commit()
    purs = cursor.fetchall()
    conn.close()
    return purs

def update_pur(pur_id, buyed=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if buyed is not None:
        cursor.execute("UPDATE purs SET buyed = ? WHERE id = ?", (buyed, pur_id))
    conn.commit()
    conn.close()


def delete_pur(pur_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_PUR, (pur_id, ))
    conn.commit()
    conn.close()
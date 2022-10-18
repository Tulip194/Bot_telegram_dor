import sqlite3 as sql
import config
from aiogram.utils.markdown import hlink
from datetime import datetime, time
from time import gmtime, strftime
import shutil
import random
import pandas as pd
#~~~~~~~~~Получение ид пользователя~~~~~~~~~~~#
def user(id):
    con = sql.connect("users.db")
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT,stat INT, message TEXT)")
        x = []
        for i in range(11):
            x.append(i)
        if '@' not in str(id):
            info = cur.execute(f"SELECT * FROM users WHERE id=('{id}')")
        elif id[0] not in x:
            info = cur.execute(f"SELECT * FROM users WHERE Nick=('{id}')")
        else:
            info = cur.execute(f"SELECT * FROM users WHERE login=('{id[1:]}')")
        return info.fetchone()
    con.commit()
    cur.close()

##########################################################################################################

def safemessage(id, Q1):
    con = sql.connect("users.db")
    info1= user(id)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, login TEXT, Nick TEXT,stat INT, message TEXT)")
        cur.execute(f'UPDATE users SET message="{Q1}" WHERE id={id}')
    con.commit()
    cur.close()
##########################################################################################################
# def queue(adminms, ):
#     con = sql.connect("users.db")
#     info= user(id)
#     with con:
#         cur = con.cursor()
#         cur.execute("CREATE TABLE IF NOT EXISTS `queue` (id INT PRIMARY KEY,Nick TEXT,numb INT, wishes TEXT)")
#         cur.execute(f'UPDATE users SET message="{Q1}" WHERE id={id}')
#     con.commit()
#     cur.close()

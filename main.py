import eel
import os
import hashlib
import pymysql
from base64 import b64encode
from email_validate import validate


def db_connect():
    db = pymysql.connect(host="127.0.0.1", port=3306,
                     user="mysql", passwd="mysql", database="scs:gop")
    return db


@eel.expose
def sign_up__f(email, nickname, password):
    try:
        if email == "" or nickname == "" or password == "":
            print(2)
            return "2"
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
        if len(cursor.fetchall()) == 0:
            c_e = validate(email_address=f"{email}")
            if c_e == True:
                salt = os.urandom(32)
                salt = b64encode(salt)
                key = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
                salt = salt.decode('utf-8')
                cursor.execute(f"INSERT INTO user (nickname, email, password, salt) VALUES ('{nickname}', '{email}', '{key}', '{salt}')")
                db.commit()
                db.close()
                print(1)
                return "1"
            else:
                db.close()
                print(2)
                return "2"
        else:
            db.close()
            print(3)
            return "3"
    except:
        print(0)
        return "0"



@eel.expose
def get__id(email):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(f"SELECT id FROM user WHERE email = '{email}'")
    id = cursor.fetchall()
    db.close()
    return id


@eel.expose
def sign_in__f(email, password):
    db = db_connect()
    cursor = db.cursor()
    print(db)
    cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
    if len(cursor.fetchall()) != 0:
        cursor.execute(f"SELECT salt FROM user WHERE email = '{email}'")
        salt = cursor.fetchall()
        salt = str(salt)[3 : -5]
        salt = salt.encode('utf-8')
        cursor.execute(f"SELECT password FROM user WHERE email = '{email}'")
        hesh = cursor.fetchall()
        hesh = str(hesh)[3 : -5]
        key = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
        if key == hesh:
            print(1)
            db.close()
            return "1"
        else:
            print(0)
            db.close()
            return "0"
    else:
        print(2)
        db.close()
        return "2"


@eel.expose
def get__nickname(email):
    db = db_connect()
    cursor = db.cursor()
    cursor.execute(f"SELECT nickname FROM user WHERE email = '{email}'")
    nickname = cursor.fetchall()
    db.close()
    return nickname


eel.init("web")
eel.start("sign_up.html", size=(500, 800), geometry={'rec_pass.html': {
          'size': (500, 400)}, 'sign_in.html': {'size': (500, 800)}, 'main.html': {'size': (1300, 500)}})

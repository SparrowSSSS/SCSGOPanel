import eel
import os
import hashlib
import pymysql
from base64 import b64encode
from email_validate import validate


def db_connect():
    try:
        db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="mysql", passwd="mysql", database="scs:gop")
        print("db_connect---Успешно")
        return db
    except:
        print("db_connect---Не удалось подключиться к базе")
        return None



@eel.expose
def sign_up__f(email, nickname, password):
    try:
        if email == "" or nickname == "" or password == "":
            print(f"sign_up---{email}---Пустые данные")
            return "2"
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
        if len(cursor.fetchall()) == 0:
            c_e = validate(
                email_address = f"{email}",
                check_format = False
                )
            if c_e == True:
                salt = os.urandom(32)
                salt = b64encode(salt)
                key = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
                salt = salt.decode('utf-8')
                cursor.execute(f"INSERT INTO user (nickname, email, password, salt) VALUES ('{nickname}', '{email}', '{key}', '{salt}')")
                db.commit()
                db.close()
                print(f"sign_up---{email}---Успешно")
                return "1"
            else:
                db.close()
                print(f"sign_up---{email}---Почта не прошла проверку")
                return "2"
        else:
            db.close()
            print(f"sign_up---{email}---Такой аккаунт уже есть")
            return "3"
    except:
        db.close()
        print(f"sign_up---{email}---Техническая ошибка")
        return "0"



@eel.expose
def get__id(email):
    try:
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM user WHERE email = '{email}'")
        id = cursor.fetchall()
        db.close()
        print(f"get__id---{email}---Успешно")
        return id
    except:
        db.close()
        print("get__id---{email}---Техническая ошибка")
        return "Не удалось достать"


@eel.expose
def sign_in__f(email, password):
    try:
        if email == "" or password == "":
            print(f"sign_up---{email}---Пустые данные")
            return "2"
        db = db_connect()
        cursor = db.cursor()
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
                db.close()
                print(f"sign_in---{email}---Успешно")
                return "1"
            else:
                db.close()
                print(f"sign_in---{email}---Неверный пароль")
                return "2"
        else:
            db.close()
            print(f"sign_in---{email}---Почта не найдена")
            return "2"
    except:
        db.close()
        print(f"sign_in---{email}---Техническая ошибка")
        return "0"



@eel.expose
def get__nickname(email):
    try:
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT nickname FROM user WHERE email = '{email}'")
        nickname = cursor.fetchall()
        db.close()
        print("get__nickname---{email}---Успешно")
        return nickname
    except:
        db.close()
        print("get__nickname---{email}---Техническая ошибка")
        return "Anonymus"



eel.init("web")
eel.start("sign_up.html", size=(500, 800), geometry={'rec_pass.html': {
          'size': (500, 400)}, 'sign_in.html': {'size': (500, 800)}, 'main.html': {'size': (1300, 500)}})

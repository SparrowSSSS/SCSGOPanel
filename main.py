import eel
import os
import hashlib
import pymysql
from base64 import b64encode
from email_validate import validate
import smtplib
from email.mime.text import MIMEText
import datetime

print("Программа успешно запущена")
print("---")

def db_connect():
    try:
        db = pymysql.connect(host="127.0.0.1", port=3306,
                             user="mysql", passwd="mysql", database="scs:gop")
        now = datetime.datetime.now()
        print(f"db_connect---{now.strftime('%H:%M')}---Успешно")
        print("---")
        return db
    except:
        now = datetime.datetime.now()
        print(f"db_connect---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return None


@eel.expose
def sign_up__f(email, nickname, password):
    try:
        if email == "" or nickname == "":
            now = datetime.datetime.now()
            print(f"sign_up__f---{now.strftime('%H:%M')}---Пустые данные")
            print("---")
            return "2.1"
        if len(password) < 8:
            now = datetime.datetime.now()
            print(f"sign_up__f---{now.strftime('%H:%M')}---Маленький пароль")
            print("---")
            return "2.2"
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
        if len(cursor.fetchall()) == 0:
            c_e = validate(
                email_address=f"{email}",
                check_format=False
            )
            if c_e == True:
                salt = os.urandom(32)
                salt = b64encode(salt)
                key = hashlib.sha256(password.encode(
                    'utf-8') + salt).hexdigest()
                salt = salt.decode('utf-8')
                cursor.execute(
                    f"INSERT INTO user (nickname, email, password, salt) VALUES ('{nickname}', '{email}', '{key}', '{salt}')")
                db.commit()
                db.close()
                now = datetime.datetime.now()
                print(f"sign_up__f---{now.strftime('%H:%M')}---Успешно")
                print("---")
                return "1"
            else:
                db.close()
                now = datetime.datetime.now()
                print(f"sign_up__f---{now.strftime('%H:%M')}---Почта не прошла проверку")
                print("---")
                return "2.1"
        else:
            db.close()
            now = datetime.datetime.now()
            print(f"sign_up__f---{now.strftime('%H:%M')}---Такой пользователь уже есть")
            print("---")
            return "3"
    except:
        db.close()
        now = datetime.datetime.now()
        print(f"sign_up__f---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return "0"


@eel.expose
def get__id(email):
    try:
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM user WHERE email = '{email}'")
        id = cursor.fetchall()
        id = str(id)[2: -4]
        db.close()
        now = datetime.datetime.now()
        print(f"get__id---{now.strftime('%H:%M')}---Успешно")
        print("---")
        return id
    except:
        db.close()
        now = datetime.datetime.now()
        print(f"get__id---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return "None"


@eel.expose
def sign_in__f(email, password):
    try:
        if email == "" or password == "":
            now = datetime.datetime.now()
            print(f"sign_in__f---{now.strftime('%H:%M')}---Пустые данные")
            print("---")
            return "2.1"
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
        if len(cursor.fetchall()) != 0:
            cursor.execute(f"SELECT salt FROM user WHERE email = '{email}'")
            salt = cursor.fetchall()
            salt = str(salt)[3: -5]
            salt = salt.encode('utf-8')
            cursor.execute(
                f"SELECT password FROM user WHERE email = '{email}'")
            hesh = cursor.fetchall()
            hesh = str(hesh)[3: -5]
            key = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
            if key == hesh:
                db.close()
                now = datetime.datetime.now()
                print(f"sign_in__f---{now.strftime('%H:%M')}---Успешно")
                print("---")
                return "1"
            else:
                db.close()
                now = datetime.datetime.now()
                print(f"sign_in__f---{now.strftime('%H:%M')}---Неверный пароль")
                print("---")
                return "2.2"
        else:
            db.close()
            now = datetime.datetime.now()
            print(f"sign_in__f---{now.strftime('%H:%M')}---Такого пользователя нет")
            print("---")
            return "2.1"
    except:
        db.close()
        now = datetime.datetime.now()
        print(f"sign_in__f---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return "0"


@eel.expose
def get__nickname(id):
    try:
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT nickname FROM user WHERE id = '{id}'")
        nickname = cursor.fetchall()
        nickname = str(nickname)[3: -5]
        db.close()
        now = datetime.datetime.now()
        print(f"get__nickname---{now.strftime('%H:%M')}---Успешно")
        print("---")
        return nickname
    except:
        db.close()
        now = datetime.datetime.now()
        print(f"get__nickname---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return "Noname"


@eel.expose
def f_email(email):
    try:
        if len(email) <= 126:
            return email
        else:
            part = []
            new_email = ""
            i1 = 0
            i2 = 126
            check = 0
            while check == 0:
                part.append(email[i1: i2])
                if len(email) - i2 <= 126:
                    part.append(email[i2:])
                    check = 1
                else:
                    i1 += 126
                    i2 += 126
            for a in range(len(part)):
                new_email += part[a] + "<wbr>"
            return new_email
    except:
        return email


@eel.expose
def change_pass(email):
    try:
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
        if len(cursor.fetchall()) != 0:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login('email', 'app_password_google')
            text = '''
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title></title>
                </head>
                <body>
                    <p>Для изменения пароля перейдите на сайт по ссылке ниже и введите новый пароль.</p>
                    <a href="https://dimlll.github.io/scsgop/">https://dimlll.github.io/scsgop/</a>
                </body>
                </html>
            '''
            msg = MIMEText(text, "html")
            msg["Subject"] = "Инструкция по изменению пароля в SCS:GOPanel"
            smtpObj.sendmail(f"email", {email}, msg.as_string())
            smtpObj.quit()
            db.close()
            now = datetime.datetime.now()
            print(f"change_pass---{now.strftime('%H:%M')}---Успешно")
            print("---")
            return 1
        else:
            db.close()
            now = datetime.datetime.now()
            print(f"change_pass---{now.strftime('%H:%M')}---Такого пользователя нет")
            print("---")
            return 2
    except:
        smtpObj.quit()
        db.close()
        now = datetime.datetime.now()
        print(f"change_pass---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return 0


@eel.expose
def new_password(password, email):
    try:
        if len(password) < 8:
            now = datetime.datetime.now()
            print(f"new_password---{now.strftime('%H:%M')}---Маленький пароль")
            print("---")
            return "2"
        salt = os.urandom(32)
        salt = b64encode(salt)
        key = hashlib.sha256(password.encode(
            'utf-8') + salt).hexdigest()
        salt = salt.decode('utf-8')
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(f"UPDATE user SET password = '{key}' WHERE email = '{email}'")
        db.commit()
        cursor.execute(f"UPDATE user SET salt = '{salt}' WHERE email = '{email}'")
        db.commit()
        db.close()
        now = datetime.datetime.now()
        print(f"new_password---{now.strftime('%H:%M')}---Успешно")
        print("---")
        return "1"
    except:
        db.close()
        now = datetime.datetime.now()
        print(f"new_password---{now.strftime('%H:%M')}---Ошибка")
        print("---")
        return 0  


eel.init("web")
eel.start("sign_up.html", size=(500, 800), geometry={'rec_pass.html': {
          'size': (500, 400)}, 'sign_in.html': {'size': (500, 800)}, 'main.html': {'size': (1300, 500)}, 'new_p.html': {'size': (500, 400)}})

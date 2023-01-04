import eel
import os
import hashlib
import pymysql

@eel.expose
def sign_up__f(email, nickname, password):
    db = pymysql.connect(host="127.0.0.1", port=3306,
                     user="mysql", passwd="mysql", database="scs:gop")
    cursor = db.cursor()
    print(db)
    cursor.execute(f"SELECT email FROM user WHERE email = '{email}'")
    if len(cursor.fetchall()) == 0:
        try:
            salt = os.urandom(32)
            key = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
            salt = salt.decode('latin1')
            cursor.execute(f"INSERT INTO user (nickname, email, password, salt) VALUES ('{nickname}', '{email}', '{key}', '{salt}')")
            db.commit()
            return "1"
        except:
            return "0"
    else:
        return "2"


eel.init("web")
eel.start("sign_up.html", size=(500, 800), geometry={'rec_pass.html': {
          'size': (500, 400)}, 'sign_in.html': {'size': (500, 800)}})

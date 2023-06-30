from apps import app
from flask import request
import sqlite3
from twilio.twiml.messaging_response import MessagingResponse
import os
from twilio.rest import Client


connection = sqlite3.connect('veritabani.db',check_same_thread=False)
cursor = connection.cursor()

def db_check_message(name, phone, message):
    sql = "SELECT * FROM kullanıcılar WHERE number = ?"
    cursor.execute(sql, (phone,)) # Numarayı arat
    results = cursor.fetchall() # Gelenleri fetchle

    # Sonuçları işle
    if len(results) > 0:
        for row in results:
            print("Adı: ", row[1])
            print("Numara: ", row[2])
            print("Eski Mesaj: ", row[3])
        print("Yeni Mesaj: ",message)
        update_sql = "UPDATE kullanıcılar SET message = ? WHERE number = ?"
        cursor.execute(update_sql, (message, phone))
        connection.commit()
    else:

        print("Numara bulunamadı.")
        insert_sql = "INSERT INTO kullanıcılar (name, number, message) VALUES (?, ?, ?)"
        cursor.execute(insert_sql, (name, phone, message))
        connection.commit()
        return send_message(name,phone)




@app.route("/msgpost",methods = ['POST'])
def get_message():
    userMsg = request.form.get('Body')
    userPhone = request.form.get('From', None)
    profileName = request.form.get('ProfileName', None)

    db_check_message(profileName, userPhone, userMsg)
    return "Status-200"

def send_message(name, number):
    account_sid = 'accounts-id'
    auth_token = 'auth-token-id'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hello {}!'.format(name),
        from_='whatsapp:YOUR-WHATSAPP-BOTS-NUM',
        to=number
    )

    print(message.sid)
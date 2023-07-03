from apps import app
from flask import request
from twilio.rest import Client
from datetime import datetime
import os
from apps.models import *


def db_check_message(name, phone, message):
    recipient = Recipient.get(phone_number=phone)
    if recipient:
        print("Numara bulundu.")
        print(f"Adi: {recipient.username}")
        print(f"Numara: {recipient.phone_number}")

        print("Gonderilen mesajlar\n")
        print("********************************\n")

        for message in recipient.messages:
            print(f"Mesaj: {message.text}")
            print(f"Gonderilme tarihi: {message.sent_at}")
            print(f"------------------------------\n")

        print("********************************\n")
        print(f"Yeni mesaj: {message}")

    else:
        print("Numara bulunamadi. Yeni alici database'e ekleniyor...")
        recipient = Recipient(username=name, phone_number=phone)
        print("Yeni numara basariyla eklendi.")

    new_message = Message(text=message, sent_at=datetime.now(), recipient=recipient)
    return send_message(new_message)


@app.route("/msgpost", methods=["POST"])
def get_message():
    data = request.get_json()

    to_name = data["to_name"]
    userPhone = data["to"]
    userMsg = data["message"]

    db_check_message(to_name, userPhone, userMsg)
    return "Status-200"


def send_message(message: Message):
    account_sid = "accounts-id"
    auth_token = "auth-token-id"

    print("Mesaj gonderiliyor...")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello {}!".format(message.recipient.username),
        from_="whatsapp:{}".format(os.getenv("PHONE_NUMBER")),
        to=message.recipient.phone_number,
    )

    print(message.sid)
    print("Mesaj gonderildi.")

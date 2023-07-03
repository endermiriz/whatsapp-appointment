from datetime import datetime
from pony.orm import *
from apps import db


class Message(db.Entity):
    id = PrimaryKey(int, auto=True)
    text = Required(str)
    sent_at = Required(datetime)
    recipient = Required("Recipient")


class Recipient(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    phone_number = Required(str, unique=True)
    messages = Set(Message)

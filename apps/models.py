from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    messages = Set("Message")
    phone_numbers = Set("PhoneNumber")


class Message(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    text = Required(str)


class PhoneNumber(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    is_active = Required(bool)
    number = Required(str)


db.generate_mapping()

from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    messages = Set('Message')
    phone_numbers = Set('PhoneNumber')


class Message(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    text = Optional(str)


class PhoneNumber(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required(User)
    is_active = Optional(bool)
    number = Required(str)



db.generate_mapping()
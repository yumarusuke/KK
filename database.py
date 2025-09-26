from peewee import *

db = SqliteDatabase('Fridge_chef.db')

class Person(Model):
    name = CharField()
    age = IntegerField()
    gender = CharField()
    mailaddress = CharField()
    password = IntegerField()
    password2 = IntegerField()
    allergie = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Family(Model):
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Shohin(Model):
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class store(Model):
    name = CharField()
    place = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Person])
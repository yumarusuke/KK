from peewee import *

db = SqliteDatabase('Fridge_chef.db')

class Person(Model):
    name = CharField()
    age = IntegerField()
    gender = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Person])
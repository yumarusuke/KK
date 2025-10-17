from peewee import *
from flask_login import UserMixin

db = SqliteDatabase('Fridge_chef.db')

class Person(Model):
    name = CharField()
    age = IntegerField()
    gender = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Family(UserMixin, Model):
    name = CharField()
    mailaddress = CharField()
    password = CharField()
    allergie = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Recipe(Model):
    name = CharField()
    photo = CharField()
    link = CharField()

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
db.create_tables([Family])
db.create_tables([Recipe])

# Recipe.create(name="さんま", photo="/static/秋刀魚.jpg", link="https://cookpad.com/jp/search/さんま")
# Recipe.create(name="メロン", photo="/static/メロン.jpg", link="https://cookpad.com/jp/search/メロン")
# Recipe.create(name="ソーセージ", photo="/static/ソーセージ.jpg", link="https://cookpad.com/jp/search/ソーセージ")

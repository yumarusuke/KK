from peewee import *
from flask_login import UserMixin
import datetime

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
class Vote(UserMixin, Model):
    name = CharField()
    what = CharField()
    when = DateField(default=datetime.datetime.now)
    class Meta:
        database = db # This model uses the "people.db" database.
class Recipe(Model):
    name = CharField()
    photo = CharField()
    link = CharField()
    grade = CharField()
    class Meta:
        database = db # This model uses the "people.db" database.

class Buy(Model):
    name = CharField()
    class Meta:
        database = db # This model uses the "people.db" database.

class Fridge(Model):
    name = CharField()
    category = CharField()
    date = DateField()
    expiration = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Shohin(Model):
    name = CharField()
    day = DateField()
    expiration = DateField()
    how = DateField()

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
db.create_tables([Fridge])
db.create_tables([Vote])
db.create_tables([Shohin])

# Recipe.create(name="さんま", photo="/static/秋刀魚.jpg", link="https://cookpad.com/jp/search/さんま")
# Recipe.create(name="メロン", photo="/static/メロン.jpg", link="https://cookpad.com/jp/search/メロン")
# Recipe.create(name="ソーセージ", photo="/static/ソーセージ.jpg", link="https://cookpad.com/jp/search/ソーセージ")

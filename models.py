from peewee import *
import urllib.request
import json


db = SqliteDatabase('Medigreen.db')


class Product(Model):
    name = TextField()
    # createdAt = DateTimeField()
    class Meta:
        database = db


class Price(Model):
    amount = TextField()
    price = FloatField()

    class Meta:
        database = db


class Dispensary(Model):
    name = TextField()
    _type = TextField()
    slug = TextField()
    state = TextField()
    city = TextField()
    wmid = IntegerField()
    license_type = TextField()


    class Meta:
        database = db


class ProductHasPrice(Model):
    productID = IntegerField()
    priceID = IntegerField()
    dispensaryID = IntegerField()
    date = DateTimeField()

    class Meta:
        database = db


class ProductHasCategory(Model):
    categoryID = IntegerField()
    category = TextField()
    productID = IntegerField()

    class Meta:
        database = db


class DispensaryHasProduct(Model):
    dispensaryID = IntegerField()
    productID = IntegerField()
    date = DateTimeField()

    class Meta:
        database = db


def initialize():
    db.connect()
    db.create_tables([Product, Price, ProductHasCategory, ProductHasPrice, Dispensary, DispensaryHasProduct], safe=True)



initialize()


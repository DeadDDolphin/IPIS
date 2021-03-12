from peewee import *

conn = MySQLDatabase.connect('Carsharing', host="localhost", user="root", passwd="")

class BaseModel(Model):
    class Meta:
        database = conn

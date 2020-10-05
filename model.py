import peewee
from peewee import *

db = peewee.SqliteDatabase('artstore.db')# creating data base
class Artist(peewee.Model):# creating Artist table
    name = CharField(unique=True)
    email = CharField(unique=True)
    
    class Meta:
        database = db
        constraints = [SQL('UNIQUE(name COLLATE NOCASE)')]
    
    def __str(self):
        return f'Artist ID:{self.id}, Name: {self.name}, Email: {self.email}'

class Artwork(peewee.Model):# creating Artwork table
    artist = ForeignKeyField(Artist, backref='artwork')
    name = CharField(unique = True)
    price = FloatField(9,2)
    is_available = BooleanField(default=True)

    class Meta:
        database =db
        constraints = [SQL('UNIQUE(name COLLATE NOCASE)')]
    def __str__(self):
        
        return f'{self.id} Artist: {self.artist}: {self.name} :{self.price} : {self.is_available}'
        




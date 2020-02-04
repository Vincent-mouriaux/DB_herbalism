from peewee import *

db = MySQLDatabase('herbalism',
                   user='Selene Mouriaux',
                   password='santoryu',
                   host='localhost')

class BaseModel(Model):
    class Meta:
        database = db

class SubClass(BaseModel):

    name = CharField(max_length=45)
    name_fr = CharField(max_length=45)

    class Meta:
        table_name = "underclass"

class Family(BaseModel):

    name = CharField(max_length=45)
    name_fr = CharField(max_length=45)
    underclass = ForeignKeyField(SubClass)

class Plant(BaseModel):

    name = CharField(max_length=45)
    indication = CharField(max_length=45)
    usedPart = CharField(column_name='used_part')
    price = DecimalField(5, 2)
    family = ForeignKeyField(Family)

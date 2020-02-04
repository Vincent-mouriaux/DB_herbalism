from models import *
from peewee import *

def avgPriceOfIndications():
    average_prices = Plant.select(Plant.indication, fn.AVG(
        Plant.price)).order_by(Plant.indication).group_by\
        (Plant.indication)
    return average_prices
from Task.celery import app
from .gspreadconf import gs
from .models import Product
from decimal import Decimal
from datetime import datetime


@app.task
def update_from_gsheets():
    def str_to_bool(value):
        return value.lower() in ("true", "yes", "t", "1")

    gs.login()
    sheet = gs.open("AmazProds").worksheet('Products')
    products = sheet.get_all_records()

    product = Product()
    for p in products:
        product.asin = p['ASIN']
        product.image = p['Image']
        product.rating = Decimal(str(p['Rating']).replace(',', '.'))
        product.price = Decimal(str(p['Price, $']).replace(',', '.'))
        product.title = p['Title']
        product.available = str_to_bool(p['Available'])
        product.amount = int(p['Amount'])
        product.weight = Decimal(str(p['Weight, lbs']).replace(',', '.'))
        product.length = Decimal(str(p['Length, mm']).replace(',', '.'))
        product.width = Decimal(str(p['Width, mm']).replace(',', '.'))
        product.height = Decimal(str(p['Height, mm']).replace(',', '.'))
        product.changed_date = datetime.strptime(str(p['Changed Date']), "%d.%m.%y").date()
        product.save()

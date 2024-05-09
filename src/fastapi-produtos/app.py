from fastapi import FastAPI
from models.products import Product

app = FastAPI()

@app.get('/')
def say():
    return {'Fast':'API'}

@app.get('/{name}')
def say_hi(name:str):
    if not name:
        pass
    return {'Hello':name}

data = [
    Product(id=1, name='Tenis Nike Air', description='Calçados', price=199.99),
    Product(id=2, name='Iphone', description='Celulares', price=3928.99),
    Product(id=3, name='Notebook', description='Eletrônicos', price=4928.97),
]

@app.get('/api/products')
def get_products():
    return data

from flask import Flask
from flask import request
from schema import ProductSchema
from decorators import authentication, rate_limit
from db import PRODUCTS
from functions import get, post

app = Flask(__name__)


@app.route('/v1/products/', methods=['GET', 'POST'])
@authentication
@rate_limit
def list_products_handle():
    if request.method == 'GET':
        return get(PRODUCTS)
    else:
        return post(PRODUCTS, request, ProductSchema())


if __name__ == '__main__':
    app.run()

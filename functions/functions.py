import json
from json import JSONDecodeError

from .helpers import search_, filter_, from_to_, fields_
from flask import jsonify


def get(products: list):
    try:
        products = search_(products)
        products = filter_(products)
        products = from_to_(products)
        products = fields_(products)
        return jsonify(products)
    except ValueError:
        products = jsonify({"msg": "parameter value error"})
        products.status_code = 400
        return products


def post(products: list, request, schema):
    try:
        raw_product = json.loads(request.data.decode('utf-8'))
    except JSONDecodeError as e:
        raw_product = jsonify({"msg": str(e)})
        raw_product.status_code = 400
        return raw_product

    clean_product, errors = schema.load(raw_product)
    if errors:
        response = jsonify(errors)
        response.status_code = 400
        return response

    products.append(clean_product)
    return jsonify(raw_product)

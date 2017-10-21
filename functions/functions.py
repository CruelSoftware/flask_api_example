import json
from json import JSONDecodeError

from .helpers import search_, filter_, from_to_, fields_, error_
from flask import jsonify


def get(products: list):
    try:
        products = search_(products)
        products = filter_(products)
        products = from_to_(products)
        products = fields_(products)
        return jsonify(products)
    except ValueError:
        return error_("parameter value error", 400)


def post(products: list, request, schema):
    try:
        raw_product = json.loads(request.data.decode('utf-8'))
    except JSONDecodeError as e:
        return error_(str(e), 400)

    clean_product, errors = schema.load(raw_product)
    if errors:
        return error_(errors, 400)

    products.append(clean_product)
    return jsonify(raw_product)

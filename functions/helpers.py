from flask import request
from flask import jsonify

def search_(products):
    query = request.args.get('q')
    if query:
        products = [p for p in products if query.lower() in p['title'].lower()]
    return products


def filter_(products):
    filter_field = request.args.get('filter')
    if filter_field:
        products = [p for p in products if p.get(filter_field)]
    return products


def from_to_(products):
    from_element = request.args.get('from')
    to_element = request.args.get('to')
    if from_element and to_element:
        from_element = int(from_element)
        to_element = int(to_element)
        products = products[from_element:to_element]
    return products


def fields_(products):
    fields = request.args.get('fields')
    if fields:
        fields = fields.split(',')
        products = [{k: v for k, v in p.items() if k in fields}
                    for p in products]
    return products

def error_(msg, status):
    data = jsonify({"message":msg})
    data.response_status = status
    return data
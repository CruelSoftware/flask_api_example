from functools import wraps
from flask import request
from flask import jsonify

from db import API_KEYS


def authentication(func):
    @wraps(func)
    def wrapped():
        api_key = request.headers.get('HTTP-X-API-KEY')
        if api_key not in API_KEYS:
            response = jsonify({'error': 'Wrong API key'})
            response.status_code = 400
            return response
        else:
            return func()

    return wrapped


def rate_limit(func):
    RATE_LIMITS_INFO = {}
    MAX_REQUESTS_PER_USER = 100

    @wraps(func)
    def wrapped():
        api_key = request.headers.get('HTTP-X-API-KEY')
        RATE_LIMITS_INFO[api_key] = RATE_LIMITS_INFO.get(api_key, 0) + 1
        if RATE_LIMITS_INFO[api_key] > MAX_REQUESTS_PER_USER:
            response = jsonify({'error': 'Rate limit exceeded'})
            response.status_code = 400
            return response
        else:
            return func()

    return wrapped

### flask_api_example
Simple flask api without database

##### 1 endpoint /v1/products/

##### 2 methods ['GET', 'POST']

GET to retrieve data

##### parameters:
    search - return items, contains this search string
    filter - return items which filtered field is not None/False
    fields - return only those item fields
    from, to - return slice

POST to create data

#### parameters:
    schema/marshmallow.py

You will need api-key, which you may define in data.py

You may define PRODUCTS in data.py

You may define parameters in schema/marshmallow.py

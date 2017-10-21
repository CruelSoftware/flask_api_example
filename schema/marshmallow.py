from marshmallow import Schema, fields

class ProductSchema(Schema):
    title = fields.Str(required=True)
    price_rub = fields.Integer(required=True)
    product_image = fields.Str(required=False)
    in_store = fields.Boolean(default=False)
from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(required=True)
    user = fields.Str(required=True, validate=validate.Length(min=2))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=6))

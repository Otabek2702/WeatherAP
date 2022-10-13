from flask_marshmallow import Marshmallow
from .models import User

ma = Marshmallow()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


user_schema = UserSchema()

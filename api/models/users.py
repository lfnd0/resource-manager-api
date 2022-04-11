import datetime

from api import database, marshmallow


class Users(database.Model):
    id = database.Column(
        database.Integer, primary_key=True, autoincrement=True)
    username = database.Column(
        database.String(32), unique=True, nullable=False)
    password = database.Column(database.String(128), nullable=False)
    is_admin = database.Column(database.Boolean, default=False)
    created_at = database.Column(
        database.DateTime, default=datetime.datetime.now())
    updated_at = database.Column(
        database.DateTime, default=datetime.datetime.now())
    allocations = database.relationship("Allocations", cascade="all, delete")

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UsersSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'username', 'password',
                  'is_admin', 'created_at', 'updated_at')


user_schema = UsersSchema()

import datetime

from api import database, marshmallow


class Resources(database.Model):
    id = database.Column(
        database.Integer, primary_key=True, autoincrement=True)
    owner_id = database.Column(
        database.Integer, database.ForeignKey('users.id'), nullable=False)
    name = database.Column(
        database.String(32), nullable=False)
    is_available = database.Column(database.Boolean, default=True)
    created_at = database.Column(
        database.DateTime, default=datetime.datetime.now())
    updated_at = database.Column(
        database.DateTime, default=datetime.datetime.now())

    def __init__(self, name, owner_id):
        self.name = name
        self.owner_id = owner_id


class ResourcesSchema(marshmallow.Schema):
    class Meta:
        fields = ['id', 'name',
                  'is_available', 'created_at', 'update_at']


resource_schema = ResourcesSchema()
resources_schema = ResourcesSchema(many=True)

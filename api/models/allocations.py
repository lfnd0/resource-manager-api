import datetime

from api import database, marshmallow


class Allocations(database.Model):
    id = database.Column(
        database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(
        database.Integer, database.ForeignKey('users.id'), nullable=False)
    resource_id = database.Column(
        database.Integer, database.ForeignKey('resources.id'), nullable=False)
    start_date = database.Column(
        database.DateTime, default=datetime.datetime.now())
    end_date = database.Column(
        database.DateTime, default=None, nullable=True)

    def __init__(self, user_id, resource_id):
        self.user_id = user_id
        self.resource_id = resource_id


class AllocationsSchema(marshmallow.Schema):
    class Meta:
        fields = ['id', 'user_id', 'resource_id', 'start_date', 'end_date']


allocation_schema = AllocationsSchema()

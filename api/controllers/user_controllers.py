import datetime

from flask import request, jsonify
from werkzeug.security import generate_password_hash

from api import database

from ..models.allocations import Allocations, allocation_schema
from ..models.resources import Resources, resources_schema
from ..models.users import Users, user_schema


def create_user():
    username = request.json['username']
    password = request.json['password']

    user = Users.query.filter(Users.username == username).first()

    if (user):
        return jsonify({'error': 'User already exists'}), 422

    password_hash = generate_password_hash(password)

    user = Users(username, password_hash)
    database.session.add(user)
    database.session.commit()

    data = user_schema.dump(user)

    return jsonify(data), 201


def read_user(id):
    user = Users.query.get(id)

    if(not user):
        return jsonify({'error': 'User not found'}), 404

    data = user_schema.dump(user)

    return jsonify(data), 200


def update_user(id):
    username = request.json['username']

    user = Users.query.get(id)
    if (not user):
        return jsonify({'error': 'User not found'}), 404

    user.username = username
    user.updated_at = datetime.datetime.now()

    database.session.commit()

    data = user_schema.dump(user)

    return jsonify(data), 200


def delete_user(id):
    user = Users.query.get(id)

    if (not user):
        return jsonify({'error': 'User not found'}), 404

    if(user.is_admin):
        return jsonify({'error': 'Not authorized'}), 401

    database.session.delete(user)
    database.session.commit()

    data = user_schema.dump(user)

    return jsonify(data), 200


def read_resources_available():
    resources = Resources.query.filter(Resources.is_available == True)

    data = resources_schema.dump(resources)

    return jsonify(data), 200


def create_allocation():
    user_id = request.headers['user_id']
    resource_id = request.headers['resource_id']

    user = Users.query.get(user_id)
    if(not user):
        return jsonify({'error': 'User not found'}), 404

    resource = Resources.query.get(resource_id)
    if(not resource):
        return jsonify({'error': 'Resource not found'}), 404

    if(resource.is_available == False):
        return jsonify({'error': 'Resource unavailable'}), 422

    allocation = Allocations(user_id, resource_id)

    resource.is_available = False
    resource.updated_at = datetime.datetime.now()

    database.session.add(allocation)
    database.session.commit()

    data = allocation_schema.dump(allocation)

    return jsonify(data), 201


def update_allocation(id):
    user_id = request.headers['user_id']
    resource_id = request.headers['resource_id']

    allocation = Allocations.query.get(id)
    if(not allocation):
        return jsonify({'error': 'Allocation not found'}), 404

    if((allocation.end_date != None) or (allocation.user_id != int(user_id)) or (allocation.resource_id != int(resource_id))):
        return jsonify({'error': 'Not authorized'}), 401

    allocation.end_date = datetime.datetime.now()

    resource = Resources.query.get(resource_id)
    resource.is_available = True
    resource.updated_at = datetime.datetime.now()

    database.session.commit()

    data = allocation_schema.dump(allocation)

    return jsonify(data), 200

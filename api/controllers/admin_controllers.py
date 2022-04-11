import datetime

from flask import jsonify, request
from werkzeug.security import generate_password_hash

from api import database

from ..models.users import Users, user_schema
from ..models.resources import Resources, resource_schema, resources_schema


def create_admin():
    username = 'admin'
    password = 'admin'

    admin = Users.query.filter(Users.username == username).first()
    if(admin):
        return jsonify({'error': 'Admin already exists'}), 422

    password_hash = generate_password_hash(password)

    admin = Users(username, password_hash)
    database.session.add(admin)
    admin.is_admin = True
    database.session.commit()

    data = user_schema.dump(admin)

    return jsonify(data), 200


def create_resource():
    name = request.json['name']
    owner_id = request.headers['owner_id']

    try:
        admin = Users.query.get(owner_id)
        if(not admin.is_admin):
            return jsonify({'error': 'Not authorized'}), 401

        resource = Resources(name, owner_id)
        database.session.add(resource)
        database.session.commit()

        data = resource_schema.dump(resource)

        return jsonify(data), 201
    except:
        return jsonify({'error': 'Internal API error'}), 500


def read_resources():
    owner_id = request.headers['owner_id']

    try:
        admin = Users.query.get(owner_id)
        if(not admin.is_admin):
            return jsonify({'error': 'Not authorized'}), 401

        resources = Resources.query.all()

        data = resources_schema.dump(resources)

        return jsonify(data), 200
    except:
        return jsonify({'error': 'Internal API error'}), 500


def update_resource(id):
    owner_id = request.headers['owner_id']

    try:
        admin = Users.query.get(owner_id)
        if(not admin.is_admin):
            return jsonify({'error': 'Not authorized'}), 401

        resource = Resources.query.get(id)
        if(not resource):
            return jsonify({'error': 'Resource not found'}), 404

        if(resource.is_available):
            resource.is_available = False
        else:
            resource.is_available = True

        resource.update_at = datetime.datetime.now()
    except:
        return jsonify({'error': 'Internal API error'}), 500

    database.session.commit()

    data = resource_schema.dump(resource)

    return jsonify(data), 200


def delete_resource(id):
    owner_id = request.headers['owner_id']

    try:
        admin = Users.query.get(owner_id)
        if(not admin.is_admin):
            return jsonify({'error': 'Not authorized'}), 401

        resource = Resources.query.get(id)
        if(not resource):
            return jsonify({'error': 'Resource not found'}), 404

        database.session.delete(resource)
        database.session.commit()

        data = resource_schema.dump(resource)

        return jsonify(data), 200
    except:
        return jsonify({'error': 'Internal API error'}), 500

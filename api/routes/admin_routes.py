from crypt import methods
from api import app

from ..controllers import admin_controllers
from ..controllers import user_controllers


@app.route('/api/admin', methods=['GET'])
def create_admin():
    return admin_controllers.create_admin()


@app.route('/api/admin/resources', methods=['POST'])
def create_resource():
    return admin_controllers.create_resource()

@app.route('/api/admin/resources', methods=['GET'])
def read_resources():
    return admin_controllers.read_resources()

@app.route('/api/admin/resources/<int:id>', methods=['PUT'])
def update_resource(id):
    return admin_controllers.update_resource(id)


@app.route('/api/admin/resources/<int:id>', methods=['DELETE'])
def delete_resource(id):
    return admin_controllers.delete_resource(id)


@app.route('/api/admin/users/<int:id>', methods=['DELETE'])
def delete_user_by_admin(id):
    return user_controllers.delete_user(id)

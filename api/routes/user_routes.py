from api import app

from ..controllers import user_controllers


@app.route('/api/users', methods=['POST'])
def create_user():
    return user_controllers.create_user()


@app.route('/api/users/<int:id>', methods=['GET'])
def read_user(id):
    return user_controllers.read_user(id)


@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    return user_controllers.update_user(id)


@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return user_controllers.delete_user(id)


@app.route('/api/users/resources', methods=['GET'])
def read_resources_available():
    return user_controllers.read_resources_available()


@app.route('/api/users/allocations', methods=['POST'])
def create_allocation():
    return user_controllers.create_allocation()


@app.route('/api/users/allocations/<int:id>', methods=['PUT'])
def update_allocation(id):
    return user_controllers.update_allocation(id)

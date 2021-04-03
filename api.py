from users import *

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'Users': User.get_all_users()})

@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()  
    User.add_user(request_data["uid"], request_data["name"], request_data["mobile"],
                    request_data["age"])
    response = Response("User added", 201, mimetype='application/json')
    return response

@app.route('/users/uid/<int:uid>', methods=['GET'])
def get_user_by_uid(uid):
    return_value = User.get_user_uid(uid)
    return jsonify(return_value)

@app.route('/users/age/<int:age>', methods=['GET'])
def get_user_by_age(age):
    return_value = User.get_user_age(age)
    return jsonify(return_value)

@app.route('/users/mobile/<int:mobile>', methods=['GET'])
def get_user_by_mobile(mobile):
    return_value = User.get_user_mobile(mobile)
    return jsonify(return_value)

@app.route('/users/name/<string:name>', methods=['GET'])
def get_user_by_name(name):
    return_value = User.get_user_name(name)
    #return (return_value)
    return jsonify(return_value[1])


if __name__ == "__main__":
    app.run(port=5000, debug=True)

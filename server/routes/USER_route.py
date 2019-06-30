from flask import Flask, jsonify, request, Blueprint
from pony.orm.serialization import to_dict
from model import USER

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods = ['POST'])
def user_post():
    data = request.get_json()
    res = USER.user_insert(data)
    return jsonify(res)

@user_api.route('/user', methods = ['GET'])
def user_get_all():
    res = USER.user_select_all()
    return  jsonify(res)

@user_api.route('/user', methods = ['PUT'])
def user_put():
    data = request.get_json()
    res = USER.user_update(data)
    return jsonify(res)

@user_api.route('/user/pass', methods = ['PUT'])
def user_pass_put():
    data = request.get_json()
    res = USER.user_update_password(data)
    return jsonify(res)

@user_api.route('/user/<id_user>', methods = ['GET'])
def user_get(id_user):
    user_id = str(id_user)
    res = USER.user_select(user_id).to_dict()
    return  jsonify(res)

@user_api.route('/user/<id_user>', methods = ['DELETE'])
def user_del(id_user):
    user_id = str(id_user)
    res = USER.user_delete(user_id)
    return res

@user_api.route('/user/<mail>/<password>', methods = ['GET'])
def login_user(mail, password):
    mail = str(mail)
    pas = str(password)
    res = USER.user_login(mail, pas)
    return jsonify(res)
from flask import Flask, jsonify, request, Blueprint
from pony.orm.serialization import to_dict
from model import USER

user_api = Blueprint('user_api', __name__)

@user_api.route('/user', methods = ['PUT'])
def user_put():
    data = request.get_json()
    res = USER.user_insert(data)
    return jsonify(res)

@user_api.route('/user', methods = ['GET'])
def user_get_all():
    res = USER.user_select_all()
    return  jsonify(res)

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
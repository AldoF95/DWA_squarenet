from flask import Flask, jsonify, request, Blueprint
from pony.orm.serialization import to_dict
from model import LOGIN

login_api = Blueprint('login_api', __name__)

@login_api.route('/login', methods = ['PUT'])
def login_put():
    data = request.get_json()
    res = LOGIN.login_insert(data)
    return jsonify(res)

@login_api.route('/login', methods = ['GET'])
def login_get_all():
    res = LOGIN.login_select_all()
    return  jsonify(res)

@login_api.route('/login/<id_log>', methods = ['GET'])
def login_get(id_log):
    log_id = str(id_log)
    res = LOGIN.login_select(log_id).to_dict()
    return  jsonify(res)

@login_api.route('/login/<login_id>', methods = ['DELETE'])
def login_del(login_id):
    log_id = str(login_id)
    res = LOGIN.login_delete(log_id)
    return res
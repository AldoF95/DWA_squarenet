from flask import Flask, jsonify, request, Blueprint
from pony.orm.serialization import to_dict
from model import PROFILE

profile_api = Blueprint('profile_api', __name__)

@profile_api.route('/profile', methods = ['POST'])
def profile_post():
    data = request.get_json()
    res = PROFILE.profile_insert(data)
    return jsonify(res)

@profile_api.route('/profile', methods = ['PUT'])
def profile_put():
    data = request.get_json()
    res = PROFILE.profile_update(data)
    return jsonify(res)

@profile_api.route('/profile', methods = ['GET'])
def profile_get_all():
    res = PROFILE.profile_select_all()
    return jsonify(res)

@profile_api.route('/profile/<profile_id>', methods = ['GET'])
def profile_get(profile_id):
    id_profile = str(profile_id)
    res = PROFILE.profile_select(id_profile).to_dict()
    return jsonify(res)

@profile_api.route('/user/profile/<user_id>', methods = ['GET'])
def user_profile_get(user_id):
    user_id = str(user_id)
    res = PROFILE.user_profile(user_id)
    return jsonify(res)

@profile_api.route('/profile/<profile_id>', methods = ['DELETE'])
def profile_del(profile_id):
    id_profile = str(profile_id)
    res = PROFILE.profile_delete(id_profile)
    return res
from flask import Flask, jsonify, request, Blueprint, Response
from pony.orm import *
from pony.orm.serialization import to_dict
import json
from model import POSTS, PROFILE

post_api = Blueprint('post_api', __name__)

@post_api.route('/posts', methods = ['POST'])
def post_post():
    data = request.get_json()
    res = POSTS.posts_insert(data)
    return jsonify(res)

@post_api.route('/posts', methods = ['PUT'])
def post_update_users():
    data = request.get_json()
    res = POSTS.post_apply_user_update(data)
    return jsonify(res)

@post_api.route('/posts', methods = ['GET'])
def post_get_all():
    res = POSTS.post_select_all()
    return jsonify(res)

@post_api.route('/posts/<id_post>', methods = ['GET'])
def post_get(id_post):
    post_id = str(id_post)
    res = POSTS.post_select(post_id)
    return jsonify(res)

@post_api.route('/posts/<id_post>', methods = ['DELETE'])
def post_del(id_post):
    post_id = str(id_post)
    res = POSTS.post_delete(post_id)
    return res

@post_api.route('/homepage/<user_id>', methods = ['GET'])
def homepage_posts_get(user_id):
    id_user = str(user_id)
    prof = PROFILE.check_user(id_user).to_dict() #returns profile if exists
    if(prof is not None):
        tags_list = prof['tags']
        posts = POSTS.homepage_posts(tags_list)
        return jsonify(posts)

    return Response(404)

@post_api.route('/profile_posts/<user_id>', methods = ['GET'])
def profile_post(user_id):
    id_user = str(user_id)
    posts = POSTS.profile_posts(id_user)
    return jsonify(posts)
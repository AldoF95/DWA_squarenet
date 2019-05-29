from flask import Flask, jsonify, request, Blueprint
from pony.orm.serialization import to_dict
from model import TAGS

tags_api = Blueprint('tags_api', __name__)

@tags_api.route('/tags', methods = ['PUT'])
def tags_put():
    data = request.get_json()
    res = TAGS.tags_insert(data)
    return jsonify(res)

@tags_api.route('/tags', methods = ['GET'])
def tags_get_all():
    res = TAGS.tags_select_all()
    return  jsonify(res)

@tags_api.route('/tags/<tag_id>', methods = ['GET'])
def tags_get(tag_id):
    id_tag = str(tag_id)
    res = TAGS.tags_select(id_tag).to_dict()
    return  jsonify(res)

@tags_api.route('/tags/<tag_id>', methods = ['DELETE'])
def tags_del(tag_id):
    id_tag = str(tag_id)
    res = TAGS.tags_delete(id_tag)
    return  res



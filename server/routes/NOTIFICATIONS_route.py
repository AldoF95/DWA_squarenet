from flask import Flask, jsonify, request, Blueprint
from pony.orm.serialization import to_dict
from model import NOTIFICATIONS

notification_api = Blueprint('notification_api', __name__)

@notification_api.route('/notification', methods = ['PUT'])
def notification_put():
    data = request.get_json()
    res = NOTIFICATIONS.notification_insert(data)
    return jsonify(res)


@notification_api.route('/notification', methods = ['GET'])
def notification_get_all():
    res = NOTIFICATIONS.notification_select_all()
    return jsonify(res)

@notification_api.route('/notification/<id_notif>', methods = ['get'])
def notification_get(id_notif):
    notif_id = str(id_notif)
    res = NOTIFICATIONS.notification_select(notif_id)
    return jsonify(res)

@notification_api.route('/notification/<id_notif>', methods = ['DELETE'])
def notification_delete(id_notif):
    notif_id = str(id_notif)
    res = NOTIFICATIONS.notification_delete(notif_id)
    return res
   
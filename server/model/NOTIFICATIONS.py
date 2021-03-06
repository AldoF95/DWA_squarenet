from pony.orm import *
from model import db_conn, USER, POSTS
import datetime, time
import uuid

class Notifications(db_conn.db.Entity):
        _table_ = "NOTIFICATIONS"
        id = PrimaryKey(str)
        time_created = Required(datetime.datetime)
        notification_type = Required(str)
        from_user = Required(Json, default = [])
        to_user = Required(USER.User)
        posts = Required(POSTS.Posts)

@db_session
def notification_insert(data):
        id_gen = str(uuid.uuid4())
        data['time_created'] = datetime.datetime.now()
        t_user = USER.user_select(data['to_user'])
        post = POSTS.post_select(data['post'])
        notification = Notifications( id = id_gen,
                                        time_created = data['time_created'],
                                        notification_type = data['notification_type'],
                                        from_user = data['from_user'],
                                        to_user = t_user,
                                        posts = post)
        commit()
        return notification.to_dict()

@db_session
def notification_select_all():
        #notif = db_conn.db.select('select * from "NOTIFICATIONS"')
        notif = select(u for u in Notifications)[:]
        notif = {'data' : [u.to_dict() for u in notif]}
        return notif

@db_session
def notification_select(notif_id):
        notif = Notifications.get(id=notif_id)
        return notif

@db_session
def notification_select_user(user_id):
        notif = select(u for u in Notifications if str(u.to_user) == str(user_id))[:]
        notif = {'data' : [u.to_dict() for u in notif]}
        return notif

@db_session
def notification_update(data):
        Notifications[data['id_notify']].notification_type = data['type']
        return 'Notification updated'


@db_session
def notification_delete(notif_id):
        Notifications[notif_id].delete()
        return 'notification deleted'

@db_session
def notification_delete_all():
        delete(u for u in Notifications)
        return 'all notifications deleted'

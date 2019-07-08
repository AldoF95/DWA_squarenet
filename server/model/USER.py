from pony.orm import *
from pony.orm.serialization import to_dict
import base64
from model import db_conn
import uuid

class User(db_conn.db.Entity):
        _table_ = "USERS"
        id = PrimaryKey(str)
        name = Required(str)
        email = Required(str)
        password = Required(str)
        login = Set('Login')
        profile = Set('Profile')
        posts = Set('Posts')
        #notifications_from = Set('Notifications', reverse = 'from_user')
        notifications_to = Set('Notifications', reverse = 'to_user')


@db_session
def user_insert(data):
        id_gen = str(uuid.uuid4())
        ch_mail = check_email(data['email'])
        if(ch_mail is not None):
                return "Email already exists"
        password_enc = str(base64.b64encode(bytes(data['password'], encoding='utf8')))
        user = User(id = id_gen,
                    name=data["name"], 
                    email = data["email"], 
                    password = password_enc)
        commit()
        return user.to_dict()
        
@db_session
def user_update_password(data):
        p = str(base64.b64encode(bytes(data['password'], encoding='utf8')))
        User[data['id']].password = p
        return 'Password updated'
        
@db_session
def user_update(data):
        User[data['id']].name = data['name']
        return 'Name updated'

@db_session
def check_email(ch_mail):
        user_email = User.get(email = ch_mail)
        return user_email

@db_session
def user_login(mail, pas):
        user = User.get(email = mail)
        pas = str(base64.b64encode(bytes(pas, encoding='utf8')))
        if user:
                user = user.to_dict()
                if user['password']==pas:
                        return user
                else:
                        return 'wrong password'
        else:
                return 'User not found'

@db_session
def user_select_all():
        #user = db_conn.db.select('select * from "USERS"') return list od data, not json format
        user = select(u for u in User)[:]
        user = {'data' : [u.to_dict() for u in user]}
        return user

@db_session
def user_select(id_user):
        user = User.get(id=id_user)
        return user

@db_session
def user_delete(id_user):
        User[id_user].delete()
        return "User deleted"



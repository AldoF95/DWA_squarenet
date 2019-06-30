from pony.orm import *
from model import db_conn
from model import USER
import datetime, time
import uuid, json

class Login(db_conn.db.Entity):
        _table_ = "LOGIN"
        id = PrimaryKey(str)
        time = Required(datetime.datetime)
        first_login = Required(bool, default = False)
        user = Required(USER.User)

@db_session
def login_insert(data):
        id_gen = str(uuid.uuid4())
        user = USER.user_select(data['user_id'])
        data['time'] = datetime.datetime.now()
        login = Login(  id = id_gen,
                        time = data['time'],
                        #first_login = bool(data['first_login']),
                        user = user)
        commit()
        return login.to_dict()

@db_session
def login_select_all():
        #login = db_conn.db.select('select * from "LOGIN"')
        login = select(u for u in Login)[:]
        login = {'data' : [u.to_dict() for u in login]}
        return login


@db_session
def login_select(id_login):
        log = Login.get(id=id_login)
        return log

@db_session
def login_delete(login_id):
        Login[login_id].delete()
        return "Login deleted"


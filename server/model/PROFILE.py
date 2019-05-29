from pony.orm import *
from pony.orm.serialization import to_dict
from model import db_conn, USER, TAGS
import uuid

class Profile(db_conn.db.Entity):
        _table_ = "PROFILE"
        id = PrimaryKey(str)
        user = Required(USER.User)
        gender = Required(str)
        age = Required(int)
        description = Required(str)
        tags = Required(Json)

@db_session
def profile_insert(data):
        id_gen = str(uuid.uuid4())
        if(check_user(data['user_id'])is not None):
                return 'Profile already exists'
        user = USER.user_select(data['user_id'])
        profile = Profile(
                id = id_gen,
                user = user,
                gender = data['gender'],
                age = data['age'],
                description = data['description'],
                tags = data['tags']
        )
        commit()
        return profile.to_dict()

@db_session
def check_user(ch_user):
        user_id = Profile.get(user = ch_user)
        return user_id

@db_session
def profile_select_all():
        #profile = db_conn.db.select('select * from "PROFILE"')
        profile = select(u for u in Profile)[:]
        profile = {'data' : [u.to_dict() for u in profile]}
        return profile

@db_session
def profile_select(profile_id):
        profile = Profile.get(id=profile_id)
        return profile

@db_session
def profile_delete(profile_id):
        Profile[profile_id].delete()
        return 'Profile deleted'

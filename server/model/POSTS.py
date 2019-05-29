from pony.orm import *
from model import db_conn, USER, TAGS
import datetime, time
import uuid

class Posts(db_conn.db.Entity):
        _table_ = "POSTS"
        id = PrimaryKey(str)
        title = Required(str)
        body = Required(str)
        time_posted = Required(datetime.datetime)
        user = Required(USER.User)
        need_users = Required(int)
        due_time = Required(datetime.datetime)
        location = Required(str)
        apply_users = Optional(Json)
        tags = Required(TAGS.Tags)
        notifications = Set('Notifications')

@db_session
def posts_insert(data):
        id_gen = str(uuid.uuid4())
        data['time_posted'] = datetime.datetime.now()
        user = USER.user_select(data['user_id'])
        tags = TAGS.tags_select(data['tag_id'])
        post = Posts(   id = id_gen,
                        title = data['title'],
                        body = data['body'],
                        time_posted = data['time_posted'],
                        user = user,
                        need_users = data['need_users'],
                        due_time = data['due_time'],
                        location = data['location'],
                        apply_users = data['apply_user'],
                        tags = tags)
        commit()
        return post.to_dict()

@db_session
def post_select_all():
        #post = db_conn.db.select('select * from "POSTS"')
        post = select(u for u in Posts)[:]
        post = {'data' : [u.to_dict() for u in post]}
        return post

@db_session
def post_select(post_id):
        post = Posts.get(id=post_id)
        return post

@db_session
def post_delete(post_id):
        Posts[post_id].delete()
        return 'post deleted'

@db_session
def homepage_posts(users_tags):
        print(users_tags)
        tags_id = []
        posts_show = []
        for tag in users_tags:
                t = TAGS.Tags.get(name=tag)
                if(t is not None):
                        t = t.to_dict()
                        tags_id.append(t['id'])
        for tag_id in tags_id:
                posts = select(u for u in Posts if u.tags.id == tag_id)[:]
                print(posts)
                if(posts != []):
                        posts = {'data' : [u.to_dict() for u in posts]}
                        posts_show.append(posts['data'])
        
        return posts_show

@db_session
def profile_posts(user_id):
        post = select(u for u in Posts if u.user.id == user_id)[:]
        if (post != []):
                post = {'data': [u.to_dict() for u in post]}
                return post
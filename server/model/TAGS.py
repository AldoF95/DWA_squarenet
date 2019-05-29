from pony.orm import *
from model import db_conn
import uuid

class Tags(db_conn.db.Entity):
        _table_ = "TAGS"
        id = PrimaryKey(str)
        name = Required(str)
        number_users = Required(int, default = 0)
        posts = Set('Posts')

@db_session
def tags_insert(data):
        id_gen = str(uuid.uuid4())
        if(check_name(data['name']) is not None):
                return 'Tag already exists'
        tag = Tags(  id = id_gen,
                     name = data['name'])
        commit()
        #return 'tag added'
        return tag.to_dict()

@db_session
def check_name(ch_name):
        tag_name = Tags.get(name = ch_name)
        return tag_name

@db_session
def tags_select_all():
        #tags = db_conn.db.select('select * from "TAGS"')
        tags = select(u for u in Tags)[:]
        tags = {'data' : [u.to_dict() for u in tags]}
        return tags

@db_session
def tags_select(id_tags):
        tag = Tags.get(id=id_tags)
        return tag

@db_session
def tags_delete(id_tags):
        Tags[id_tags].delete()
        return "Tag deleted"
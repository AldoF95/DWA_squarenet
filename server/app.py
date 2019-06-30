from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from model import LOGIN, USER, TAGS, PROFILE, POSTS, NOTIFICATIONS
from model import db_conn
from routes import USER_route, LOGIN_route, TAGS_route, PROFILE_route, POSTS_route, NOTIFICATIONS_route

app = Flask(__name__)
CORS(app)

app.register_blueprint(USER_route.user_api)
app.register_blueprint(LOGIN_route.login_api)
app.register_blueprint(TAGS_route.tags_api)
app.register_blueprint(PROFILE_route.profile_api)
app.register_blueprint(POSTS_route.post_api)
app.register_blueprint(NOTIFICATIONS_route.notification_api)

db_conn.db.generate_mapping(create_tables=True)

@app.route('/')
def index():
    return Response(200)



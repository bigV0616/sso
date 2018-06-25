# coding: utf-8

import json
from base64 import b64encode
import python_jwt
import random
from flask import Flask, request, redirect, session, render_template, make_response
from libs.token import checkCookieToken, getCookieInfo
import conf
from libs.oldap import checkUserPwd

token_list = {}
login_user = {}
def create_app(object_name):
    '''
    sso逻辑不多，就在搞一层了
    :param object_name:
    :return:
    '''
    app = Flask(__name__)
    app.config.from_object(object_name)
    app.secret_key = app.config.get("SECRET_KEY")

    @app.route("/get_user")
    def get_user():
        sid = checkCookieToken(request, token_list)
        if sid:
            user = login_user.get(sid, None)
            if user:
                return json.dumps(user)
        return "no user"

    @app.route("/login")
    def login_first():
        return render_template("login.html")

    @app.route("/do_login", methods=["POST"])
    def login():
        username = request.form.get("username")
        password = request.form.get("password")
        next_url = request.form.get("next_url")
        if username and password:
            # 去OpenLdap中校验用户名密码
            if username == "test" and password == "test":
                # 生成token
                seeds = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
                token = ''
                for i in range(24):
                    token += random.choice(seeds)
                user_token = b64encode(token)
                cookie_token = python_jwt.json_encode({'user_token': user_token})

                sid = session.get('id', username)
                session['id'] = sid
                token_list[cookie_token] = sid
                login_user[sid] = {'username': username}
                resp = make_response(next_url)
                resp.set_cookie('cookie_token', cookie_token)
                return resp

        resp = make_response("login failed", 400)
        return "no user"

    @app.route("/logout")
    def logout():
        sid = checkCookieToken(request, token_list)
        if sid:
            login_user[sid] = None
            return "GoodBye Human"
        return "logout failed"

    @app.route("/test")
    def test():
        return "sucess"

    return app



if __name__ == "__main__":
    # APP_DEV_PORT = 8902
    app = create_app("conf.app.DevConfig")
    APP_DEV_PORT = app.config.get("APP_DEV_PORT")
    app.run(host='0.0.0.0', port=APP_DEV_PORT, debug=app.config["DEBUG"])









#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,request,make_response,redirect,render_template
from base64 import b64encode
import os
import python_jwt
import requests
import random
app = Flask(__name__)

app_name='app-1'

sso_server = 'http://127.0.0.1:8888'

@app.before_request
def hello_world():
    '''
    1. 查看请求cookie中是否存在用户cookie
    2. 校验是否存在真实用户
    3. 不存在用户cookie， 则去sso登录
    注： cookie sid存储在mem中，重启丢失，如果有需求可以吧cookie 存储到db
    :return:
    '''
    cookie_token = request.cookies.get("cookie_token", None)
    if cookie_token:
        headers = {'Authorization': cookie_token}
        try:
            r = requests.get(sso_server+'/get_user', headers=headers, timeout=60)
            if r.status_code == requests.codes.ok:
                if r.text != 'no user':
                    return
        except Exception as e:
            print e
    return redirect(sso_server + '/login?next_url=' + request.url)

@app.route("/test/sso")
def test():
    return "sucess"

@app.route("/")
def  welcome():
    return "hello world"

@app.route('/logout')
def logout():
    # 尝试获取token
    cookie_token = request.cookies.get('cookie_token', None)
    if cookie_token:
        headers = {'Authorization': cookie_token}
        # 发起注销请求
        try:
            r = requests.get(sso_server + '/logout', headers=headers, timeout=10)
            if r.status_code == requests.codes.ok:
                if r.text == 'logout success':
                    return redirect('/')
        except Exception as e:
            print(e)

    return redirect('/')



if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0',port=8082)

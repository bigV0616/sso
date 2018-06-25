# -*- coding: utf-8 -*-
import python_jwt

def getCookieInfo(cookie_info):
    info = python_jwt.json_decode(cookie_info)
    return info

def checkCookieToken(req, tokens):
    # request中是否携带了cookie
    cookie = req.headers.get('Authorization', None)
    if cookie:
        info = getCookieInfo(cookie)
        if info:
            sid = tokens.get(cookie, None)
            print "[sso] sid:", sid
            if sid:
                return sid
    return False
# coding: utf-8
# AUTHOR: BIGV YANG yangdawei@7lk.com
# DATA:   2018-06-26
import ldap
from conf.app import ProdConfig
#LDAP_SERVER = "ldap://10.9.2.222:389"
#BASE_DN = "dc=7lk, dc=com"
#DN = "cn=Manager,dc=7lk,dc=com"

def checkUserPwd(username, password):
    user_dn = "uid=%s, ou=users, %s"%(username, ProdConfig.BASE_DN)
    conn = ldap.initialize(ProdConfig.LDAP_SERVER)
    try:
        conn.simple_bind_s(user_dn, password)
    except Exception, e:
        return False
    return True

if __name__ == "__main__":
    print checkUserPwd("yangdawei", "111qqq")
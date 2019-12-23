from django.contrib.auth.hashers import check_password,make_password


def make_token(pwd):
    token = make_password(pwd,'123')
    return token


def check_token(pwd,m_pwd):
    token = check_password(pwd,m_pwd)
    return token

import uuid

from rest_framework.response import Response
from rest_framework.views import APIView
from units.redis import r
from units.token import make_token, check_token
from user.models import User


class Login(APIView):
    def post(self, request):
        mes = {}
        data = request.data
        user = User.objects.filter(username=data['username'], password=data['password']).first()
        if user:
            uid = str(uuid.uuid1())
            t = make_token(uid)
            r.set(user.id, uid)
            mes['message'] = '登录成功'
            mes['code'] = 200
            mes['token'] = t
            mes['user_id'] = user.id
        return Response(mes)


class Index(APIView):
    def post(self, request):
        mes = {}
        data = request.data
        token = r.get(data['user_id']).decode()
        c_token = check_token(token, data['token'])
        if c_token:
            mes['code'] = 200
        else:
            mes['code'] = 400
            mes['message'] = '账号已在别处登录'
        return Response(mes)

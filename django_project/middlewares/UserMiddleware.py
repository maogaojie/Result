import time
from units.redis import r
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        if r.llen(ip) < 5:  # 如果长度（次数）小于5就添加一条数据
            timestamp = int(time.time())  # 1576739124.0805035 小数点，用int去除小数点
            r.rpush(ip, timestamp)  # 在尾部加一条ip为key,当前时间戳为value的数据
        else:
            timestamp = r.lrange(ip, 0, 0)  # 获取第一条数据  key start stop 返回一个列表
            stimestamp = timestamp[0].decode()  # 编码为字符串，默认为bytes
            t = int(time.time())
            if t - int(stimestamp) > 60:  # 60秒内判断   如果当前时间减去第一次访问的时间大于60秒
                r.lpop(ip)  # 移除第一条数据
                r.rpush(ip, t)  # 添加新的一条数据
            else:  # IP超过限制次数
                return HttpResponse('访问次数过于频繁')

# class SessionMiddleware(MiddlewareMixin):
#
#     def process_request(self, request):
#         if not request.path in ['/user/login/',]:
#             user = request.session.get('user_id')
#             if not user:
#                 return HttpResponse('请登录')
#             else:
#                 session_key = request.session.session_key
#                 for session in Session.objects.exclude(session_key=session_key):  # 不是当前浏览的会话session
#                     data = session.get_decoded()
#                     if data.get('user_id') == request.session.get('user_id'):
#                         session.delete()

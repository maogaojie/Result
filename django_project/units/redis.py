import redis

# 当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时
# 无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接

pool = redis.ConnectionPool(host='127.0.0.1')  # 实现一个连接池,选择数据库0 ,password='pwd'
r = redis.Redis(connection_pool=pool)


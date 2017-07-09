import redis,json

try:
    r=redis.StrictRedis(host='192.168.0.109',port=6379)
except Exception,e:
    print e.message

pipe = r.pipeline()
pipe_size = 10000000

len = 0
key_list = []
print r.pipeline()
keys = r.keys("it475*")
for key in keys:
    key_list.append(key)
    pipe.get(key)
    if len < pipe_size:
        len += 1
    else:
        for (k, v) in zip(key_list, pipe.execute()):
            print k, v
        len = 0
        key_list = []

for (k, v) in zip(key_list, pipe.execute()):
    print json.loads(v)["content"][0]
#r.flushdb()
    # keys = r.keys()
# print type(keys)
# print keys
# print r.get("a")
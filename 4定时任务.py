import time

# 时间戳:1970年1月1日0点0分0秒到当前时间的时间间隔,单位秒
print(time.time())
while True:
    time.sleep(24 * 60 * 60)  # 经过一天
    print("hello world")

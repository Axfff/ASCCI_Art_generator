# -*- coding:utf-8 -*-
 
import win32api
import win32con
import time
import threading
# -1代表向下移动一个单位，-100也会向下移动一个单位，都是一个单位哦，亲~

print("即将开始自动滚动...")
for i in range(4):
    print(3-i)
    time.sleep(1)

stop = False
def timer():
    global stop
    for i in range(1,221):
        print("剩余时间%ss"%(220-i))
        time.sleep(1)
    stop = True
    return


threading.Thread(target=timer).start()
while not stop:
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-770)
    time.sleep(0.001)

#1147,0.002
#1930,0.004
#770,0.0001



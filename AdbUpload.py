# -*- coding: utf8 -*-
# -*- 自动刷机务通数据 -*-
import os
import time
out = os.popen('adb push C:\Users\kaiku\adb\畅想机务通 /storage/sdcard0/').readlines()
time.sleep(5)
print out
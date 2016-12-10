# -*- coding: utf8 -*-
# 自动刷机务通数据
import os
import pygame
import threading
import re
count = 0
adbDevices = []
devicesNum =  []
doneDevicesNum = []
toDoDevicesNum =[]

def upload(deviceNum = ''):
    print deviceNum + '线程开始上传\n'
    global count
    # 在此处插入执行的ADB命令语句
    os.popen("adb -s %s uninstall com.tf.elecbook"%deviceNum)
    os.popen("adb -s %s install /home/dukaiguang/jwt客户端/elecbook.apk"%deviceNum)
    print deviceNum + '线程安装apk完成\n'
    os.popen("adb -s %s push /home/dukaiguang/jwt客户端/畅想机务通/ /sdcard/"%deviceNum)
    os.popen("adb -s %s shell reboot"%deviceNum)
    pygame.mixer.music.play()
    count += 1 # 刷新设备总数计数
    print deviceNum + ("上传完成,请拔下设备,目前总共上传完成%d\n"%count)

if __name__ == '__main__':
    pygame.init()
    # 随便找了个音乐做完成提示音
    pygame.mixer.music.load("/usr/share/sounds/ubuntu/ringtones/Ubuntu.ogg")
    while True:
        # 首先清空要刷机的设备列表
        toDoDevicesNum = []
        adbDevices = os.popen("adb devices").readlines()
        # 把安卓设备序号提出来
        for line in adbDevices[1:-1]:
            deviceNum = (re.sub(r'\S*\s*\n','',line))
            # 已经上传过数据的不再刷机
            if deviceNum not in doneDevicesNum:
                toDoDevicesNum.append(deviceNum)
        for line in toDoDevicesNum:
            # 开启线程把设备序号传给上传程序
            threadUpload = threading.Thread(target=upload,args=(line,))
            threadUpload.setDaemon(True)
            threadUpload.start()
            print line + '上传线程正在运行中\n'
            # 把上传过数据的加入列表
            doneDevicesNum.append(line)

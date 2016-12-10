# -*- coding: utf8 -*-
# 自动刷机务通数据
import os
import pygame
done = False
count = 0


def upload():
    global done, count
    # 在此处插入执行的ADB命令语句
    os.popen("adb uninstall com.tf.elecbook")
    os.popen("adb install /home/dukaiguang/jwt客户端/elecbook.apk")
    os.popen("adb push /home/dukaiguang/jwt客户端/畅想机务通/ /sdcard/")
    pygame.mixer.music.play()
    done = 1 # 连接的设备刷新完成标志
    count += 1 # 刷新设备总数计数
    print ("上传完成一台,请拔下设备,目前总共上传完成%d"%count)

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.music.load("/usr/share/sounds/ubuntu/ringtones/Ubuntu.ogg") # 随便找了个音乐做完成提示音
    while True:
        if (done == False)and((len(os.popen('adb devices').readlines())) == 3):
            print ("发现设备,开始上传")
            upload()
        elif (done == True)and((len(os.popen('adb devices').readlines())) != 3):
            done = False # 把刷新完成标志清除
            print ("请插入一台新设备")
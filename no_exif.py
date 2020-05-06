# -*- coding:utf-8 -*-
"""
Summary of the code:
    Test using exif tools.
    
@Author:
    Gao-zl
@Time:
    2020.05.05
"""
import exifread
import os
import time

"""
Summary of this function:
    get the exif imfomation of the photo.
    取消这种方式，因为exif有可能没有相关信息
    
"""
def getSimpleExif(filename):
    # 读取照片信息
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd)
    fd.close()
    print(tags['Image DateTime'])

# getSimpleExif("testImg/2.jpg")



"""
Summary of this function:
    get the time of photo.
    
"""
def getTime(filename):
    # 读取照片
    statinfo = os.stat(filename)
    print(statinfo)

    # 获取文件修改时间
    mtime = statinfo.st_mtime
    time_local = time.localtime(mtime)
    time_YmdHMS = time.strftime("%Y%m%d_%H%M%S", time_local)
    print('currentTimeStamp:', mtime)
    print('time_local:', time_local)
    print('time_YmdHMS:', time_YmdHMS)

getTime("testImg/IMG_0031.JPG")
print("=============================")
getTime("testImg/IMG_0032.JPG")
print("=============================")
getTime("testImg/1.png")
print("=============================")
getTime("testImg/2.jpg")
print("=============================")
getSimpleExif("testImg/IMG_0032.JPG")
print("=============================")
getTime("testImg/IMG_8092.JPG")
print("=============================")
getTime("testImg/IMG_8111.JPG")
print("=============================MP4")
getTime("testImg/FPES9285.MP4")
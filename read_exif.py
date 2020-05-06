"""
Summary of the code:
    Rename the photos in files.
    There are two ways:
    1.If the photo has exif imfomation, rename it by exif time.
    2.If the photo dont has exif imfomation, remane it using backup time. 
    This code is No.1 way.
    You can run the main.py

@author:
    Gao-zl
@Time:
    2020.05.05
"""
import os
import exifread

def getExif(path, filename):
    old_full_file_name = os.path.join(imgpath, filename)
    # 定义一个字典值便于后续调用
    FIELD = "EXIF DateTimeOriginal"
    # 读取照片
    fd = open(old_full_file_name, 'rb')
    tags = exifread.process_file(fd)
    fd.close()

    if FIELD in tags:
        # 当存在exif信息的时候，保存为拍摄时间相关
        # 以下为测试输出内容
        print("===========================================")
        # print("\nstr(tags[FIELD]): %s" % (str(tags[FIELD])))  # 获取到的结果格式类似为：2018:12:07 03:10:34
        # print("\nstr(tags[FIELD]).replace(':', '').replace(' ', '_'): %s" % (str(tags[FIELD]).replace(':', '').replace(' ', '_')))  # 获取结果格式类似为：20181207_031034
        # print("\nos.path.splitext(filename)[1]: %s" % (os.path.splitext(filename)[1]))  # 获取了图片的格式，结果类似为：.jpg
        new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + os.path.splitext(filename)[1]
        # print("\nnew_name: %s" % (new_name))  # 20181207_031034.jpg
        #
        # time = new_name.split(".")[0][:13]
        # new_name2 = new_name.split(".")[0][:8] + '_' + filename
        # print("\nfilename: %s" % filename)
        # print("\n%s的拍摄时间是: %s年%s月%s日%s时%s分" % (filename, time[0:4], time[4:6], time[6:8], time[9:11], time[11:13]))

        # 可对图片进行重命名
        new_full_file_name = os.path.join(imgpath, new_name)
        # print(new_full_file_name)
        print(old_full_file_name," ---> ", new_full_file_name)
        # os.rename(old_full_file_name, new_full_file_name)
    else:
        print("===============================================")
        print('No {} found'.format(FIELD), ' in: ', old_full_file_name)


imgpath = "D:\\github\\Photo-backup\\testImg"

for filename in os.listdir(imgpath):
    full_file_name = os.path.join(imgpath, filename)

    if os.path.isfile(full_file_name):
        getExif(imgpath, filename)
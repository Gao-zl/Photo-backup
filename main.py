"""
Summary of the code:
    Rename the photo in files.
    There are two ways:
        1.If the photo has exif infomation, rename it by exif time.
        2.If don't have it, rename it by save time.
        
@author: 
    Gao-zl
@Time:
    2020.05.06  v0.1
    2020.05.07  v0.2
    2020.05.08  v1.0
    2020.05.09  v1.1
"""
import os
import tqdm
import time
import exifread

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from gui import Ui_Form

'''
function：
    重命名主函数
'''
def rename(path, filename):

    old_full_file_name = os.path.join(imgpath, filename)
    # 定义一个字典值后续使用
    FIELD = "EXIF DateTimeOriginal"
    fd = open(old_full_file_name, 'rb')
    tags = exifread.process_file(fd)
    fd.close()

    # 有exif信息时
    if FIELD in tags:
        # 改变数据的格式，加上原有的后缀名
        new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(current_process)\
                   + os.path.splitext(filename)[1]
        # 生成新的文件按路径
        new_full_file_name = os.path.join(imgpath, new_name)

        try:
            os.rename(old_full_file_name, new_full_file_name)
            # 输出结果
            w.textBrowser.append('[info]%d/%d   Success!   %s--->%s'%(current_process, total, filename, new_name))
            QApplication.processEvents()
        except Exception as e:
            w.textBrowser_2.append('[info]%d/%d   Failed!    %s'%(current_process, total, e))
            QApplication.processEvents()


    # 无exif信息时
    else:
        # 读取文件信息
        statinfo = os.stat(old_full_file_name)
        # 获取文件的修改时间，也就是首次创建的时间
        mtime = statinfo.st_mtime
        # 时间格式转化
        time_local = time.localtime(mtime)
        time_YmdHMS = time.strftime("%Y%m%d_%H%M%S", time_local)
        # 更新名字
        new_name_without_exif = str(time_YmdHMS) + '_' + str(current_process)\
                                + os.path.splitext(filename)[1]
        new_full_file_name_without_exif = os.path.join(imgpath, new_name_without_exif)

        # 重命名
        try:
            os.rename(old_full_file_name, new_full_file_name_without_exif)
            # 输出结果
            w.textBrowser.append(
                '[info]%d/%d   Success!   %s--->%s' % (current_process, total, filename, new_name_without_exif))
            QApplication.processEvents()
        except Exception as e:
            w.textBrowser_2.append('[info]%d/%d   Failed!    %s'%(current_process, total, e))
            QApplication.processEvents()


'''
function:
    main
'''
# if __name__ == '__main__':
#
#     print("请输入绝对路径：")
#     input_path = input()
#     imgpath = input_path
#
#     # 统计处理数量
#     total = len([lists for lists in os.listdir(imgpath)])
#     current_process = 1
#
#     start_time = time.time()
#     for filename in os.listdir(imgpath):
#         full_file_name = os.path.join(imgpath, filename)
#
#         if os.path.isfile(full_file_name):
#             rename(imgpath, filename)
#             current_process += 1
#     end_time = time.time()
#     print("程序运行时间：",end_time - start_time)
#     input("按下任意键退出")

'''
function:
    Using GUI

@time:
    2020.05.08
'''

class mwindow(QWidget, Ui_Form):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)

    # 定义一个输入方法，将输入的信息获取下来
    def click_button(self):
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        self.textBrowser_3.clear()
        global imgpath, current_process, total, filename
        current_process = 1
        total = 1
        imgpath = self.lineEdit.text()
        self.textBrowser.append(imgpath)


        # 增加纠错机制v1.1
        try:
            total = len([lists for lists in os.listdir(imgpath)])
            start_time = time.time()
            for filename in os.listdir(imgpath):
                full_file_name = os.path.join(imgpath, filename)
                if os.path.isfile(full_file_name):
                    rename(imgpath, filename)
                    current_process +=1
            end_time = time.time()
            self.textBrowser_3.append("%f"%(end_time-start_time))
        except Exception as e:
            self.textBrowser_2.append("%ss"%(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    # 将输入的给输出来
    w.pushButton.clicked.connect(w.click_button)
    w.show()
    sys.exit(app.exec_())
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
    2020.05.09  v2.0
    2020.05.09  v2.1
    2020.05.10  v2.2
"""
import os
import tqdm
import time
import exifread

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from gui import Ui_Form
from backup_gui import Ui_Dialog

import shutil

'''
function：
    重命名主函数
'''
def rename(path, filename):
    # 获取旧的照片名称：带照片的地址
    old_full_file_name = os.path.join(imgpath, filename)
    # 定义一个字典值后续使用
    FIELD = "EXIF DateTimeOriginal"
    fd = open(old_full_file_name, 'rb')
    tags = exifread.process_file(fd)
    fd.close()

    # 有exif信息时，即tags中存在FIELD字段，采用exif信息
    if FIELD in tags:
        # 改变数据的格式，加上原有的后缀名
        new_name = str(tags[FIELD]).replace(':', '').replace(' ', '_') + '_' + str(current_process)\
                   + os.path.splitext(filename)[1]
        # 生成新的文件按路径
        new_full_file_name = os.path.join(imgpath, new_name)

        try:
            # 系统的rename函数
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
            # 实现实时刷新的功能
            QApplication.processEvents()
        except Exception as e:
            w.textBrowser_2.append('================错误提示信息================'
                                   '[info]%d/%d   Failed!    %s'%(current_process, total, e))
            QApplication.processEvents()


'''
function:
    main for v0.1-0.2
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
        # 清除原有的输出内容
        self.textBrowser.clear()
        self.textBrowser_2.clear()
        # self.textBrowser_3.clear()
        # 全局变量
        global imgpath, current_process, total, filename
        # 当前处理的编号
        current_process = 1
        # 文件夹下文件数量
        total = 1
        # 获取输入的信息
        imgpath = self.lineEdit.text()
        self.textBrowser.append(imgpath)


        # 增加纠错机制v1.1
        try:
            # 读取文件数量，作为全局变量total
            total = len([lists for lists in os.listdir(imgpath)])
            start_time = time.time()
            # 循环读取一个个处理
            for filename in os.listdir(imgpath):
                full_file_name = os.path.join(imgpath, filename)
                if os.path.isfile(full_file_name):
                    rename(imgpath, filename)
                    current_process +=1
            end_time = time.time()
            self.textBrowser.append("================================"
                                    "\n完成！程序运行时间为：%f 秒"%(end_time-start_time))
        except Exception as e:
            self.textBrowser_2.append("================错误提示信息================\n"
                                      "%s"%(e))

    # 跳转到备份工具
    def change_to_backup(self):
        # v2.2取消关闭页面，可同时运行
        # # 关闭前一个页面
        # self.close()
        # 打开新的页面
        m2window.backup_gui(self)


'''
Summary:
    判断文件夹是否存在,不存在即创建一个

@time:
    2020.05.09
'''
def make_path(path):
    if not os.path.exists(path):
        os.makedirs(path)


'''
Summary:
    判断文件是否存在，并决定是否要移过去

@time：
    2020.05.09
'''
def move_photo(origin_full_file_name, backup_full_path):
    try:
        shutil.copy2(origin_full_file_name, backup_full_path)
    except Exception as e:
        print(e)


'''
Summary:
    Photo backup function

@time:
    2020.05.09
'''
# 定义新类
class m2window(QWidget, Ui_Dialog):
    # 绘制gui
    def __init__(self):
        super(m2window, self).__init__()
        self.setupUi(self)

    def backup_gui(self):
        self.w2 = m2window()
        self.w2.show()
        self.w2.pushButton.clicked.connect(self.w2.start_backup)


    # 开始执行备份操作
    def start_backup(self):
        # 清除原有的输出，如果有的话
        self.textBrowser.clear()
        # self.textBrowser_3.clear()
        # 定义全局变量
        global origin_path, backup_path
        # 获取地址信息
        # 定义一个输入方法，将输入的信息保存下来
        # 在此处即为原照片地址信息和新照片地址信息
        origin_path = self.lineEdit.text()
        backup_path = self.lineEdit_2.text()

        # v2.1新增内容：增加纠错机制
        try:
            total2 = len([lists for lists in os.listdir(origin_path)])
            current2 = 1
            start_time2 = time.time()
            for filename in os.listdir(origin_path):
                # 获取照片的含地址的名称
                origin_full_file_name = os.path.join(origin_path, filename)
                if os.path.isfile(origin_full_file_name):
                    # 备份主函数
                    # 获取时间信息:日期和月份
                    year = filename.split('_')[0][:4]
                    month = filename.split('_')[0][4:6]

                    # 构建完整目录结构
                    backup_full_path = backup_path + '\\' + year + '\\' + month
                    make_path(backup_full_path)

                    # 移动照片到对应的文件夹下
                    move_photo(origin_full_file_name, backup_full_path)
                    # 输出信息
                    self.textBrowser.append("[info]%d/%d  %s  -->  %s"%(current2, total2, filename, backup_full_path))
                    # 实现实时刷新的功能
                    QApplication.processEvents()
                    current2 += 1
            end_time2 = time.time()
            self.textBrowser.append("[info] total：%d 已存入备份文件夹：%s"%(total2, backup_path))
            self.textBrowser.append("================================"
                                    "\n完成！程序运行时间为：%f 秒"%(end_time2-start_time2))
        except Exception as e:
            self.textBrowser.append("================错误提示信息================\n"
                                    "%s"%(e))


if __name__ == '__main__':

    # 照片重命名功能模块
    app = QApplication(sys.argv)
    w = mwindow()
    # 将输入的给输出来
    w.pushButton.clicked.connect(w.click_button)
    w.pushButton_2.clicked.connect(w.change_to_backup)
    w.show()
    sys.exit(app.exec_())
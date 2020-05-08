"""
Summary of the code:
    Use test.py
    
@author:
    Gao-zl
    
@time:
    2020.05.08
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import test

if __name__ == '__main__':
    # QApplication创建一个QApplication的实例，如果没有这个实例，QT无法执行
    # sys.argv是命令行参数，可以通过命令启动的时候传递参数
    app = QApplication(sys.argv)
    # 创建一个windows实例（对象），MainWindows是实例（对象）的名字，可以随便起
    MainWindow = QMainWindow()
    # 调用在test中出现的类（QtPy5自动生成的）
    ui = test.Ui_Form()
    ui.setupUi(MainWindow)
    # 展示
    MainWindow.show()
    # 一直运行下去，除非有人关闭它
    sys.exit(app.exec_())
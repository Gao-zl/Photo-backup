# Photo-backup


## Background:


    由于本人常备份照片，而相机或手机导出的照片名称不够规范
    因此使用python写个小工具开发一款提取exif信息重新命名的小工具
    后续存储到对应日期目录下，进行备份

    In view of the fact that I often back up photos,
    and the names of the photos exported by the camera or mobile phone are not standardized,
    I used python to write a gadget to develop a renamed gadget,
    which was subsequently stored in the corresponding date directory for backup

## Install&Usage:


    运行环境为python3.x，使用到的库主要为exifread
    GUI框架为PyQt5

    只需下载dist目录下main.exe即可使用

    The operating environment is python3.x, and the libraries used are mainly exifread.
    The GUI framework is PyQt5.
    Just download main.exe in the dist directory to use


## Version:


    ### v0.1 简单实现原始的重命名功能

    ### v0.2 解决如果照片出现相同时间无法重命名问题，目前的名称定义为 年月日_时分秒_文件夹中的次序.xxx

    ### v1.0 实现简单GUI界面展示
             使用的是PyQt5的框架，具体流程介绍：
             使用PyQt5的designer.exe来构建界面，将.ui文件用拓展改为.py文件
             调用.py文件的内容来展示
             PS:GUI文件夹为测试使用
             版本1.0为最简单的带有界面的版本，稍微等待一会儿即可完成任务
             可去dist/main下的main.exe下载使用

    ### v1.1 新增纠错机制，不会导致程序奔溃
             新增实时更新机制，不会导致程序要卡一下才能输出
             优化界面展示

    ### v2.0 实现照片备份功能（带GUI，入口在照片命名的下方）
             可以备份到自己需要的地方，不存在目录时自动创建
             用年份+月份的方式来进行备份

    ### v2.1 实现纠错机制，输出程序无法执行原因
             实时刷新机制
             优化界面展示

@author:
    Gao-zl
    2020

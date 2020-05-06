# Photo-backup

## Background:

    由于本人常备份照片，而相机或手机导出的照片名称不够规范，因此使用python写个小工具开发一款提取exif信息重新命名的小工具，后续存储到对应日期目录下，进行备份
    In view of the fact that I often back up photos, and the names of the photos exported by the camera or mobile phone are not standardized, I used python to write a gadget to develop a renamed gadget, which was subsequently stored in the corresponding date directory for backup

## Install&Usage:

    运行环境为python3.x，使用到的库主要为exifread
    当然直接使用的话可以运行dist下的main.exe即可
    The operating environment is python3.x, and the libraries used are mainly exifread
    Of course, if you use it directly, you can run main.exe under dist.

## Version:

    ### v0.1 简单实现原始的重命名功能

    ### v0.2 解决如果照A片出现相同时间无法重命名问题，目前的名称定义为 年月日_时分秒_文件夹中的次序.xxx


@uthor:
    Gao-zl

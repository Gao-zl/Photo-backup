import os
import shutil

origin_path = "D:\\github\\Photo-backup\\testImg"
backup_path = "D:\\github\\Photo-backup\\testImg2"

def make_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_photo(origin_full_file_name,backup_full_path):
    try:
        shutil.copy2(origin_full_file_name,backup_full_path)
    except Exception as e:
        print(e)

for filename in os.listdir(origin_path):
    # 获取照片的含地址的名称
    origin_full_file_name = os.path.join(origin_path, filename)
    if os.path.isfile(origin_full_file_name):
        # 备份主函数
        # 获取时间信息
        year = filename.split('_')[0][:4]
        month = filename.split('_')[0][4:6]
        print(year)
        print(month)

        backup_full_path = backup_path + '\\' + year + '\\' + month

        make_path(backup_full_path)

        move_photo(origin_full_file_name,backup_full_path)


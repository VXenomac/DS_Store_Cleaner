import os
from pathlib import Path


def remove_file(path):
    """
    根据文件路径删除文件
    :param files: 当前目录下及子文件夹下的所有文件
    """
    path = Path(path)
    files = [f for f in path.rglob('.DS_Store')]
    for file_path in files:
        print('正在删除 %s…' % file_path)
        os.remove(file_path)
    print('一共删除 %d 个 .DS_Store 文件…' % len(files))

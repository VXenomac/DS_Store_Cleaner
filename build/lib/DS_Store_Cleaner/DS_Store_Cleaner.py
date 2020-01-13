import os


os.chdir(os.getcwd())


def all_file(base_path):
    """
    遍历出当前路径或指定路径及子目录下的所有文件
    :param base_path: 指定路径
    :return files: 包含所有文件路径的列表
    """
    files = []
    for item in os.listdir(base_path):
        file_path = os.path.join(base_path, item)
        if os.path.isdir(file_path):
            all_file(file_path)
        else:
            files.append(os.path.join(base_path, file_path))
    return files


def remove_file(files):
    """
    根据文件路径删除文件
    :param files: 当前目录下及子文件夹下的所有文件
    """
    files = [f for f in files if f.endswith('.DS_Store')]
    for file_path in files:
        print('正在删除 %s…' % file_path)
        os.remove(file_path)
    print('一共删除 %d 个 .DS_Store 文件…' % len(files))

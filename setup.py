import setuptools


setuptools.setup(
    name='DS_Store_Cleaner',
    version='0.2',
    author='VXenomac',
    author_email='vxenomac@xyzlab.ai',
    description='删除当前目录或指定目录下所有的 .DS_Store 文件',
    url='https://github.com/VXenomac/DS_Store_Cleaner',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    entry_points={
        'console_scripts': [
            'dsclean = DS_Store_Cleaner.__main__:main'
        ]
    }
)

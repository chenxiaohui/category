# category

a tool to category files into disk collections. It will prompt you which directory to use.

# usage

    python category.py <filname|filelist>

recommend:

    bk='python ~/share/category/category.py '

# config

    base_dir = "/Volumes/exdisk/百度云同步盘/itbooks/" #directory to sync(base)
    del_after_copy=True #del file after category it to that directory
    extra=(u'其他',u'自定义') # when prompt sub directory auto add this two choices.
    prompt=False #whether prompt a message when copy (and delete) or not

# example:

    $  bk 人工神经网络实用教程.pdf
    ----------------------人工神经网络实用教程.pdf----------------------
    0 office&tex
    1 安全
    2 3d
    3 AS
    4 C#
    5 c++
    6 http
    7 java
    8 Linux
    9 mac
    10 开发工具
    11 总结
    12 推荐系统
    13 搜索引擎
    14 操作系统
    15 数字图像处理
    16 数据库
    17 数据挖掘
    18 机器学习
    19 硬件
    20 移动
    21 算法
    22 编码
    23 编译原理
    24 网络
    25 自我修炼
    26 虚拟机
    27 论文
    28 设计模式
    29 课程电子书
    30 软件工程
    31 面试
    32 php
    33 python
    34 vim
    35 web服务器
    36 windows
    37 产品理念
    38 其他
    39 其他语言
    40 分布式
    41 多媒体
    select a most probably one:
    18
    人工神经网络实用教程.pdf 机器学习/
    mv '人工神经网络实用教程.pdf' /Volumes/exdisk/百度云同步盘/itbooks//机器学习/
    ln -s  '/Volumes/exdisk/百度云同步盘/itbooks//机器学习//人工神经网络实用教程.pdf' '人工神经网络实用教程.pdf''

result:

    $ ls -la
    lrwxr-xr-x    1 cxh  staff         92 Jun 20 22:03 人工神经网络实用教程.pdf@ -> /Volumes/exdisk/百度云同步盘/itbooks//机器学习//人工神经网络实用教程.pdf

this file has already been moved to the directory : /Volumes/exdisk/百度云同步盘/itbooks//机器学习/ only leaves this symbole file here.

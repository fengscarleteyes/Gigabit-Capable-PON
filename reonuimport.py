# -*- coding:  utf-8 -*-
# Author: zhengyanfeng (fengscarleteyes, hongyan)
'''导入指定文件类型'''
import os


def file_name():
    '''定义寻找文件路径的函数'''
    dir_path = os.getcwd()
    # 读取当前文件夹路径
    file_list = os.listdir(dir_path)
    # 列出当前文件夹的文件列表
    file_type_log = []
    # 定义空列表
    for file_type_var in file_list:
        # 遍历列表
        if '.log' in file_type_var:
            # 找出带有'.log'字样的文件
            file_type_log.append(file_type_var)
            # 增加到file_type_log
    if len(file_type_log) != 1:
        # file_type_log 的元素不等于1时
        # file_log_path = 'README.md'
        print('请阅读MARKDOWN文档 : README.md')
        # 返回'readme'的路径,并打印
    else:
        file_log_path = file_type_log[0]
        # 返回'.log'文件的路径
        return file_log_path


def file_import(path_var):
    '''导入单个端口配置文件'''
    # file_obj = open(
    #     path_var,
    #     mode='r', buffering=-1,
    #     encoding='UTF-8', errors=None,
    #     newline=None, closefd=True
    #     )
    file_obj = open(path_var, mode='r', encoding='UTF-8')
    # 打开文件
    string_file = file_obj.read()
    # 读取文件
    file_obj.close()
    # 关闭文件
    return string_file
    # 函数返回读取的字符


FILE_NAME_STR = file_name()
# 得出路径
FILE_READ = file_import(FILE_NAME_STR)
# 读取文件内容


def cfg_old():
    '''方法返回文本内容'''
    return FILE_READ


# 测试语句
# print(FILE_READ)

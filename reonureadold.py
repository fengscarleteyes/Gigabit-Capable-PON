# -*- coding:  utf-8 -*-
# Author: zhengyanfeng (fengscarleteyes, hongyan)
'''
re 正则表达式 匹配相关数据
初始化配置的源文件
'''
import re

import reonuimport
# import reonutmp


def re_onu_pool(str_var1):
    '''利用正则表达式筛选出添加ONU的指令'''
    re_ont_add = re.compile(
        ' ont add ' + '[0-9]*?' + ' ' + '[0-9]*?'
        + '.*?' + '(?=desc)', re.S
        )
    # 正则表达式
    re_ont_add_var = re.findall(re_ont_add, str_var1)
    # 将筛选出的字符串（个别数据包含换行）赋值并return
    return re_ont_add_var


def re_srv_pool(str_var2):
    '''利用正则表达式筛选出ONU对应的srv业务流指令'''
    re_ont_srv = re.compile(
        ' service-port ' + '[0-9]*' + ' ' + '.*?' + '(?=\n service-port)', re.S
        )
    # 正则表达式
    re_srv_pool_var = re.findall(re_ont_srv, str_var2)
    # 将筛选出的字符串（个别数据包含换行）赋值并return
    return re_srv_pool_var


def re_onu_ip(str_var4):
    '''用正则表达式筛选出大U的ip地址'''
    # ont ipconfig 1 78 static ip-address 172.28.0.5
    # mask 255.255.255.128 vlan 4000  priority 6
    # gateway 172.28.0.1
    re_ont_ip = re.compile(
        ' ont ipconfig '
        + '[0-9]*'
        + ' '
        + '[0-9]*'
        + ' '
        + '.*?' '(?=\n ont)', re.S)
    re_onu_ip_var = re.findall(re_ont_ip, str_var4)
    return re_onu_ip_var


def re_onu_alarm(str_var5):
    '''用正则表达式筛选出onu告警模板'''
    # ont alarm-policy 1 1 policy-id 1
    re_ont_alarm = re.compile(
        ' ont alarm-policy '
        + '[0-9]*'
        + ' '
        + '[0-9]*'
        + ' '
        + '.*?' '(?=\n ont)',
        re.S)
    re_onu_alarm_var = re.findall(re_ont_alarm, str_var5)
    return re_onu_alarm_var


def re_onu_snmp(str_var6):
    '''用正则表达式筛选出snmp模板'''
    #  ont snmp-profile 1 3 profile-id 3
    re_ont_snmp = re.compile(
        ' ont snmp-profile '
        + '[0-9]*'
        + ' '
        + '[0-9]*'
        + ' '
        + '.*?' '(?=\n ont)',
        re.S)
    re_onu_snmp_var = re.findall(re_ont_snmp, str_var6)
    return re_onu_snmp_var


def re_onu_native(str_var7):
    #  ont port native-vlan 1 8 eth 1 vlan 101 priority 1
    ''' 正则表达式取出nativevlan'''
    re_ont_native = re.compile(
        ' ont port native-vlan '
        + '[0-9]*'
        + ' '
        + '[0-9]*'
        + ' '
        + '.*?' '(?=\n ont)',
        re.S)
    re_onu_native_var = re.findall(re_ont_native, str_var7)
    return re_onu_native_var


def print_info(str_var3):
    '''打印测试'''
    tmp_str = str(len(str_var3))
    print('计算得出数据有 : ' + tmp_str + '条 ！')
    print('\n\n\n')
    print('命令列表如下 ：')
    for bbbb in str_var3:
        print(bbbb)
    print('\n\n\n')


# -------------------------------------------------------
ALLONU_STR = reonuimport.cfg_old()
# ALLONU_STR 割接的pon口命令全部的字符

ONU_ADD_CMD_OLD_TMP = re_onu_pool(ALLONU_STR)
ONU_ADD_CMD_OLD = []
for str_var8 in ONU_ADD_CMD_OLD_TMP:
    # 去除列表元素内的换行,
    if '\n' in str_var8:
        tmprep_1 = str_var8.replace('\n', '')
        ONU_ADD_CMD_OLD.append(tmprep_1)
    else:
        ONU_ADD_CMD_OLD.append(str_var8)
# ONU_ADD_CMD_OLD onu的添加命令 原本pon

ONU_SRV_CMD_OLD_TMP = re_srv_pool(ALLONU_STR)
ONU_SRV_CMD_OLD_TMP2 = []
ONU_SRV_CMD_OLD = []
for str_var9 in ONU_SRV_CMD_OLD_TMP:
    # 取出列表元素内的换行
    if '\n' in str_var9:
        tmprep_2 = str_var9.replace('\n', '')
        ONU_SRV_CMD_OLD_TMP2.append(tmprep_2)
    else:
        ONU_SRV_CMD_OLD_TMP2.append(str_var9)
for str_var10 in ONU_SRV_CMD_OLD_TMP2:
    # 取出列表元素内的双空格'  '
    if '  ' in str_var10:
        tmprep_3 = str_var10.replace('  ', ' ')
        ONU_SRV_CMD_OLD.append(tmprep_3)
    else:
        ONU_SRV_CMD_OLD.append(str_var10)
# ONU_SRV_CMD_OLD onu对应的业务流命令 原本pon

ONU_IP_CMD_OLD = re_onu_ip(ALLONU_STR)
# ONU_IP_CMD_OLD 大onu对应的IP地址 原本pon
ONU_ALARM_CMD_OLD = re_onu_alarm(ALLONU_STR)
# ONU_ALARM_CMD_OLD onu对应的告警模板
ONU_SNMP_CMD_OLD = re_onu_snmp(ALLONU_STR)
# ONU_SNMP_CMD_OLD onu的snmp简单网络管理协议模板
ONU_NATIVE_CMD_OLD = re_onu_native(ALLONU_STR)
# ONU_NATIVE_CMD_OLD onu的native-vlan,割接数据可不做上去

ONU_ALL_CMD_OLD = ONU_ADD_CMD_OLD + ONU_SRV_CMD_OLD \
   + ONU_IP_CMD_OLD + ONU_ALARM_CMD_OLD \
   + ONU_SNMP_CMD_OLD + ONU_NATIVE_CMD_OLD
# ONU_ALL_CMD_OLD 把取出的几个列表合并在一起
ONU_ALL_CMD_OLD.sort()
# 就地排序


def cfg_str_init():
    '''方法返回初始化后的原始配置文本'''
    return ONU_ALL_CMD_OLD

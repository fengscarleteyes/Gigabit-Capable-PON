# -*- coding:  utf-8 -*-
# Author: zhengyanfeng (fengscarleteyes, hongyan)
'''
re 正则表达式 匹配相关数据
修改原数据的各类模板id
使对应id均对应为name
'''
import re

import reonuimport

TMP_STR = reonuimport.cfg_old()


def re_onu_line(str_var_1):
    '''正则表达式找出onu的线路模板'''
    # ont-lineprofile gpon profile-id 64 profile-name "ftth"
    re_onu_line_pat = re.compile(
        ' ont-lineprofile gpon profile-id '
        + '[0-9]*' + ' profile-name '
        + '".*?"'
    )
    re_onu_line_var = re.findall(re_onu_line_pat, str_var_1)
    return re_onu_line_var


def re_onu_srv(str_var_2):
    '''正则表达式找出onu的业务模板'''
    # ont-srvprofile gpon profile-id 1 profile-name "FTTH-ALL-NEW"
    re_onu_srv_pat = re.compile(
        ' ont-srvprofile gpon profile-id '
        + '[0-9]*' + ' profile-name '
        + '".*?"'
    )
    re_onu_srv_var = re.findall(re_onu_srv_pat, str_var_2)
    return re_onu_srv_var


def re_traffic_table(str_var_3):
    '''正则表达式找出流量模板'''
    re_traffic_table_pat = re.compile(
        ' traffic table ip index '
        + '[0-9]*' + ' name ' + '".*?"'
    )
    # traffic table ip index 9 name "FTTH-VPN-2M-NEW"
    # cir 2048 cbs 67536 pir 4096 pbs 133072 color-mode
    # color-blind priority user-cos 3 inner-priority 3
    # priority-policy tag-in-package
    re_traffic_table_var = re.findall(re_traffic_table_pat, str_var_3)
    return re_traffic_table_var


# ont-lineprofile gpon profile-id 218 profile-name "ftth"
def onu_line_id_to_name(str_var_4):
    '''线路模板读取出id对应上NAME'''
    onu_line_id_to_name_pat1 = re.compile('profile-id ' + '[0-9]*')
    onu_line_id_to_name_pat2 = re.compile('".*?"')
    onu_line_id_to_name_idvar = re.findall(
        onu_line_id_to_name_pat1, str_var_4
        )
    onu_line_id_to_name_namevar = re.findall(
        onu_line_id_to_name_pat2, str_var_4
        )
    # ont add 1 1 password-auth "C6fYYQpwYn"
    # hex "4336665959517077596E" always-on
    # omci ont-lineprofile-id 218 ont-srvprofile-id 141
    # desc "ONT_NO_DESCRIPTION"
    onu_line_index = []
    for tmpstr_l1 in onu_line_id_to_name_idvar:
        if tmpstr_l1 != '':
            onu_line_index.append('ont-line' + tmpstr_l1 + ' ')
    for tmpstr_l2 in onu_line_id_to_name_namevar:
        if tmpstr_l2 != '':
            onu_line_index.append('ont-lineprofile-name ' + tmpstr_l2 + ' ')
    return onu_line_index


# ont-srvprofile gpon profile-id 141 profile-name "ftth"
def onu_srv_id_to_name(str_var_5):
    '''业务模板读取出id对应上NAME'''
    onu_srv_id_to_name_pat1 = re.compile('profile-id ' + '[0-9]*')
    onu_srv_id_to_name_pat2 = re.compile('".*?"')
    onu_srv_id_to_name_idvar = re.findall(
        onu_srv_id_to_name_pat1, str_var_5
        )
    onu_srv_id_to_name_namevar = re.findall(
        onu_srv_id_to_name_pat2, str_var_5
        )
    # ont add 1 1 password-auth "C6fYYQpwYn"
    # hex "4336665959517077596E" always-on
    # omci ont-lineprofile-id 218 ont-srvprofile-id 141
    # desc "ONT_NO_DESCRIPTION"
    onu_srv_index = []
    for tmpstr_s1 in onu_srv_id_to_name_idvar:
        if tmpstr_s1 != '':
            onu_srv_index.append('ont-srv' + tmpstr_s1 + ' ')
    for tmpstr_s2 in onu_srv_id_to_name_namevar:
        if tmpstr_s2 != '':
            onu_srv_index.append('ont-srvprofile-name ' + tmpstr_s2 + ' ')
    return onu_srv_index


# traffic table ip index 52 name "FTTH-VPN-50M-NEW"
def traffic_id_to_name(str_var_6):
    '''业务模板读取出id对应上NAME'''
    traffic_id_to_name_pat1 = re.compile(' index ' + '[0-9]*')
    traffic_id_to_name_pat2 = re.compile('".*?"')
    traffic_id_to_name_idvar = re.findall(
        traffic_id_to_name_pat1, str_var_6
        )
    traffic_id_to_name_namevar = re.findall(
        traffic_id_to_name_pat2, str_var_6
        )
    # service-port 40086 vlan 2226 gpon 0/1/1 ont 46 gemport 8 multi-service
    # user-vlan 81 tag-transform translate-and-add inner-vlan 2338 inbound
    # traffic-table index 147 outbound traffic-table index 147
    traffic_id_to_name_index = []
    for tmpstr_t1 in traffic_id_to_name_idvar:
        if tmpstr_t1 != '':
            traffic_id_to_name_index.append(
                'traffic-table' + tmpstr_t1
                )
    for tmpstr_t2 in traffic_id_to_name_namevar:
        if tmpstr_t2 != '':
            traffic_id_to_name_index.append(
                'traffic-table name ' + tmpstr_t2 + ' '
                )
    return traffic_id_to_name_index


ONT_LINE_VAR = re_onu_line(TMP_STR)
# onu线路模板列表
ONT_SRV_VAR = re_onu_srv(TMP_STR)
# onu业务模板列表
TRAFFIC_TABLE_VAR = re_traffic_table(TMP_STR)
# 流量模板列表

ONT_LINE_KEY = []
# 定义一个空数组ONT_LINE_KEY,用于存放配置文件读取出的线路模板id,以及对应名称
for tmpstr_var1 in ONT_LINE_VAR:
    ONT_LINE_KEY.append(onu_line_id_to_name(tmpstr_var1))
    # 遍历ONT_LINE_VAR线路模板配置文件
    # 将得出的对应数组增加到ONT_LINE_KEY

ONT_SRV_KEY = []
# 存放配置文件读取出的业务模板id,以及对应名称
for tmpstr_var2 in ONT_SRV_VAR:
    ONT_SRV_KEY.append(onu_srv_id_to_name(tmpstr_var2))

TRAFFIC_TABLE_KEY = []
# 存放配置文件读取出的流量模板id,以及对应名称
for tmpstr_var3 in TRAFFIC_TABLE_VAR:
    TRAFFIC_TABLE_KEY.append(traffic_id_to_name(tmpstr_var3))

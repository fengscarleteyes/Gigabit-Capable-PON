# -*- coding:  utf-8 -*-
# Author: zhengyanfeng (fengscarleteyes, hongyan)
'''
目标数据的导入
'''
import csv
import re
import reonunew


def getsolt():
    '''获取槽号'''
    slot_str = input('input slot num:')

    while not re.findall('^[0-9]*$', slot_str) or slot_str == '':
        slot_str = input('input slot num:')
    slot_value = int(slot_str)
    return slot_value


def getpon():
    '''获取端口号'''
    pon_str = input('input pon num:')
    while not re.findall('^[0-9]*$', pon_str) or pon_str == '':
        pon_str = input('input pon num:')
    pon_value = int(pon_str)
    return pon_value


# 读取文件,获得所有空闲内外层
TARGET_INNER_VLAN = []
# 宽带内外层
PPPOE_VLAN = []
# 电视内外层
OTT_VLAN = []
# tr069内外层
TR069_VLAN = []

with open('inner-vlan.csv', 'r', encoding='UTF-8') as csvfile:
    # 读取inner-vlan.csv内的可用内层vlan csvfile_str
    CSV_STR = csv.reader(csvfile, dialect='excel')
    for tmp_var1 in CSV_STR:
        TARGET_INNER_VLAN.append(tmp_var1)

for tmplist1 in TARGET_INNER_VLAN:
    if tmplist1[0] == 'PPPOE':
        PPPOE_VLAN.append(tmplist1)
        # 宽带内外层的区分

for tmplist2 in TARGET_INNER_VLAN:
    if tmplist2[0] == 'OTT':
        OTT_VLAN.append(tmplist2)
        # 电视内外层区分

for tmplist3 in TARGET_INNER_VLAN:
    if tmplist3[0] == 'TR069':
        TR069_VLAN.append(tmplist3)
        # tr069内外层区分

SOLTNUM = getsolt()
# 获取目标槽号
PONNUM = getpon()
# 获取目标端口号

FTTBONU_TARGET_CMD_LIST = []
FTTBMNGSRV_TARGET_CMD_LIST = []
FTTHONU_TARGET_CMD_LIST = []
SPLSRV_TARGET_CMD_LIST = []
NORMALSRV_TARGET_CMD_LIST = []
INNER_VLAN_RE = []

# 定义目标大ONU的添加命令
# 使用for遍历并进行替换
# 将替换后的值,赋值到对应数组

for tmp1 in reonunew.TERMINALCMD_CLASS.fttbonu:
    # 替换为目的端口,饼添加到FTTBONU_TARGET_CMD_LIST
    FTTBONU_TARGET_CMD_LIST.append(
        re.sub(' ont add [0-9]* ', ' ont add ' + str(PONNUM) + ' ', tmp1)
        )

for tmp2 in reonunew.TERMINALCMD_CLASS.ftthonu:
    # 替换为目的端口,饼添加到FTTHONU_TARGET_CMD_LIST
    FTTHONU_TARGET_CMD_LIST.append(
        re.sub(' ont add [0-9]* ', ' ont add ' + str(PONNUM) + ' ', tmp2)
        )

for tmp3 in reonunew.TERMINALCMD_CLASS.splsrv:
    # 专线业务流的对应替换
    tmp3_1 = re.sub(' service-port [0-9]* ', ' service-port ', tmp3)
    tmp3_2 = re.sub(
        '[0-9]*/[0-9]*/[0-9]*', '0/' + str(SOLTNUM) + '/' + str(PONNUM), tmp3_1
        )
    tmp3_3 = re.sub(' vlan [0-9]* ', ' vlan *zhuanxian-svlan* ', tmp3_2)
    tmp3_4 = re.sub(
        ' inner-vlan [0-9]* ', ' inner-vlan *zhuanxian-cvlan* ', tmp3_3
        )
    SPLSRV_TARGET_CMD_LIST.append(tmp3_4)

for tmp4 in reonunew.TERMINALCMD_CLASS.normalsrv:
    # 家宽 电视 tr069 的 业务流的对应替换
    tmp4_1 = re.sub(' service-port [0-9]* ', ' service-port ', tmp4)
    tmp4_2 = re.sub(
        '[0-9]*/[0-9]*/[0-9]*', '0/' + str(SOLTNUM) + '/' + str(PONNUM), tmp4_1
        )
    if ' vlan 900 ' in tmp4_2:
        NORMALSRV_TARGET_CMD_LIST.append(tmp4_2)
    elif re.search(' vlan [0-9]*[01] ', tmp4_2):
        tmp4_5 = PPPOE_VLAN.pop()
        tmp4_3 = re.sub(
            ' vlan [0-9]*[01] ', ' vlan ' + str(tmp4_5[1]) + ' ', tmp4_2
            )
        tmp4_4 = re.sub(
            ' inner-vlan [0-9]* ', ' inner-vlan ' + str(
                tmp4_5[2]) + ' ', tmp4_3
            )
        NORMALSRV_TARGET_CMD_LIST.append(tmp4_4)
    elif re.search(' vlan [0-9]*[6] ', tmp4_2):
        tmp4_6 = OTT_VLAN.pop()
        tmp4_7 = re.sub(
            ' vlan [0-9]*[6] ', ' vlan ' + str(tmp4_6[1]) + ' ', tmp4_2
            )
        tmp4_8 = re.sub(
            ' inner-vlan [0-9]* ', ' inner-vlan ' + str(
                tmp4_6[2]) + ' ', tmp4_7
            )
        NORMALSRV_TARGET_CMD_LIST.append(tmp4_8)
    elif re.search(' vlan [0-9]*[8] ', tmp4_2):
        tmp4_9 = TR069_VLAN.pop()
        tmp4_10 = re.sub(
            ' vlan [0-9]*[8] ', ' vlan ' + str(tmp4_9[1]) + ' ', tmp4_2
            )
        tmp4_11 = re.sub(
            ' inner-vlan [0-9]* ', ' inner-vlan ' + str(
                tmp4_9[2]) + ' ', tmp4_10
            )
        NORMALSRV_TARGET_CMD_LIST.append(tmp4_11)

for tmp5 in reonunew.TERMINALCMD_CLASS.fttbmngsrv:
    tmp5_1 = re.sub(' service-port [0-9]* ', ' service-port ', tmp5)
    tmp5_2 = re.sub(
        '[0-9]*/[0-9]*/[0-9]*', '0/' + str(SOLTNUM) + '/' + str(PONNUM), tmp5_1
        )
    tmp5_3 = re.sub(' vlan [0-9]* ', ' vlan *wangguan-vlan* ', tmp5_2)
    FTTBMNGSRV_TARGET_CMD_LIST.append(tmp5_3)

INNER_VLAN_RE = PPPOE_VLAN + OTT_VLAN + TR069_VLAN

# 取出对应ont-line ont-srv traffic table 的模板
# 整理模板和命令

INTERFACE_PON = []
INTERFACE_PON.append('interface 0/' + str(SOLTNUM))
QUIT_STR = ['quit', ]
# interface ?/?
# ...
# quit
ALLNEWCMD = INTERFACE_PON + FTTBONU_TARGET_CMD_LIST + \
    FTTHONU_TARGET_CMD_LIST + QUIT_STR + \
    FTTBMNGSRV_TARGET_CMD_LIST + NORMALSRV_TARGET_CMD_LIST + \
    SPLSRV_TARGET_CMD_LIST

TRAGET_ONT_LINE_NAME = []
# 线路模板
TRAGET_ONT_SRV_NAME = []
# 业务模板
TRAGET_SRV_SRVTRAFFIC_NAME = []
# 流量模板
for tmp6 in ALLNEWCMD:
    if re.search('ont-lineprofile-name ".*?"', tmp6):
        TRAGET_ONT_LINE_NAME.append(
            re.findall('ont-lineprofile-name ".*?"', tmp6)
        )
        # 遍历列表取线路模板
    if re.search('ont-srvprofile-name ".*?"', tmp6):
        TRAGET_ONT_SRV_NAME.append(
            re.findall('ont-srvprofile-name ".*?"', tmp6)
        )
        # 遍历列表取业务模板
    if re.search('traffic-table name ".*?"', tmp6):
        TRAGET_SRV_SRVTRAFFIC_NAME.append(
            re.findall('traffic-table name ".*?"', tmp6)
        )
        # 遍历列表取流量模板

# 读取模板并去重复 -----------------------
ALL_TARGET_PROFILE_NAME = []

for tmp7 in TRAGET_SRV_SRVTRAFFIC_NAME:
    if tmp7[0] not in ALL_TARGET_PROFILE_NAME and tmp7[0] == tmp7[1]:
        ALL_TARGET_PROFILE_NAME.append(tmp7[0])
    else:
        ALL_TARGET_PROFILE_NAME.append(tmp7[0])
        ALL_TARGET_PROFILE_NAME.append(tmp7[1])

for tmp7_1 in TRAGET_ONT_LINE_NAME:
    # TRAGET_ONT_SRV_NAME
    ALL_TARGET_PROFILE_NAME.append(tmp7_1)

for tmp7_1 in TRAGET_ONT_SRV_NAME:
    ALL_TARGET_PROFILE_NAME.append(tmp7_1)

# 读取模板并去重复 -----------------------

ALL_PFNAME_AND_CMD = []
for tmp8 in ALL_TARGET_PROFILE_NAME + ALLNEWCMD:
    if tmp8 not in ALL_PFNAME_AND_CMD:
        ALL_PFNAME_AND_CMD.append(tmp8)


def writenewinnervlan():
    '''写入剩余空闲内外层'''
    with open('inner-vlan.csv', 'w', encoding='UTF-8', newline='') as csv2file:
        # 把剩余的 内层vlan写入文件
        csvwriter = csv.writer(csv2file)
        csvwriter.writerows(INNER_VLAN_RE)


def writenewcmdfile():
    '''写入最终目标命令'''
    with open('commandlist.txt', 'w', encoding='UTF-8') as cmdfile:
        # 写入为命令列表
        for cmdlistnew in ALL_PFNAME_AND_CMD:
            cmdfile.writelines(str(cmdlistnew) + '\n')


writenewinnervlan()
writenewcmdfile()

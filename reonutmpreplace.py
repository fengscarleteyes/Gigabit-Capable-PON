# -*- coding:  utf-8 -*-
# Author: zhengyanfeng (fengscarleteyes, hongyan)
'''
初始化配置的源文件
替换线路模板业务模板流量模板
'''
import reonutmp
import reonureadold

ONT_LINE_TEMPLET_ID_NAME_LIST = reonutmp.ONT_LINE_KEY
# 读取线路模板id以及对应的名称
ONT_SRV_TEMPLET_ID_NAME_LIST = reonutmp.ONT_SRV_KEY
# 读取业务模板id以及对应的名称
TRAFFIC_TABLE_ID_NAME_LIST = reonutmp.TRAFFIC_TABLE_KEY
# 读取流量模板id以及对应的名称
# ---------------------修改onu add的链路模板和业务模板-------------------------
ONU_ADD_READOLD = reonureadold.ONU_ADD_CMD_OLD
# 读取reonureadold的onu添加命令
OND_ADD_REPLACE_LINE = []
OND_ADD_REPLACE_SRV = []
ONU_ADD_REPLACE_ALL = []
# 定义放置格式化后线路模板和业务模板的指令列表
for replace_var1 in ONU_ADD_READOLD:
    # 遍历ONU_ADD_READOLD列表,读取的仅onu添加的原本指令
    if 'ont-lineprofile-id' in replace_var1:
        # 当指令包含'ont-lineprofile-id'才执行替换
        tmp_var1 = 0
        while tmp_var1 < len(ONT_LINE_TEMPLET_ID_NAME_LIST):
            # while遍历ONT_LINE_TEMPLET_ID_NAME_LIST线路模板,
            if ONT_LINE_TEMPLET_ID_NAME_LIST[tmp_var1][0] in replace_var1:
                # 当线路模板的id条件存在,才替换为name
                tmp_str1 = replace_var1.replace(
                    ONT_LINE_TEMPLET_ID_NAME_LIST[tmp_var1][0],
                    ONT_LINE_TEMPLET_ID_NAME_LIST[tmp_var1][1]
                    )
                # 实现替换
            tmp_var1 += 1
    else:
        tmp_str1 = replace_var1
        # 否则如果不包含'ont-lineprofile-id'字样,则不替换,直接返回值
    OND_ADD_REPLACE_LINE.append(tmp_str1)
    # ONU_ADD_REPLACE_LINE最终将替换后的结果保存
for replace_var2 in OND_ADD_REPLACE_LINE:
    # 遍历OND_ADD_REPLACE_LINE这个已经替换线路模板的列表
    if 'ont-srvprofile-id' in replace_var2:
        # 继续判断'ont-srvprofile-id'是否存在,tmp_str1是在上一个替换循环中代表指令文本的变量名
        tmp_var2 = 0
        while tmp_var2 < len(ONT_SRV_TEMPLET_ID_NAME_LIST):
            # while循环读取ONT_SRV_TEMPLET_ID_NAME_LIST业务模板,
            if ONT_SRV_TEMPLET_ID_NAME_LIST[tmp_var2][0] in replace_var2:
                # 当业务模板的id条件存在时,才替换为name
                tmp_str2 = replace_var2.replace(
                    ONT_SRV_TEMPLET_ID_NAME_LIST[tmp_var2][0],
                    ONT_SRV_TEMPLET_ID_NAME_LIST[tmp_var2][1]
                    )
                # 实现替换
            tmp_var2 += 1
    else:
        tmp_str2 = replace_var2
        # 否则,如果不包含'ont-srvprofile-id',则不做改变
    OND_ADD_REPLACE_SRV.append(tmp_str2)
    # OND_ADD_REPLACE_SRV列表添加对应元素
ONU_ADD_REPLACE_ALL = OND_ADD_REPLACE_SRV
# ONU_ADD_REPLACE_ALL就是onu add 命令替换线路模板业务模板后的结果,用于调用
# ----------------------------修改service-port业务流的流量模板-------------------------
ONU_SERVICE_PORT_READOLD = reonureadold.ONU_SRV_CMD_OLD
# ONU_SERVICE_PORT_READOLD 读取reonureadold的业务流列表
ONU_SERVICE_PORT_REPLACE_ALL = []
# 创建空列表ONU_SERVICE_PORT_REPLACE_ALL,用于放置修改模板后的列表
for replace_var3 in ONU_SERVICE_PORT_READOLD:
    if 'traffic-table index' in replace_var3:
        tmp_var3 = 0
        tmp_str3 = replace_var3
        while tmp_var3 < len(TRAFFIC_TABLE_ID_NAME_LIST):
            if TRAFFIC_TABLE_ID_NAME_LIST[tmp_var3][0] in replace_var3:
                tmp_str3 = replace_var3.replace(
                    TRAFFIC_TABLE_ID_NAME_LIST[tmp_var3][0],
                    TRAFFIC_TABLE_ID_NAME_LIST[tmp_var3][1]
                    )
                # print('inb' + " " + tmp_str3)
            tmp_var3 += 1
    else:
        tmp_str3 = replace_var3
    ONU_SERVICE_PORT_REPLACE_ALL.append(tmp_str3)

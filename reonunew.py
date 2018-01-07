# -*- coding:  utf-8 -*-
# Author: zhengyanfeng (fengscarleteyes, hongyan)
'''
修改对应
'''
import re

import reonureadold
import reonutmpreplace


class TERMINALCMD(object):
    '''
    定义终端命令类
    '''
    def __init__(self, onuadd, onusrv, *onuother):
        '''
        初始化
            reonutmpreplace.ONU_ADD_REPLACE_ALL,
            reonutmpreplace.ONU_SERVICE_PORT_REPLACE_ALL,
        *onuother
            存放3个数组
            reonureadold.ONU_IP_CMD_OLD,
            reonureadold.ONU_ALARM_CMD_OLD,
            reonureadold.ONU_SNMP_CMD_OLD,
            reonureadold.ONU_NATIVE_CMD_OLD
        '''
        self.fttbonu = []
        # fttb的大onu命令,利用for循环添加关键字为snmp
        for tmpstrfttb in onuadd:
            if 'snmp' in tmpstrfttb:
                self.fttbonu.append(tmpstrfttb)
        # ftth家宽小onu命令,for添加 omci
        self.ftthonu = []
        for tmpstrftth in onuadd:
            if 'omci' in tmpstrftth:
                self.ftthonu.append(tmpstrftth)
        # normalsrv正常业务流包括宽带,电视,tr069
        # splsrv专线或其他业务流
        # fttbmngsrv大onu的管理业务流
        self.normalsrv = []
        self.splsrv = []
        self.fttbmngsrv = []
        srvnormal_pat = re.compile(' vlan ' + '[0-9]*')
        # 定义查找外层的正则表达式
        for tmpnmsrv in onusrv:
            tmpnmsrvfind = re.findall(srvnormal_pat, tmpnmsrv)
            # 遍历全部业务流
            if 'MANAGE' not in tmpnmsrv:
                # 排除fttb大onu的管理协议业务流
                if tmpnmsrvfind[0].endswith('0') or \
                        tmpnmsrvfind[0].endswith('1') or \
                        tmpnmsrvfind[0].endswith('6') or \
                        tmpnmsrvfind[0].endswith('8'):
                    # 增加正常业务流
                    self.normalsrv.append(tmpnmsrv)
                else:
                    # 否则添加为专线业务流
                    self.splsrv.append(tmpnmsrv)
            else:
                # 否则添加为大onu的管理业务流
                self.fttbmngsrv.append(tmpnmsrv)
        self.othercmd = onuother[0] + onuother[1] + onuother[2] + onuother[3]

    def cmdlen(self):
        '''
        待定
        '''
        pass

    def cmdlen1(self):
        '''
        待定
        '''
        pass


TERMINALCMD_CLASS = TERMINALCMD(
    reonutmpreplace.ONU_ADD_REPLACE_ALL,
    reonutmpreplace.ONU_SERVICE_PORT_REPLACE_ALL,
    reonureadold.ONU_IP_CMD_OLD,
    reonureadold.ONU_ALARM_CMD_OLD,
    reonureadold.ONU_SNMP_CMD_OLD,
    reonureadold.ONU_NATIVE_CMD_OLD
    )

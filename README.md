# 脚本说明

## 作者
Author: 郑艳烽 zhengyanfeng (fengscarleteyes, hongyan)

----

![spmoe.com](http://media.spmoe.com/LOGO.jpg)



## 致敬 [www.spmoe.com](http://www.spmoe.com/)

spmoe是一个乒乓球相关的分享网站！

向来到本站的各位看客致敬！

## 关于作为站长的我

白天是个上班狗，晚上是个休闲的乒乓球爱好者。

* 来自中国大地的南方，有着一群热爱着这项运动的小伙伴们。

我希望记录一些自己的所见所得分享一些精彩的比赛瞬间。

* 因为这些瞬间简单，美丽，精彩，引人入胜！

我讨厌一大串繁杂的的字眼，更喜欢直观的表达。

* 在这里,你只需要泡杯咖啡或者好茶一同品味乒乓。

----

## 个人信息

### 郑艳烽

* MAIL：fengscarleteyes#hotmail.com（把#换成@）
* PHONE：15916435511
* QQ：603024842

### 工作相关 2010 - 2017 

* 个人认证
  * Huawei Certified Network Professional HCNP
  * Digtal China Certified Technical Engineer 神州数码认证
  * 国家计算机软件资格水平认证中级网络工程师
  * National Computer Rank Visual Basic
  * CITT Level 4 Photoshop
* 工作经验
  * Sony VAIO Yangjiang Sales Director & technical manager
  * LENOVO Sales Director & technical manager
  * HP Sales Director & technical manager
  * Alibaba Tmall Taobao company support
  * China Mobile Metropolitan Area Network & Gpon support
* 现项目组
  * 中国移动城域网技术支撑(阳江)
    * 多年城域网运维经验
    * 涉及OLT,SW,SR,BNG,BAS等设备
    * 对口中国移动家宽以及城域网核心相关故障处理及网络优化

![jiangzhang](http://media.spmoe.com/jianlijiangzhang.png)

----

## 兴趣使然的开发者

学习 python 以及 markdown，有欣喜，也还有汗水。

作为历练，编写了适用于华为GPON设备间的用户数据互通割接程序，并持续更新。

并开源于OSCHINA的代码托管平台码云。

代码片段：

```python
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
```

![python](http://media.spmoe.com/python.png)

## 工作以外的兴趣

虽不好世俗烟酒，但和大多数普通人一样，我热爱音乐，热爱写作，热爱观赏体育赛事。

----

## 感激
感谢在我前进路上给予我历练的一切人与事，我仍将勇敢向前！

![hua](http://media.spmoe.com/hua.jpg)


----

## 本项目说明

* 脚本内容编码,以及对象文本编码需要均确保为UTF8

```5680
配置导出指令:
scroll
display current-configuration section global-config | include name
display current-configuration port */*/*
```

利用xshell或crt导出对应`.log`,存放至本软件根目录

## inner-vlan.csv

```python
PPPOE,1111,1
PPPOE,1111,2
PPPOE,1111,3
PPPOE,1111,4
PPPOE,1111,5
OTT,1116,1
OTT,1116,2
OTT,1116,3
OTT,1116,4
OTT,1116,5
TR069,1118,1
TR069,1118,2
TR069,1118,3
TR069,1118,4
TR069,1118,5
# csv为utf8编码
# 可从U2000导出已用内外层
# 通过excel得出空闲内外层后保存为对应名称csv
```

通过表格操作确认空闲的svlan和cvlan

## reonuimport.py 文件导入

导入文件数:

```python
file_name() # file_path() 无需参数,取出文件夹内'.log'文件名.
file_import() # file_import() 需要一个字符型的路径参数,并读取内容.
FILE_NAME_STR # 相对目录需要读取的文件名.
FILE_READ # 返回读取的文件内容.
cfg_old() # 返回读取的文件内容,作为方法调用.
```

* 每次只能导入一个PON口配置文件.
* 后缀名只能为'.log'.
* 若有2个以上'.log'文件,则打印'readme.md',并返回'readme.md'的路径.
* 若只有1个'.log'文件,则返回该文件路径.

读取文件夹中的'.log'文件

* 编码为utf8.
* 通过路径函数 file_path() 作为路径,读取整个文件的文本内容.
* 通过 file_import() 函数返回文本内容.

## reonureadold.py 格式化原OLTpon口配置数据

格式化文本:

```python
re_onu_pool(str_var1) # 需要一个文本参数,筛选出文本内的onu add字符,涉及onu的添加命令.
re_srv_pool(str_var2) # 需要一个文本参数,筛选出文本内的service-port的添加命令相关字符.
re_onu_ip(str_var4) # 需要一个文本参数,筛选出文本内的onu的ip配置相关字符.
re_onu_alarm(str_var5) # 需要一个文本参数,筛选出文本内的onu的告警模板相关字符.
re_onu_snmp(str_var6) # 需要一个文本参数,筛选出文本内的onu简单网络管理协议snmp相关字符.
re_onu_native(str_var7) # 需要一个文本参数,筛选出文本内的onu相关的native vlan配置.
ALLONU_STR # 赋值为读取出原配置文件的文本.
ONU_ADD_CMD_OLD # 筛选并赋值为仅添加onu的相关命令,无其他.
ONU_SRV_CMD_OLD # 筛选并赋值为仅添加srv的业务流添加相关命令,无其他.
ONU_IP_CMD_OLD # 筛选并赋值为仅onu的IP地址相关命令,无其他.
ONU_ALARM_CMD_OLD # 筛选并赋值为仅onu的告警模板相关命令,无其他.
ONU_SNMP_CMD_OLD # 筛选并赋值为仅onu的snmp协议相关命令,无其他.
ONU_NATIVE_CMD_OLD # 筛选并赋值为仅添加onu的native vlan 相关命令,无其他.
ONU_ALL_CMD_OLD # 为筛选并排序后的文本,格式化后的最终结果.
cfg_str_init() # 作为方法调用,返回格式化后的最终结果.
```

* 通过自定义函数，使用正则表达式筛选出对应的指令块.
* 将自定义函数得出的列表，赋值到对应的变量.
* 最终定义一个变量合并所有列表.

## reonutmp.py 读取配置数据相关的线路,流量,业务模板

```python
re_onu_line(str_var_1) # 需要一个文本参数,正则表达式取出onu线路模板.
re_onu_srv(str_var_2) # 需要一个文本参数,正则表达式取出onu业务模板.
re_traffic_table(str_var_3) # 需要一个文本参数,正则表达式取出流量模板.
onu_line_id_to_name(str_var_4) # 需要一个文本参数,正则表达式取出线路模板的id和name,返回一个数组,分别是 命令对应id 和命令对应名称,目的用来增加一个对应的列表以name命令替换id命令
onu_srv_id_to_name(str_var_5) # 需要一个文本参数,功能实现同上,对业务模板操作.
traffic_id_to_name(str_var_6) # 需要一个文本参数,功能实现同上,对流量模板操作.
ONT_LINE_VAR # 线路模板列表
ONT_SRV_VAR # 业务模板列表
TRAFFIC_TABLE_VAR # 流量模板列表
ONT_LINE_KEY # 用于存放配置文件读取出的线路模板id,以及对应名称
ONT_SRV_KEY # 存放配置文件读取出的业务模板id,以及对应名称
TRAFFIC_TABLE_KEY # 存放配置文件读取出的流量模板id,以及对应名称
```

* 通过自定义函数，使用正则表达式筛选出对应的指令块.
* 将自定义函数得出的列表，赋值到对应的变量.

## reonutmpreplace.py 替换' onu add '命令的线路模板,业务模板

```python
ONT_LINE_TEMPLET_ID_NAME_LIST # 读取线路模板id以及对应的名称
ONT_SRV_TEMPLET_ID_NAME_LIST # 读取业务模板id以及对应的名称
TRAFFIC_TABLE_ID_NAME_LIST # 读取流量模板id以及对应的名称
ONU_ADD_READOLD # 读取reonureadold的' onu add '命令对应组
ONU_ADD_REPLACE_ALL # 定义放置格式化(替换)线路模板和业务模板后的指令列表
ONU_SERVICE_PORT_REPLACE_ALL # 放置格式化(替换)流量模板后的业务流指令列表
```

## reonunew.py

```python
class TERMINALCMD(object):
# 定义类
# 类的2个自定义方法为pass
# 待定为计算命令行数功能
# 待补完
TERMINALCMD_CLASS # TERMINALCMD_CLASS 为继承TERMINALCMD_CLASS类
self.fttbonu # 大U add
self.ftthonu # 小U add
self.normalsrv # 普通业务流 家宽 电视 TR069
self.splsrv # 专线业务流
self.fttbmngsrv # 大U管理业务流
self.othercmd # 其他指令: 
            reonureadold.ONU_IP_CMD_OLD,
            # 原PON口的大U的IP地址
            reonureadold.ONU_ALARM_CMD_OLD,
            # 原PON口的onu告警模板
            reonureadold.ONU_SNMP_CMD_OLD,
            # 原PON口的网管snmp模板
            reonureadold.ONU_NATIVE_CMD_OLD
            # 原PON口的NATIVE-vlan相关
```

## reonutarget.py

```python
def getsolt():
    '''获取槽号'''
def getpon():
    '''获取端口号'''
# 读取文件,获得所有空闲内外层
TARGET_INNER_VLAN = []
# 宽带内外层
PPPOE_VLAN = []
# 电视内外层
OTT_VLAN = []
# tr069内外层

# FTTBONU_TARGET_CMD_LIST
# FTTBMNGSRV_TARGET_CMD_LIST
# FTTHONU_TARGET_CMD_LIST
# SPLSRV_TARGET_CMD_LIST
# NORMALSRV_TARGET_CMD_LIST

ALL_PFNAME_AND_CMD = []
# 全命令 含对应模板名 的列表

def writenewinnervlan(): # 将剩余空闲内外层写入到文件
def writenewcmdfile(): # 输出ALL_PFNAME_AND_CMD 模板和指令列表到文件
```

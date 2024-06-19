#coding: utf-8
'''************************************************************************
    > File Name: config.py
    > Author: mbinary
    > Mail: zhuheqin1@gmail.com 
    > Created Time: Fri 06 Apr 2018 11:06:16 AM DST
 ************************************************************************'''

# python变量 配置参数

'''
CSDN_AUTH_DATA ,CSDN_COOKIE 至少选一个配置
 CSDN_AUTH_DATA  使用api 来发送p博客,
     需要在http://open.csdn.net/wiki/api/ 注册开发者,得到cliet_id 和 client_secret
 CSDN_COOKIE 在发博客页面获取cookie,
'''
CSDN_AUTH_DATA = {'client_id' :'***',# 需填
               'client_secret': '***',# 需填
               'grant_type': 'password', # 不需要改
               'username': 'marvellousbinary',#改成自己的用户名
               'password': '***' #需填
                }
'''
通过浏览器,打开发送博客的页面https://mp.csdn.net/mdeditor
然后F12,在network中的第一个页面中复制cookie  str 
可参考这篇文章https://blog.csdn.net/marvellousbinary/article/details/79832708
'''
CSDN_COOKIE = '''
              uuid_tt_dd=10_19725690000-1700653000009-254449; UN=qq_47085173; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22qq_47085173%22%2C%22scope%22%3A1%7D%7D; cf_clearance=Eoxu10syt.vHUvvlI5c12B6MXtx3c1WjIcwc3boz2Kg-1713778634-1.0.1.1-rHesJ6EwziZS8vs1_SClP7D04RyHNunslA2oNXxQhUKH76cJY35ZZm4hbw1b8XNKpD1TnEfr9Hh42Y69GvsOYg; c_adb=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1714017626,1714980465,1716272810,1716445042; cf_clearance=mJrQ6wIFVIWHUEhgXOZHAFePoAfbkhBAiqbPFIx61eU-1716445041-1.0.1.1-re0G.0Ezp6LyrVlb._sZ4Vv2e3peZMFN8bSicxbCsrYnY5Ia7RoJdEgA_8VepyAHaYEMADzOfGKkeFKCD.oU_g; loginbox_strategy=%7B%22taskId%22%3A317%2C%22abCheckTime%22%3A1716874725038%2C%22version%22%3A%22ExpA%22%2C%22nickName%22%3A%22LJY_LU%22%2C%22blog-threeH-dialog-expa%22%3A1716874725038%7D; UserName=qq_47085173; UserInfo=8cd025c0b0814c76a66bb5fd49630400; UserToken=8cd025c0b0814c76a66bb5fd49630400; UserNick=LJY_LU; AU=D23; BT=1716874744676; p_uid=U010000; c_dl_prid=-; c_dl_rid=1717044446823_220634; c_dl_fref=https://blog.csdn.net/weixin_39754267/article/details/110936682; c_dl_fpage=/download/wazjajl/1293176; c_dl_um=-; AMP_MKTG_79fa01af82=JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmNuLmJpbmcuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMmNuLmJpbmcuY29tJTIyJTdE; AMP_79fa01af82=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5MWNiMmQ2NC03YmE1LTRkZmEtYjJjYi1mNTM1NWE1MjdjOTAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJMSlklMjBMdSUyMCU0MHBYVkNKOS5leUpsYldGcGJDSTZJbXhxZVd4MWMyTXlRR2R0WVdsc0xtTnZiU0lzSW1Ob1pXTnJjM1Z0SWpvaVlYbGxPR1lpTENKcFlYUWlPakUzTVRnd056TTJNVFFzSW1WNGNDSTZNVGN5TXpJMU56WXhOSDAuUzlxbnE3Z3lndXZHOUNGXzZzelE3a2gyNXE5dzZlVXFsODROcmxQVUhqRSUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE3MTgxMDQwNDg2MzUlMkMlMjJvcHRPdXQlMjIlM0FmYWxzZSU3RA==; firstDie=1; dc_sid=b150127c9aedf9f19c5ba39c75de6fde; c_segment=1; dc_session_id=10_1718789974130.407075; redpack_close_time=1; log_Id_click=82; x_dev_cloud_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcmVkZW50aWFsIjoiIiwiY3NkblVzZXJuYW1lIjoicXFfNDcwODUxNzMiLCJ1c2VySWQiOiI2MmQ2NmU5Yzk5ZWFiODVhYmQyMzQzZWQiLCJ1c2VybmFtZSI6InFxXzQ3MDg1MTczIn0._hDrUqy2r_34qqufwlcF_izNWa1FpFwAOqquOiYoS-w; c_ins_prid=-; c_ins_rid=1718790956052_423333; c_ins_fref=https://www.bing.com/; c_ins_fpage=/index.html; c_ins_um=-; ins_first_time=1718791001068; x_inscode_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcmVkZW50aWFsIjoiIiwiY3NkblVzZXJuYW1lIjoicXFfNDcwODUxNzMiLCJ1c2VySWQiOiI2MmQ2NmU5Yzk5ZWFiODVhYmQyMzQzZWQiLCJ1c2VybmFtZSI6InFxXzQ3MDg1MTczIn0._hDrUqy2r_34qqufwlcF_izNWa1FpFwAOqquOiYoS-w; c_pref=default; c_ref=default; c_first_ref=default; c_page_id=default; log_Id_pv=219; c_first_page=https%3A//mp.csdn.net/mdeditor; c_dsid=11_1718792361110.447133; creativeSetApiNew=%7B%22toolbarImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20231011044944.png%22%2C%22publishSuccessImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20240229024608.png%22%2C%22articleNum%22%3A0%2C%22type%22%3A0%2C%22oldUser%22%3Afalse%2C%22useSeven%22%3Atrue%2C%22oldFullVersion%22%3Afalse%2C%22userName%22%3A%22qq_47085173%22%7D; log_Id_view=6721; dc_tos=sfbop3
              '''

# 使用markdown 语法, 需pip install markdown
MDON  = False 


# default configuration
DEFAULT_DATA={
             "title":"do you know my name?",
             "markdowncontent":'# hello, world~',
             "content": '''<h1>hello, world~</h1>''',
             "categories":"默认分类",
              'tags':'leetcode,python,algorithm',
              'channel':33,
              'articleedittype':'1',
              'type':'original',
              'status':0,
            'type':'original', #original原创 report转载 translated 翻译
             "private":'0'
             #"id": 0    # int 修改已有文章
             }


             
'''
channel  各个值的含义
1:移动开发  
2:云计算大数据 
3:研发管理 
6:数据库
12:运维
14:前端
15:架构
16:编程语言
28:人工智能
29:物联网
30:游戏开发
31:后端
32:安全
33:程序人生
34:区块链
35:音视频开发
36:资讯
37:计算机理论与基础

'''      
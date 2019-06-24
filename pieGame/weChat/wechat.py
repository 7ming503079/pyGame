import itchat,time

# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
# @itchat.msg_register(itchat.content.PICTURE)
# def print_content(msg):
#     print(msg['Text'])
# @itchat.msg_register(itchat.content.RECORDING)
# def print_content(msg):
#     print(msg['Text'])
# @itchat.msg_register(itchat.content.CARD)
# def print_content(msg):
#     print(msg['Text'])

itchat.auto_login(hotReload=True)
name = itchat.search_friends(name=u'谷明丰')
# name = itchat.search_friends(name=u'吕世洋')
print(name)
XiaoMing = name[0]["UserName"]
print(XiaoMing)
for i in range(10):
    itchat.send(u'世洋你好，中午吃的好么？第'+str(i)+"遍",XiaoMing)
    time.sleep(1)
itchat.run()


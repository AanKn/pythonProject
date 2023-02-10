from tkinter import*
from urllib import request
from urllib import parse
import json
import hashlib


def translateWord(enstr):
    URL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    FormData = {}
    FormData['from'] = 'en'
    FormData['to'] = 'zh'
    FormData['q'] = enstr
    # 要翻译数据
    FormData['appid'] ='20230109001524599'
    # 申请的APPID
    FormData['salt'] = '123456789'
    Key = "viNhZF1cv26bnkpvbRMZ"
    # 平台分配的密钥
    m = FormData['appid']+enstr+FormData['salt']+Key
    print(m)
    m_MD5 = hashlib.md5(m.encode('utf8'))
    FormData['sign']=m_MD5.hexdigest()

    data = parse.urlencode(FormData).encode('utf-8')
    print(data)
    # 使用urlencode()方法转换标准格式#传递Request对象和转换完格式的数据
    response = request.urlopen(URL, data)
    print(response)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    print(translate_results)
    # 打印出JSON数据
    translate_results = translate_results['trans_result'][0]['dst']
    # 找到翻译结果
    print("翻译的结果是:%s" % translate_results)  # 打印翻译信息
    return translate_results


def leftClick1(event):
    enstr = Entry1.get()
    print(enstr)
    vText = translateWord(enstr)
    s.set('')
    Entry2.insert(0, vText)


def leftClick2(event):
    s.set('')
    s2.set('')


root = Tk()
root.title("单词翻译器")
root['width'] = 500
root['height'] = 250
Label(root, text='输入要翻译的内容:', width=15).place(x=1, y=1)  # 绝对坐标(1，1)
Label(root, text='翻译的结果:', width=10).place(x=1, y=20)  # 绝对坐标(1，1)
s = StringVar()
s2 = StringVar()
# s.set("大家好，这是测试")
Entry1 = Entry(root, width=50, textvariable=s2)
Entry1.place(x=110, y=1)  # 绝对坐标(110，1)Label(root,text='翻译的结果: ,width=18).place(x=l,y=20) #绝对坐标(1，20)#一个strinqVar()对象
Entry2 = Entry(root, width=50, textvariable=s)
Entry2.place(x=110, y=20)
# 绝对坐标(110，20)
Button1 = Button(root, text='翻译', width=8)
Button1.place(x=40, y=80)
Button2 = Button(root, text='清空', width=8)
Button2.place(x=110, y=80)  # 给 Button 绑定鼠标监听事件
# 绝对坐标(40，80)
# 绝对坐标(110，80)
# “翻译”按钮#“清空”按钮



Button1.bind("<Button-1>", leftClick1)
Button2.bind("<Button-1>", leftClick2)
root.mainloop()

from telethon import TelegramClient, client, events
import time
import threading
import requests
import urllib
def check():
    my_ip = requests.get('https://api.ipify.org').text   # IP của máy
    listtk = []
    with urllib.request.urlopen('https://raw.githubusercontent.com/hoangks5/QLKH/main/forwardchanel.txt') as url:  # Url danh sách IP có thể sử dụng
        s = url.read()
        key = s.decode("utf-8")
        key = key.splitlines()
        for k in key:
            keyz = k.split(';')
            listtk.append(keyz[0])
    if my_ip not in listtk:
        while True:
            print('Key lỗi')
check()
f = open('setting/setting.txt','r',encoding='utf-8')
f = f.read()
f = f.split('#auto')
api_id =  8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'
acc = f[0]
client = TelegramClient(acc,api_id,api_hash)
chanlel = f[1]
linkgr = f[2]
time_leep = int(f[3])*60
try:
    linkgr = linkgr.split(';')
except:
    pass
chanlel = int('-100'+chanlel)
@client.on(events.NewMessage)
async def handler(envent):
    chat = await envent.get_chat()
    ttt = envent.raw_text
    chat_id = envent.chat_id
    if chat_id == chanlel:
        for gr in linkgr:
            await client.forward_messages(gr, envent.message)
        time.sleep(time_leep)
    else:
        pass

client.start()
client.run_until_disconnected()
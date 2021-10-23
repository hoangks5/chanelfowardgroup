from telethon import TelegramClient, client
import time
api_id =  8763319
api_hash = '28f53a40a4052cd950dab693a3a3c04c'
acc = input('Nhập tên acc: ')
id_chanel = input('Nhập id chanel(vd: 1731891326): ')
id_mess = input('Nhập id tin nhắn: ')
chat_id = int(id_chanel)
mess_id = int(id_mess)
linkgr = input('Nhập link group chuyển tiếp(cách nhau bởi dấu ; vd: https://t.me/laucua;https://t.me/laucu) :')
time_leep = int(input('Thời gian chờ tin nhắn(phút): '))*60
id_chanel = int('-100'+id_chanel)
try:
    linkgr = linkgr.split(';')
except:
    pass
while True:
    client = TelegramClient(acc,api_id,api_hash)
    async def main():
            for gr in linkgr:
                await client.forward_messages(gr,int(id_mess),id_chanel)
    with client:
        client.loop.run_until_complete(main())
    client.disconnect()
    time.sleep(time_leep)


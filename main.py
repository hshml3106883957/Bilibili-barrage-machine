#by hshml123
from mcrcon import *
from bilibili_api import Credential, Danmaku, sync
from bilibili_api.live import LiveDanmaku, LiveRoom
from tkinter import *


def start():
    sessdata = sessdata_get.get()
    bili_jct = bili_jct_get.get()
    ROOMID = int(roomid.get())
    RCON_IP = rconip.get()
    RCON_PASSWORD = password.get()
    RCON_PORT = port.get()
    root.destroy()
    credential = Credential(
        sessdata=f"{sessdata}",
        bili_jct=f"{bili_jct}"
    )

    monitor = LiveDanmaku(ROOMID, credential=credential)
    sender = LiveRoom(ROOMID, credential=credential)
    UID = sync(sender.get_room_info())["room_info"]["uid"]

    @monitor.on('SEND_GIFT')
    async def on_gift(event):
        # 收到礼物
        print(event)
        with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as rcon:
            response = rcon.command(
                f'/tellraw @a "                             \u00A7a[直播礼物] \u00A76感谢老板的{event}"')

    @monitor.on("DANMU_MSG")
    async def recv(event):
        # 发送者UID
        uid = event["data"]["info"][2][0]
        # 排除自己发送的弹幕
        # 弹幕文本
        msg = event["data"]["info"][1]
        print(msg)
        with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as rcon:
            response = rcon.command(f'/tellraw @a "                             \u00A7a[直播弹幕] \u00A76{msg}"')

    sync(monitor.connect())


root = Tk()
root.title("B站弹幕机->我的世界")
root.geometry("200x300")
text = Label(root, text="请输入b站'sessdata'")
text.pack()
sessdata_get = Entry(root)
sessdata_get.pack()
text1 = Label(root, text="请输入B站'bili_jct'")
text1.pack()
bili_jct_get = Entry(root)
bili_jct_get.pack()
text2 = Label(root, text="请输入B站直播间ID")
text2.pack()
roomid = Entry(root)
roomid.pack()
text3 = Label(root, text="请输入我的世界RCON-IP")
text3.pack()
rconip = Entry(root)
rconip.pack()
text4 = Label(root, text="请输入我的世界RCON密码")
text4.pack()
password = Entry(root)
password.pack()
text5 = Label(root, text="请输入我的世界RCON端口")
text5.pack()
port = Entry(root)
port.pack()
button = Button(root, text="确认", command=start)
button.pack()
root.mainloop()

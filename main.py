# --*-- coding=utf-8 --*--
import requests
import os
import time


def getversion():
    # *先将verjson给全局化
    global verjson
    # *获取配置
    response = requests.get(
        "https://cdn.jsdelivr.net/gh/misaka10843/genshin-server-switching@2.0/ver.json", timeout=30)
    # !简要判断是否服务器无法连接
    if response.status_code == 200:
        # *将api解析成json
        verjson = response.json()
    else:
        print("中国镜像加速源似乎崩溃了，我们将直接从github获取qwq\n")
        verjson = requests.get(
            "https://raw.githubusercontent.com/misaka10843/genshin-server-switching/2.0/ver.json")


def get_game_path():
    global path
    path = "null"
    if(os.path.exists("./path.txt")):
        with open('./path.txt', 'r') as f:
            path = f.read()  # 读取路径
    if(path == "null"):
        path = input(
            "请输入您的'Genshin Impact Game'文件夹的路径(如:E:\Genshin Impact\Genshin Impact Game)\n")
        if(os.path.exists(path+"/YuanShen.exe") and os.path.exists(path+"/config.ini") and os.path.exists(path+"/mhyprot2.Sys")):
            path = path.replace('\\', '/')
            print("我们已经找到了您的游戏文件啦！")
            with open('./path.txt', 'w+') as f:
                f.write(path)  # 将路径写入文件


def iniget():
    global isserver
    print(path)
    with open(path+"/config.ini", "r") as f:
        f = f.read()
        bili = f.find('bilibili')
        mihoyo = f.find('mihoyo')
    if (bili < 0):
        print("您现在所在mihoyo服务器中,我们将更换到bilibili服务器中")
        isserver = "bili"
    elif (mihoyo < 0):
        print("您现在所在bilibili服务器中,我们将更换到mihoyo服务器中")
        isserver = "mihoyo"


def inichange():
    if(isserver == "bili"):
        with open(path+"/config.ini", 'w+') as f:
            # 将路径写入文件
            f.write(
                "[General]\r\nchannel=%s\r\ncps=%s\r\ngame_version=%s\r\nsdk_version=\r\nsub_channel=%s" % (verjson["bili_channel"], verjson["bili_cps"], verjson["game_version"], verjson["bili_sub_channel"]))
        print("已经从mihoyo服务器转接到bilibili服务器啦！")
    elif(isserver == "mihoyo"):
        with open(path+"/config.ini", 'w+') as f:
            # 将路径写入文件
            f.write(
                "[General]\r\nchannel=%s\r\ncps=%s\r\ngame_version=%s\r\nsdk_version=\r\nsub_channel=%s" % (verjson["mihoyo_channel"], verjson["mihoyo_cps"], verjson["game_version"], verjson["mihoyo_sub_channel"]))
        print("已经从bilibili服务器转接到mihoyo服务器啦！")
    isopen = input("是否打开原神?(0:是,1:否,默认0)\n")
    if(isopen == "1"):
        print("好吧，那我就关闭啦！(*/ω＼*)")
        time.sleep(3)
        exit()
    else:
        os.system("\""+path+"/YuanShen.exe\"")
        time.sleep(3)
        exit()


if __name__ == "__main__":
    print("欢迎使用原神快速换服程序qwq\n")
    getversion()
    get_game_path()
    iniget()
    inichange()

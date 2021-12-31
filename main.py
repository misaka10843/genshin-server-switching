# --*-- coding=utf-8 --*--
import requests
import os
import time


def getversion():
    # *先将verjson给全局化
    global verjson
    # *获取配置

    response = requests.get(
        "https://gitee.com/misaka10843/genshin-server-switching/raw/2.0/ver.json", timeout=30)
    # !简要判断是否服务器无法连接
    if response.status_code == 200:
        # *将api解析成json
        verjson = response.json()
        print("github/gitee库中的配置文件游戏版本信息为:" +
              verjson["game_version"]+"\n如果与最新游戏版本请前往Github发送issue,感谢支持与维护！")
    else:
        print("gitee都无法访问,您的网络似乎有重大问题?\n请检查您的网络后重试\n")
        time.sleep(3)
        exit()


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
        else:
            print("您似乎写错了路径?我们重来一遍吧！")
            get_game_path()


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
        # *查找是否有PCGameSDK.dll(B站的SDK)
        if not (os.path.exists(path+"/YuanShen_Data/Plugins/PCGameSDK.dll")):
            getSDK()

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


def getSDK():
    print("downloading PCGameSDK.dll")
    url = 'https://raw.fastgit.org/misaka10843/genshin-server-switching/2.0/PCGameSDK.dll'
    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        with open(path+"/YuanShen_Data/Plugins/PCGameSDK.dll", "wb") as code:
            code.write(r.content)
        print("download PCGameSDK.dll complete")
    else:
        print("我们似乎无法获取b站的SDK,还请您检查您的网络,非常感谢！\n或者您从GitHub库中下载PCGameSDK.dll后放入您游戏文件夹中的YuanShen_Data/Plugins文件夹中即可")
        time.sleep(3)
        exit()


if __name__ == "__main__":
    print("欢迎使用原神快速换服程序qwq\n我们现在准备获取配置信息,请稍后!")
    getversion()
    get_game_path()
    iniget()
    inichange()

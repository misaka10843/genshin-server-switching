# --*-- coding=utf-8 --*--
import os
import time
from shutil import copyfile

import requests
import urllib3


def getversion():
    # *先将VerJson给全局化
    global VerJson
    # *获取配置

    response = requests.get(
        "https://gitee.com/misaka10843/genshin-server-switching/raw/2.0/ver.json", timeout=30)
    # !简要判断是否服务器无法连接
    if response.status_code == 200:
        # *将api解析成json
        VerJson = response.json()
        print("github/gitee库中的配置文件游戏版本信息为:" +
              VerJson["game_version"] + "\n如果与最新游戏版本请前往Github发送issue,感谢支持与维护！")
    else:
        print("gitee都无法访问,您的网络似乎有重大问题?\n请检查您的网络后重试\n")
        time.sleep(3)
        exit()


def get_game_path():
    global path
    path = "null"
    if os.path.exists("./path.txt"):
        with open('./path.txt', 'r') as f:
            path = f.read()  # 读取路径
    if path == "null":
        path = input(
            "请输入您的'Genshin Impact Game'文件夹的路径(如:E:\Genshin Impact\Genshin Impact Game)\n")
        if os.path.exists(path + "/YuanShen.exe") and os.path.exists(path + "/config.ini") and os.path.exists(
                path + "/mhyprot2.Sys"):
            path = path.replace('\\', '/')
            print("我们已经找到了您的游戏文件啦！")
            # 启动备份
            backup()
            with open('./path.txt', 'w+') as f:
                f.write(path)  # 将路径写入文件
            # 备份用户替换数据以防止无法进入游戏

        else:
            print("您似乎写错了路径?我们重来一遍吧！")
            get_game_path()


def iniget():
    global ToServer
    print(path)
    with open(path + "/config.ini", "r") as f:
        f = f.read()
        bili = f.find('bilibili')
        mihoyo = f.find('mihoyo')
    if bili < 0:
        print("您现在所在mihoyo服务器中,我们将更换到bilibili服务器中")
        ToServer = "bili"
    elif mihoyo < 0:
        print("您现在所在bilibili服务器中,我们将更换到mihoyo服务器中")
        ToServer = "mihoyo"


def inichange():
    if ToServer == "bili":
        # *查找是否有PCGameSDK.dll(B站的SDK)
        if not (os.path.exists(path + "/YuanShen_Data/Plugins/PCGameSDK.dll")):
            getSDK()

        with open(path + "/config.ini", 'w+') as f:
            # 将路径写入文件
            f.write(
                "[General]\r\nchannel=%s\r\ncps=%s\r\ngame_version=%s\r\nsdk_version=%s\r\nsub_channel=%s" % (
                    VerJson["bili_channel"], VerJson["bili_cps"], VerJson["game_version"], VerJson["bili_SDK"],
                    VerJson["bili_sub_channel"]))
        print("已经从mihoyo服务器转接到bilibili服务器啦！")
    elif ToServer == "mihoyo":
        if os.path.exists(path + "/YuanShen_Data/Plugins/PCGameSDK.dll"):
            os.remove(path + "/YuanShen_Data/Plugins/PCGameSDK.dll")
        with open(path + "/config.ini", 'w+') as f:
            # 将路径写入文件
            f.write(
                "[General]\r\nchannel=%s\r\ncps=%s\r\ngame_version=%s\r\nsdk_version=\r\nsub_channel=%s" % (
                    VerJson["mihoyo_channel"], VerJson["mihoyo_cps"], VerJson["game_version"],
                    VerJson["mihoyo_sub_channel"]))
        print("已经从bilibili服务器转接到mihoyo服务器啦！")
    isopen = input("是否打开原神?(0:是,1:否,默认0)\n(因为更改了服务器,所以您可能需要打开后关闭再打开才能生效!)")
    if isopen == "1":
        print("好吧，那我就关闭啦！(*/ω＼*)")
        time.sleep(3)
        exit()
    else:
        os.system("\"" + path + "/YuanShen.exe\"")
        time.sleep(3)
        exit()


def getSDK():
    print("downloading PCGameSDK.dll")
    url = 'https://gitee.com/misaka10843/genshin-server-switching/raw/2.0/bili_Config/PCGameSDK.dll'
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    with open(path + "/YuanShen_Data/Plugins/PCGameSDK.dll", "wb") as code:
        code.write(response.data)
    print("download PCGameSDK.dll complete")
    response.release_conn()


def getSDK_pkg():
    print("downloading SDK_pkg_version")
    url = 'https://gitee.com/misaka10843/genshin-server-switching/raw/2.0/bili_Config/sdk_pkg_version'
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    with open(path + "/sdk_pkg_version", "wb") as code:
        code.write(response.data)
    print("download SDK_pkg_version complete")
    response.release_conn()


def backup():
    print("正在备份您的原始游戏配置文件....")
    DllPath = path + "/YuanShen_Data/Plugins/PCGameSDK.dll"
    BackupPath = path + "/backup/"
    IniPath = path + "/config.ini"
    if not os.path.exists(path + "/backup/"):
        os.makedirs(BackupPath)
    # 复制dll
    if os.path.exists(DllPath):
        copyfile(DllPath, BackupPath)
    # 复制ini
    copyfile(DllPath, IniPath)
    print(
        "\n如果您无法进入游戏或者有其他bug，\n您可以在游戏目录下的backup文件夹找到备份文件并替换\n(如果是官服请注意YuanShen_Data/Plugins下有没有PCGameSDK.dll，如有请删除)\n")


if __name__ == "__main__":
    print("欢迎使用原神快速换服程序qwq\n我们现在准备获取配置信息,请稍后!")
    getversion()
    get_game_path()
    iniget()
    inichange()

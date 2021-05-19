// genshin.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include<iostream>
#include<fstream>
#include <WINDOWS.H>
#include <string>
using namespace std;


int main()
{
	char server;
	bool Isbili = false;
	fstream fin1("config.ini", ios::in);	//读取配置文件
	if (!fin1)
	{
		cout << "我们并未读取到您的原神配置文件\n" << "1.您确定将程序及两个配置文件夹放到游戏目录下了吗？\n" << "2.您是否删除了配置文件？(如果是这种情况请不用担心，我们会新建一个配置文件)" << "\n\n" << endl;
	}

	fstream fin2("biliserver/config.ini");		//读取两个服务器的配置文件
	fstream fin3("mihoyoserver/config.ini");
	//判断是否有这两个配置文件
	if (!fin2) {
		cout << "已找到原神的配置文件，但未找到biliserver下的配置文件，请检查您是否将biliserver文件夹放入游戏根目录，或者您是否下载了此文件夹(建议直接下载tag中的zip后直接解压到游戏根目录)..." << "\n\n" << endl;
		if (!fin3) {
			cout << "已找到原神的配置文件，但未找到mihoyoserver下的配置文件，请检查您是否将mihoyoserver文件夹放入游戏根目录，或者您是否下载了此文件夹(建议直接下载tag中的zip后直接解压到游戏根目录)..." << "\n\n" << endl;
		}
		system("pause");
		return -1;
	}
	else {
		cout << "已找到原神、biliserver、mihoyoserver的配置文件，正在获取配置中..." << "\n\n" << endl;
	}

	fin1.get(server);		//判断现在客户端服务器类型
	{
		if (server == 'bili') {
			Isbili = true;
			cout << "我们读取到您的原神是bilibili服务器的，建议替换成mihoyo服务器" << "\n\n" << endl;
		}
		else {
			cout << "我们读取到您的原神是mihoyo服务器的，建议替换成bilibili服务器" << "\n\n" << endl;
		}
	}
	/*有bug的检测版本模块
	char ver;
	fin1.get(ver);
	if (ver == '1.5') {
	}
	else {
		cout << "您好像不是1.5.0版本的，如果您是1.6.0版本还请去github下载最新替换器\n" << "链接：https://github.com/misaka10843/genshin-server-switching" << "\n\n" << endl;
		system("pause");
		return -1;
	}
	*/
	fin1.close();

	int a;
	cout << "您需要游玩哪一个服务器？\n" << "1：bilibili服务器，2：mihoyo服务器" << endl;
	//如果是bilibili的服务器就会显示bilibili为默认服务器，如果不是就显示官方服务器是默认服务器
	if (Isbili == true) {
		cout << "(bilibili为默认服务器)" << "\n\n" << endl;
	}
	else {
		cout << "(MiHoYo为默认服务器)" << "\n\n" << endl;
	}
	cin >> a;		//检测用户选择
	if (a == 1) {
		cout << "正在复制配置文件..." << "\n\n" << endl;
		char const * source = "biliserver//config.ini";
		char const * destination = "config.ini";
		CopyFile(source, destination, false);		//复制配置文件
		cout << "复制完成！\n" << "5秒后进行执行打开任务\n" << "如果出现“允许此应用进行更改吗？”请选是" << endl;
		Sleep(5000);
		system("start YuanShen.exe");	//打开原神

	}
	else {
		cout << "正在复制配置文件..." << "\n\n" << endl;
		char const * source = "mihoyoserver//config.ini";
		char const * destination = "config.ini";
		CopyFile(source, destination, false);
		cout << "复制完成！\n" << "5秒后进行执行打开任务\n" << "如果出现“允许此应用进行更改吗？”请选是" << endl;
		Sleep(5000);
		system("start YuanShen.exe");

	}
	return 0;
}

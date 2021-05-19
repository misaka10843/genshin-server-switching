/*
 * genshin.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
 *
 */

#include <iostream>
#include <fstream>
#include <WINDOWS.H>
#include <string>
using namespace std;


int main()
{
	bool Isbili = false;


	/*****************************
	 *
	 * 匹配文件、检测文件   开始
	 *
	 ******************************/

	/*算法非常的通俗qwq，因为测试了用if else有bug，所以只能一个判断读取一次文件了qwq*/
	char line[256] = { 0 };

	ifstream	mihoyo("../Genshin Impact Game/config.ini");
	ifstream	assest("../Genshin Impact Game/YuanShen_Data/resources.assets");
	/* 判断是否有原配置文件 */
	if (!mihoyo)
	{
		/* 判断是否安装原神或者路径出错 */
		if (!assest)
		{
			cout << "我们并未读取到您的原神配置文件\n" << "因为您没有安装原神，或者没有放置在游戏的上一级目录的子目录中（与游戏根目录同级）" << "\n\n" << endl;
			system("pause");
			return(-1);
		}
		cout << "我们并未读取到您的原神配置文件\n" << "1.您确定将程序及两个配置文件夹放置在游戏的上一级目录的子目录中（与游戏根目录同级）了吗？\n" << "2.您是否删除了配置文件？(如果是这种情况请不用担心，我们会新建一个配置文件)" << "\n\n" << endl;
		system("pause");
		return(-1);
	}
	fstream fin2("biliserver/config.ini");               /* 读取两个服务器的配置文件 */
	fstream fin3("mihoyoserver/config.ini");
	/* 判断是否有这两个配置文件 */
	if (!fin2)
	{
		cout << "已找到原神的配置文件，但未找到biliserver下的配置文件，请检查您是否将biliserver文件夹放入游戏根目录，或者您是否下载了此文件夹(建议直接下载tag中的zip后直接解压到游戏根目录)..." << "\n\n" << endl;
		if (!fin3)
		{
			cout << "已找到原神的配置文件，但未找到mihoyoserver下的配置文件，请检查您是否将mihoyoserver文件夹放入游戏根目录，或者您是否下载了此文件夹(建议直接下载tag中的zip后直接解压到游戏根目录)..." << "\n\n" << endl;
		}
		system("pause");
		return(-1);
	}
	else {
		cout << "已找到原神、biliserver、mihoyoserver的配置文件，正在获取配置中..." << "\n\n" << endl;
	}
	fin2.close();
	fin3.close();

	/* 匹配是否为mihoyo服务器 */
	while (!mihoyo.eof())

	{
		mihoyo.getline(line, sizeof(line) - 1);

		if (strstr(line, "mihoyo") != NULL)

		{
			cout << "我们读取到您的原神是mihoyo服务器的，建议替换成bilibili服务器" << "\n\n" << endl;

			break;
		}
	}

	mihoyo.close();

	/* 匹配是否为bilibili服务器 */
	ifstream	bili("../Genshin Impact Game/config.ini");
	char		line1[256] = { 0 };
	while (!bili.eof())

	{
		bili.getline(line1, sizeof(line1) - 1);

		if (strstr(line1, "14") != NULL)

		{
			Isbili = true;
			cout << "我们读取到您的原神是bilibili服务器的，建议替换成mihoyo服务器" << "\n\n" << endl;

			break;
		}
	}

	bili.close();

	/* 匹配版本 */
	ifstream	Version("../Genshin Impact Game/config.ini");
	char		line2[256] = { 0 };
	bool		ver = true;
	while (!Version.eof())

	{
		Version.getline(line2, sizeof(line2) - 1);

		if (strstr(line2, "1.5.0") != NULL)

		{
			ver = false;

			break;
		}
	}
	if (ver == true)
	{
		cout << "您好像不是1.5.0版本的，如果您是1.6.0版本还请去github下载最新替换器\n" << "链接：https://github.com/misaka10843/genshin-server-switching" << "\n\n" << endl;
		system("pause");
	}

	Version.close();


	/*****************************
	 *
	 * 匹配文件、检测文件   结束
	 *
	 ******************************/


	 /******************************************
	 *
	 *  玩家交互、复制配置文件、打开客户端   开始
	 *
	 ******************************************/
	int a;
	cout << "您需要游玩哪一个服务器？\n" << "1：bilibili服务器，2：mihoyo服务器" << endl;
	/* 如果是bilibili的服务器就会显示bilibili为默认服务器，如果不是就显示官方服务器是默认服务器 */
	if (Isbili == true)
	{
		cout << "(bilibili为默认服务器)" << "\n\n" << endl;
	}
	else {
		cout << "(MiHoYo为默认服务器)" << "\n\n" << endl;
	}
	cin >> a; /* 检测用户选择 */
	if (a == 1)
	{
		/*复制配置文件（这是我在google找到的最有效方法了QWQ） */
		char		sourcename[80] = "./biliserver/config.ini", destname[80] = "../Genshin Impact Game/config.ini", buffer[256];
		int		n;
		ifstream	in(sourcename, ios_base::in | ios_base::binary);
		ofstream	out(destname, ios_base::out | ios_base::binary);
		if (!in || !out)
		{
			cerr << "Open File Failure,Please Try Again!"; exit(1);
		}
		while (!in.eof())
		{
			in.read(buffer, 256); /* 从文件中读取256个字节的数据到缓存区 */
			n = in.gcount();        /* 由于最后一行不知读取了多少字节的数据，所以用函数计算一下。 */
			out.write(buffer, n); /* 写入那个字节的数据 */
		}
		in.close();
		out.close();
		cout << "复制完成！\n" << "5秒后进行执行打开任务\n" << "如果出现“允许此应用进行更改吗？”请选是" << endl;
		Sleep(5000);
		system("start \"caption\" \"..\\Genshin Impact Game\\YuanShen.exe\"");
	}
	else {
		char		sourcename[80] = "./mihoyoserver/config.ini", destname[80] = "../Genshin Impact Game/config.ini", buffer[256];
		int		n;
		ifstream	in(sourcename, ios_base::in | ios_base::binary);
		ofstream	out(destname, ios_base::out | ios_base::binary);
		if (!in || !out)
		{
			cerr << "Open File Failure,Please Try Again!"; exit(1);
		}
		while (!in.eof())
		{
			in.read(buffer, 256); /* 从文件中读取256个字节的数据到缓存区 */
			n = in.gcount();        /* 由于最后一行不知读取了多少字节的数据，所以用函数计算一下。 */
			out.write(buffer, n); /* 写入那个字节的数据 */
		}
		in.close();
		out.close();
		cout << "复制完成！\n" << "5秒后进行执行打开任务\n" << "如果出现“允许此应用进行更改吗？”请选是" << endl;
		Sleep(5000);
		system("start \"caption\" \"..\\Genshin Impact Game\\YuanShen.exe\"");


		/******************************************
		*
		*  玩家交互、复制配置文件、打开客户端   结束
		*
		******************************************/
	}
	return(0);
}



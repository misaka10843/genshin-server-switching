#include<iostream>
#include<fstream>
#include <WINDOWS.H>
using namespace std ;

int main()
{
    SetConsoleOutputCP(65001);
    int a;
    cout << "您需要转到哪一个服务器？\n" << "1：bilibili服务器，2：mihoyo服务器" <<endl;
    cin >> a;
    if (a == 1){
        cout << "已经成功转到bilibili！" <<endl;
       char const * source = "biliserver//config.ini";
    char const * destination = "config.ini";
    CopyFile(source, destination, false);
        
    }else{
        cout << "已经成功转到miHoYo！" <<endl;
       char const * source = "mihoyoserver//config.ini";
    char const * destination = "config.ini";
    CopyFile(source, destination, false);
        
    }
    return 0;
}
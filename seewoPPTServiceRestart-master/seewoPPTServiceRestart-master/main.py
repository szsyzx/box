# coding: utf-8
# 希沃PPTService重启小程序 by Misaka-blog
import os
import winreg
import subprocess

# 通过读取本机注册表，获取希沃PPT小工具的安装位置
string = r'SOFTWARE\WOW6432Node\Seewo\PPTService'
handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
location, _type = winreg.QueryValueEx(handle, "ExePath")

# 调用系统命令，重启希沃PPT小工具
os.system('taskkill /f /im PPTService.exe')
subprocess.Popen(location)

# Goorm 搭建 xray vmess / vless 节点

使用goorm的免费ide，配合其alwayson功能和端口转发，实现xray代理服务

# 注：请勿在常用账号部署本项目
# 项目疑似被识别，请谨慎部署

![image](https://user-images.githubusercontent.com/96560028/171325273-bbccc70f-f275-47fc-a6eb-c36d5e7d0ab0.png)

![image](https://user-images.githubusercontent.com/96560028/171325137-22cbc6ed-6322-4a1a-8304-4ed026bbb302.png)

## 食用方法

博客图文教程：https://owo.misaka.rest/goormide-xray/

1. 注册并登录Goorm账号
2. 创建一个Container
3. 输入容器名称、选择地区，Slack选择blank，点击创建按钮创建容器

![](https://gcore.jsdelivr.net/gh/Misaka-blog/tuchuang@master/20220531052101.png)

![](https://gcore.jsdelivr.net/gh/Misaka-blog/tuchuang@master/20220531052141.png)

4. 输入以下命令

```shell
wget -N https://raw.githubusercontent.com/Misaka-blog/GX/master/misaka.sh && bash misaka.sh
```

5. 配置端口转发

![](https://gcore.jsdelivr.net/gh/Misaka-blog/tuchuang@master/20220531052447.png)

6. vmess / vless 配置如下

```
地址：IP
端口：转发的端口
默认UUID：8d4a8f5e-c2f7-4c1b-b8c0-f8f5a9b6c384
vmess额外id：0
加密：auto 或 none
传输协议：ws
伪装类型：none
```

IP被墙？关机，重启即可更换IP

## 免责声明

本项目仅为个人研究软件原理、效果之用，不对部署产生的任何后果负责

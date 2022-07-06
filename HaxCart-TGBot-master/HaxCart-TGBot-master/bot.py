# -*- coding: utf-8 -*-
import re

import requests
from bs4 import BeautifulSoup
from telegram.ext import CommandHandler, Updater

updater = Updater("<YOUR BOT TOKEN>", workers=128)
dispatcher = updater.dispatcher


class Hax:
    def check(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Content-type": "application/json",
        }
        datas = requests.get(url, headers=headers).text
        return datas

    def get_server_info(self):
        html_text = self.check("https://hax.co.id/data-center")
        soup = BeautifulSoup(html_text, "html.parser")
        zone_list = [x.text for x in soup("h5", class_="card-title mb-4")]
        sum_list = [x.text for x in soup("h1", class_="card-text")]
        vps_list = []
        vps_dict = {}
        vps_str = ""
        for k, v in zip(zone_list, sum_list):
            zone = k.split("-", 1)[0].lstrip("./")
            sum = (
                k.split("-", 1)[1] + "(" + v.rstrip(" VPS") + "♝)"
                if len(k.split("-", 1)) > 1
                else v
            )
            vps_list.append((zone, sum))
        for k_v in vps_list:
            k, v = k_v
            vps_dict.setdefault(k, []).append(v)
        for k, v in vps_dict.items():
            vps_str += ">>" + k + "-" + ", ".join(v) + "\n"
        return vps_str

    def get_data_center(self):
        html_text = self.check("https://hax.co.id/create-vps")
        soup = BeautifulSoup(html_text, "html.parser")
        ctr_list = [x.text for x in soup("option", value=re.compile(r"^[A-Z]{2,}-"))]
        vir_list = [(c.split(" (")[1].rstrip(")"), c.split(" (")[0]) for c in ctr_list]
        vir_dict = {}
        vir_str = ""
        for k_v in vir_list:
            k, v = k_v
            vir_dict.setdefault(k, []).append(v)
        for k, v in vir_dict.items():
            vir_str += "★" + k + "★ " + ", ".join(v) + "\n"
        return vir_str

    def main(self):
        vps_str = self.get_server_info()
        srv_stat = f"[🛰Server Stats / 已开通数据]\n{vps_str}\n"
        vir_str = self.get_data_center()
        data_center = f"[🚩Available Centers / 可开通区域]\n{vir_str}\n"
        msg = data_center
        return msg


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="欢迎使用Hax库存查询监控bot！\n我能够帮你拿到hax官网上的库存信息，并把他们发送到你的Telegram会话中\n输入 /help 获取帮助列表\nGithub: Misaka-blog    TG: @misakanetcn",
    )


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hax 库存查询监控BOT 帮助菜单\n/help 显示本菜单\n/get 获取当前库存情况\n/ping 检测bot存活状态",
    )


def ping(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Pong~")


def get(update, context):
    res = Hax().main()
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)


Start = CommandHandler("start", start, run_async=True)
Ping = CommandHandler("ping", ping, run_async=True)
Get = CommandHandler("get", get, run_async=True)
Help = CommandHandler("help", help, run_async=True)
dispatcher.add_handler(Ping)
dispatcher.add_handler(Start)
dispatcher.add_handler(Get)
dispatcher.add_handler(Help)

updater.start_polling()

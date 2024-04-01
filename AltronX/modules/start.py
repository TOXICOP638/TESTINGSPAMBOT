from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("☢️𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦☢️", data="help_back")
        ],
        [
        Button.url("☢️𝗖𝗛𝗔𝗡𝗡𝗘𝗟☢️", "https://t.me/HEROKU_CC_STORE"),
        Button.url("☢️𝗦𝗨𝗣𝗣𝗢𝗥𝗧☢️", "https://t.me/TCF_OFFICIAL")
        ],
        [
        Button.url("☢️𝗧𝗢𝗫𝗜𝗖-𝗫𝗗☢️", "https://t.me/TOHAR_BAAP_XD")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**𝗛𝗘𝗬 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝗜 𝗔𝗠  [{BotName}](tg://user?id={BotId})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **✦ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗗 𝗕𝗬 :~ [𝗧𝗢𝗫𝗜𝗖-𝗫𝗗](https://t.me/TOHAR_BAAPU_XD)**\n\n"
        TEXT += f"» **𝗧𝗢𝗫𝗜𝗖-𝗫𝗗 𝗦𝗣𝗔𝗠 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `3.2`\n"
        TEXT += f"» **𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡:** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file()
                event.chat_id,
                "https://graph.org/file/40c093f75c662d5d8e8cd.jpg",
                caption=TEXT, 
                buttons=PythonButton)

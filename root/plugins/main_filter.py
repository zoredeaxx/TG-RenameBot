'''
RenameBot
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''
import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psutil 
import shutil
import time
# the Strings used for this "thing"
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
from root.utils.utils import get_readable_file_size, get_readable_time

botStartTime = time.time()

@Client.on_message(filters.document | filters.video | filters.audio | filters.voice | filters.video_note | filters.animation) 
async def rename_filter(c,m):
    media = m.document or m.video or m.audio or m.voice or m.video_note or m.animation
    text = ""
    button = []
    try:
      filename = media.file_name
      text += f"FileName:\n{filename}\n"
    except:
    # some files dont gib name ..
      filename = None 
    
    text += "Select the desired Option"
    button.append([InlineKeyboardButton("Rename as File", callback_data="rename_file")])
    # Thanks to albert for mime_type suggestion 
    if media.mime_type.startswith("video/"):
      # how the f the other formats can be uploaded as video 
      button.append([InlineKeyboardButton("Rename as Video",callback_data="rename_video")])
      button.append([InlineKeyboardButton("Convert to File",callback_data="convert_file")])
      button.append([InlineKeyboardButton("Convert to Video ",callback_data="convert_video")])
    button.append([InlineKeyboardButton("Cancel ❌",callback_data="cancel")])
 

    try:
      await m.reply_text(text,quote=True,
         reply_markup=InlineKeyboardMarkup(button),
         disable_web_page_preview=True)
    except Exception as e:
      await m.reply(f"Error\n {e}", True)

      log.error(str(e))

@Client.on_message(filters.command(["stats"]) & filters.private)
async def stats_handler(c: Client, m: Message):
    currentTime = get_readable_time(time.time() - botStartTime)
    total, used, free = shutil.disk_usage(".")
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = (
        f"<b>╭「 💠 BOT STATISTICS 」</b>\n"
        f"<b>│</b>\n"
        f"<b>├⏳ Bot Uptime : {currentTime}</b>\n"
        f"<b>├💾 Total Disk Space : {total}</b>\n"
        f"<b>├📀 Total Used Space : {used}</b>\n"
        f"<b>├💿 Total Free Space : {free}</b>\n"
        f"<b>├🔺 Total Upload : {sent}</b>\n"
        f"<b>├🔻 Total Download : {recv}</b>\n"
        f"<b>├🖥 CPU : {cpuUsage}%</b>\n"
        f"<b>├⚙️ RAM : {memory}%</b>\n"
        f"<b>╰💿 DISK : {disk}%</b>"
    )
    await m.reply_text(text=stats, quote=True)

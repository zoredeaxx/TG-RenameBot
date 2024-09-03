import os, logging
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from root.config import Config
from root.messages import Translation
import shutil
import time
import psutil
from utils.utils import get_readable_file_size, get_readable_time
 
botStartTime = time.time()
log = logging.getLogger(__name__)

@Client.on_message(filters.command("stats"))
async def stats_handler(c,m):
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

@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    try:
       await m.reply_text(
            text=Translation.START_TEXT,
            quote=True, 
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton(
               "Owner ", 
               url=f"https://t.me/{Config.OWNER_USERNAME}")
             ]]) , 
            disable_web_page_preview=True
      ) 
    except Exception as e:
        log.error(str(e))

@Client.on_message(filters.command("help"))
async def help_user(c,m):
    try:
       await m.reply_text(text=Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))


@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")

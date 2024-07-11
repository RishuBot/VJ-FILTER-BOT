from info import API_ID, API_HASH, LOG_CHANNEL
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from utils import temp
from database.users_chat_db import db
import re
import pytz
from datetime import datetime
import asyncio
from Script import script
import time

@Client.on_message(filters.command('clone'))
async def clone_menu(client, message):

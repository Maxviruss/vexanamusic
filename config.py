import os
import aiohttp
from Python_ARQ import ARQ
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Vexana_robot")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/c2da18c0bd66f3631c8f4.png")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c2da18c0bd66f3631c8f4.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/c2da18c0bd66f3631c8f4.png")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/c2da18c0bd66f3631c8f4.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "Vexana_robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Vexana_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Vexana_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Vexana_updates")
OWNER_NAME = getenv("OWNER_NAME", "itzz_axel11") # fill in your username without the @ symbol
ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🚥")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
OWNER_ID = int(os.environ.get("OWNER_ID"))
# Database
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "True"))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/aksr-aashish/musicvexana")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)

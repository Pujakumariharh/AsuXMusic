from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "26119931")) 
API_HASH = getenv("API_HASH", "79e5b0d03df604b1bd1ee8b2f753372e")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN"5782334409:AAF9H9NZ-VY_vVZmIt2rn8JD_MYlAlHOfgI)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("LOGGER_ID"-1001618068091))
MONGO_DB_URI = getenv("MONGO_DB_URI"MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Nobitaxdbot:Nobitaxdbot@cluster0.9ypg5vh.mongodb.net/?retryWrites=true&w=majority)
OWNER_ID = list(map(int, getenv("OWNER_ID", "5897579715").split()))
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("START_IMG","https://telegra.ph/file/238d26f5188c9056b307b.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/alone_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/alone_support")
STRING_SESSION = getenv("STRING_SESSION",BQBBjW4UT2GqDGJJn5QvYb-lNTWPUsjo3fnL7uHN0njweYkCmLZyU0o5yWEqUZijsu82qh3vVbg-3zx5QveYPQahcfgrJtWQasGwDMT1_6KQh2yq0PHRBEyRACU2GFNOboetls9R4MJ_lko2yrMeRBqjyO_DSig1Llm4tQrdCz_iSEdEAtrq3MhyUPAmZWrkKceOjwD0xZo8amxsIH4QcZgoBqTro6EQinpeuA-3dK0BSpY1MnAuycNF0TiVIaLLwdhljOqV9CGeVd6CJN_3Ksn-QbpPZDlVzTrucOqPnEcMn7JWLXekF-W1dLSjEK078oH0jCikE_N15WhjvGlJ4k9MAAAAAV-9kLgA None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5901226168").split()))

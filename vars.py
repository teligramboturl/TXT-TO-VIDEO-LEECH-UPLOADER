

from os import environ

API_ID = int(environ.get("API_ID", "23673651"))
API_HASH = environ.get("API_HASH", "f032bfa12ee46e1283f6fb23cfca5c6b")
BOT_TOKEN = environ.get("BOT_TOKEN", "8307502375:AAH0_nZ784i-0Hdg4d75TlpIveBMbV7ynqE")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "palsabchannel")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/palsabchannel")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "6677821706").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "6677821706"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://beqaliha:BOn3lVYHJMjyD0P0@cluster0.asioswd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")



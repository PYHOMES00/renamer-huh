# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28243586")

API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7229486383:AAHwLgEvybUjmj9pH7n-pr8m9FgRHVkjG20") 

FORCE_SUB = os.environ.get("FORCE_SUB", "The_Creator_bot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "clustor0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://madarazbotz:b6xT4jUpyf4qzOFi@cluster0.tnvjhjr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5340652544').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Telegram Account Api Id And Api Hash
API_ID = int(os.getenv("API_ID", "24140875"))
API_HASH = os.getenv("API_HASH", "4386e721d5e41515ba9ea594555c37ac")

# Your Main Bot Token 
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(os.getenv("OWNER_ID", "1318826936")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = os.getenv("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# Port To Run Web Application 
PORT = int(os.getenv('PORT', 8080))

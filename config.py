#config.py 
from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "20078321"))
API_HASH = environ.get("API_HASH", "c8ed904e4aac83cea1f27b73984debad")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "8431050510:AAEu8WZD2FlFpzYapaDrnLWUMXPHVGhaBSg")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "1318826936")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://wanglinmongodb:wanglin@renegadeimmortal.o1qj9yf.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))

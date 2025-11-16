from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "24140875"))
API_HASH = environ.get("API_HASH", "4386e721d5e41515ba9ea594555c37ac")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "1318826936")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://wanglinmongodb:wanglin@renegadeimmortal.o1qj9yf.mongodb.net/?retryWrites=true&w=majority")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))

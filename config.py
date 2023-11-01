import os

API_ID = API_ID = 26368249

API_HASH = os.environ.get("API_HASH", "ac2db262d5eb7ce0efc0162404c8d172")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6370708272:AAFZmBMrKFZKJKWBoS3BQKWQP6mL6U8u-NM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5684410709))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5684410709").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)



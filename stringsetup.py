from telethon.sync import TelegramClient
from telethon.sessions import StringSession
#------------------------------------------#
print("Telethon String Session Generator")

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
#---------------------------------------#
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    string = client.session.save()
    result = client.send_message("me", string)
    result.reply("Here is Your String Session \nContact: @feelded")
    print("Check Your Telegram Saved Messages For String Session")

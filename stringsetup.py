from telethon.sync import TelegramClient
from telethon.sessions import StringSession
#------------------------------------------#
print("Online Telethon StringSessionGenerator")

APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
#---------------------------------------#
with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    string = client.session.save()
    result = client.send_message("me", string)
    result.reply("Here is Your StringSession \nContact: @FeelDeD")
    print("Check Your Telegram Saved Messages For StringSession")
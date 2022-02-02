from pyrogram import Client



Rexer=Client(
    "Pyrogram Bot",
    bot_token="5015801326:AAEAaUFxm0PFl9fbPoYNH_e6VHMJhvdb4lA",
    api_id="13160306",
    api_hash="5023c40ea655bc2834e48888b17ccee8"
)

from pyrogram import Client, filters



Rexer=Client(
    "Pyrogram Bot",
    bot_token="5015801326:AAEAaUFxm0PFl9fbPoYNH_e6VHMJhvdb4lA",
    api_id="13160306",
    api_hash="5023c40ea655bc2834e48888b17ccee8"
)
# -- Constants -- #
START = "hi bro"

@Rexer.on_message(filters.command("START"))
async def
    start_message(bot, message): await message.reply_text("START")



Rexer.run()

import discord

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

bot = discord.Bot()

@bot.slash_command()
async def restart_server(ctx):
    os.system(os.getenv("RESTART_PZ_SERVER_SCRIPT"))
    await ctx.respond("Restarting, should be back up in 5 minutes-ish..")

bot.run(os.getenv("BOT_TOKEN"))

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command= None)

@bot.event
async def on_ready():
    channel_len_tak = bot.get_channel(947043615992074241)
    await channel_len_tak.send(discord.__version__)
    await bot.close()

bot.run('MTAzNDgyNzk2NDQwNTI2MDMxOA.GCVFrX.zVFt8elzslAGWE33FV2E6xwojr5WKmJt5CQXlg')

# heroku login
# cd my-project/
# git init
# heroku git:remote -a heroku-botko
# git add .
# git commit -am "make it better"
# git push heroku master




#await client.wait_until_ready()
#channel_len_tak = client.get_channel(947043615992074241)
#await channel_len_tak.send(discord.__version__)





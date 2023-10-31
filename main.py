#https://discord.com/api/oauth2/authorize?client_id=1169037598803640501&permissions=8&scope=bot
import os
import discord
from discord import app_commands 
from dotenv import load_dotenv

load_dotenv()

# Initiating the bot
intents = discord.Intents().all()
activity = discord.Activity(name='to quran', type=discord.ActivityType.listening)
bot = discord.Client(intents=intents, activity=activity)
tree = app_commands.CommandTree(bot)
token = os.getenv('TOKEN')
guild_id = 1169038417942822932


@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print('[DONE]: We have logged in as {0.user}'.format(bot))

@bot.event
# Making Sure the bot doesn't reply to himself
async def on_message(message):
    print(message.content)
    if message.author == bot.user:
        return

#Setting up the commands
@tree.command(name = "ping", description = "Ping the bot", guild=discord.Object(id=guild_id)) 
@app_commands.describe()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

bot.run(token)
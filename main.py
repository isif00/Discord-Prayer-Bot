#https://discord.com/api/oauth2/authorize?client_id=1169037598803640501&permissions=8&scope=bot
import asyncio
from datetime import datetime
import os
import discord
from discord import app_commands 
from dotenv import load_dotenv

from api.calendar import get_prayer_times

load_dotenv()

# Initiating the bot
intents = discord.Intents().all()
activity = discord.Activity(name='to quran', type=discord.ActivityType.listening)
bot = discord.Client(intents=intents, activity=activity, allowed_mentions = discord.AllowedMentions(everyone = True))
tree = app_commands.CommandTree(bot)
token = os.getenv('TOKEN')
guild_id = 1169038417942822932
channel_id = 1169074414554447882

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

#Ping Pong
@tree.command(name = "ping", description = "Ping the bot", guild=discord.Object(id=guild_id)) 
@app_commands.describe()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

#get prayer times
@tree.command(name = "prayer-times", description = "get the prayer times", guild=discord.Object(id=guild_id)) 
@app_commands.describe()
async def ping(interaction: discord.Interaction):
    prayer_times_data = get_prayer_times()
    prayer_times = prayer_times_data["data"][0]["timings"]
    formatted_prayer_times = ""

    for key, value in prayer_times.items():
        formatted_prayer_times += f"{key}: {value}\n"
     
    await interaction.response.send_message(formatted_prayer_times)

#notify adhan time
async def send_prayer_time():
    prayer_times_data = get_prayer_times()
    prayer_times = prayer_times_data["data"][0]["timings"]

    while not bot.is_closed():
        current_time = datetime.now().strftime('%H:%M')
        for prayer, time in prayer_times.items():
            if current_time == time:
                channel = bot.get_channel(channel_id)  
                await channel.send(f"It's time for {prayer} prayer @everyone !")
        await asyncio.sleep(3600)
        
bot.run(token)
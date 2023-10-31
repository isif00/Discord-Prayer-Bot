#https://discord.com/api/oauth2/authorize?client_id=1169037598803640501&permissions=8&scope=bot
import os
import discord
from dotenv import load_dotenv

load_dotenv()

# Initiating the bot
intents = discord.Intents().all()
client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('[DONE]: We have logged in as {0.user}'.format(client))

@client.event
# Making Sure the bot doesn't reply to himself
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return


client.run(token)
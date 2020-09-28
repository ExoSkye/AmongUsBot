import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def getPrefix():
    with open("./conf.txt","r") as conf:
        lines = conf.readlines()
        return lines[0].strip("\n")

def setPrefix(newPrefix):
    replace_line("conf.txt",0,newPrefix+"\n")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(getPrefix()):
        if message.content[1:7] == "prefix":
            prefix = message.content[8:]
            setPrefix(prefix)
            await message.channel.send(f'Prefix set to `{prefix}`')

        elif message.content[1:5] == "help":
            await message.channel.send("""Currently supported commands are:
            - prefix [new prefix] *Changes the prefix*
            - help                *Displays this help message*
            - join   [game id]    *Tells the bot to join a game* **Not currently implemented**""")

        elif message.content[1:5] == "join":
            await message.channel.send("**Not currently implemented**")
        
        else:
            await message.channel.send("**Command not found**")

client.run(TOKEN)

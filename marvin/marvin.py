import discord
from random import choice
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime
import os
from credentials import LOGINS
from credentials import CHANNELS

load_dotenv("token.env")

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Bot online at {dt_string}.")

client = discord.Client()

def getLogin(loginCommand):
    if loginCommand == "apple":
        for key in LOGINS:
            if key == "Apple TV":
                this_login = (f'Username: {LOGINS[f"{key}"]["username"]}\nPassword: {LOGINS[f"{key}"]["password"]}')
        return this_login

@client.event
async def on_ready():
    channel = client.get_channel(CHANNELS["SKYNET"])
    await channel.send(f"Marvin logged in at {dt_string}.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f'Hello, {message.author.mention}!')
        
    if message.content.startswith('!status'):
        # await message.channel.send(f'Please check status in <#{SKYNET}>')
        await message.channel.send(choice(
            ["I think you ought to know I'm feeling very depressed.",
             "Here I am, brain the size of a planet, and they tell me to take you up to the bridge. Call that job satisfaction? 'Cos I don't.",
             "Life? Don't talk to me about life.",
             "I wish you'd just tell me rather than trying to engage my enthusiasm because I haven't got one.",
             "There's only one life-form as intelligent as me within thirty parsecs of here and that's me."]
        ))

    if message.content.startswith("!help"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        await channel.send(message.author.mention)
        await channel.send("Current commands are:")
        commands = ["!status", "!help", "!source", "!appletv", "!hbomax", "!wsj", "!peacock", "!mlb", "!disneyplus"]
        for command in commands:
        	await channel.send(command)

    if message.content.startswith("!games"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        await message.channel.send(message.author.mention)
        await message.channel.send("Wordle:\n<https://www.nytimes.com/games/wordle/index.html>"
                           "\n\nWorldle:\n<https://worldle.teuteuf.fr/>"
                           "\n\nNerdle:\n<https://nerdlegame.com/>"
                           "\n\nLordle of the Rings:\n<https://digitaltolkien.github.io/vue-wordle/>"
                           "\n\nGloble:\n<https://globle-game.com/>"
                           "\n\nWaffle:\n<https://wafflegame.net/>"
                           "\n\nFramed:\n<https://framed.wtf/>"
                           "\n\nMoviedle:\n<https://www.moviedle.app/>")

    if message.content.startswith("!appletv"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        #await channel.send(message.author.mention)
        this_login = getLogin("apple")
        await channel.send(this_login)

    if message.content.startswith("!hbomax"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        for key in LOGINS:
            if key == "HBO Max":
                this_login = (f'Username: {LOGINS[f"{key}"]["username"]}\nPassword: {LOGINS[f"{key}"]["password"]}')
        await channel.send(message.author.mention)
        await channel.send(this_login)

    if message.content.startswith("!wsj"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        for key in LOGINS:
            if key == "WSJ":
                this_login = (f'Username: {LOGINS[f"{key}"]["username"]}\nPassword: {LOGINS[f"{key}"]["password"]}')
        await channel.send(message.author.mention)
        await channel.send(this_login)

    if message.content.startswith("!peacock"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        for key in LOGINS:
            if key == "Peacock":
                this_login = (f'Username: {LOGINS[f"{key}"]["username"]}\nPassword: {LOGINS[f"{key}"]["password"]}')
        await channel.send(message.author.mention)
        await channel.send(this_login)

    if message.content.startswith("!mlb"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        for key in LOGINS:
            if key == "MLB":
                this_login = (f'Username: {LOGINS[f"{key}"]["username"]}\nPassword: {LOGINS[f"{key}"]["password"]}')
        await channel.send(message.author.mention)
        await channel.send(this_login)

    if message.content.startswith("!disneyplus"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        await channel.send(message.author.mention)
        await channel.send("<https://www.youtube.com/watch?v=dQw4w9WgXcQ>")

    if message.content.startswith("!kill"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        await channel.send("Goodbye, Arthur.\nMarvin is offline.")
        await client.close()
        quit()

    if message.content.startswith("!source"):
        channel = client.get_channel(CHANNELS["SKYNET"])
        await channel.send(message.author.mention)
        await channel.send("See my source code at:"
                           "\nhttps://github.com/thanksforthefish/bots/blob/main/discord/marvin/marvin.py")


client.run(os.getenv("TOKEN"))
my_secret = os.environ["TOKEN"]
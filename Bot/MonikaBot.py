import discord
import os
import numpy as np
from asyncio import sleep
from random import choice

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

STATUS_LIST = ['uwu', 'uwU', 'uWu', 'uWU', 'Uwu', 'UwU', 'UWu', 'UWU']
INPUTSTRING = "GIMMEDEMNUMBERS"

def getZs():
    return '\n'.join(map(str, np.random.normal(size=10)))

@client.event
async def on_ready():
    '''Called when client is ready. Prints the bot's current user.'''
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        if message.author == client.user:
            return
        if message.content == "?start":
            await message.author.send("Welcome puzzle attempter! My name is Monika. I’ve been trapped in this dark room for an eternity. Will you help me?")
        print(message.content + " by " + message.author.name)
        
        if isinstance(message.channel, discord.DMChannel):
            if message.content.upper() in ["YES", "Y"]:
                await message.author.send("This dark room seems to flash this image periodically. Sometimes, these words are also said: DIBEH-YAZZIE AH-JAH D-AH ‘ DIBEH  AH-TAD A-KHA  D-AH A-KHA  CHA-GEE  TAH-BAHN (B) TAH-BAHN (B). What are they saying?")
                await message.author.send("https://blog.kachinahouse.com/wp-content/uploads/2020/04/oHwngOow.png")
            if message.content.upper() == "LET'S GO TO THE BEACH BEACH":
                await message.author.send("Oh! Now the images are gone, but this tune started playing! What is going on? _ _ _ _ _  _ _ _  _ _ _ _ _ _")
                await message.author.send("https://drive.google.com/file/d/1A3WexiPTvaLBQBh7OqGsC9WVtbtfPCBB/view?usp=sharing")
            if message.content.upper() == "ENTER THE MATRIX":
                await message.author.send("That annoying sound finally stopped! But what are all of these numbers?")
                await message.author.send("https://drive.google.com/file/d/1HAAU99V8KBlUUn8KxFeJT2xa2PD7fipe/view?usp=sharing")
            if message.content.upper() == "1413":
                await message.author.send(getZs() + f"\nWhat? You just created even more numbers! What is this distribution? Wait, try typing in `{INPUTSTRING}`.\nSee if that changes anything.")
            if message.content.upper() == INPUTSTRING:
                await message.author.send(getZs())
            if message.content.upper() in ["NORMAL", "GAUSSIAN", "STANDARD NORMAL", "GAUSS"]:
                await message.author.send("Wow you are really good at math. I’d give you a 7.8/10! The room seems to be so much darker, I can barely see anything except for these small flashes of light. They appear to read a long series of meaningless letters! \n A1B1A2DB1A2DA1B2A2A3DB1A2A3DB1A2B2A3DDA1B1DA1B2A3DA1B1A3DA1B2DB1A2A3DDA1A2B2A3DA1B2DA1A2A3DB1A2DA1B1DA1DA1B1B2A3DB1A2B2A3DA1A2B2DA2B2B3DDA1A2A3DA1DB1A2A3DB1A2B2A3DDA1A2DA1B2A3DA1B1A3DA1B2DB1A2A3DDB1A2B2B3DA1DB1A2DA1A2A3DA1B2A3DA1A2B2A3DA1B1B2DA2B2B3")
            if message.content.upper() in ["RELICANTH WAILORD", 'FIRST COMES RELICANTH. LAST COMES WAILORD.']:
                await message.author.send("Huh! It appears that the lights turned on! Where are we? Oh, I found this letter on the ground. ")
                await message.author.send("https://docs.google.com/document/d/1jkRFI2jD31xIsTPPDLYGtH3JMWtSP_6JIeOSKWVIgA4/edit?usp=sharing")
            if message.content.upper() == "200340":
                await message.author.send("I feel like we are making progress! What’s this? Another letter? Maybe it’s a clue on how to get out of this! ")
                await message.author.send("https://docs.google.com/document/d/1g1gkPsh9o8JS4WOuwQed-abiWsO7C6OWAevbMZoBApk/edit?usp=sharing")
            if message.content.upper() == "B01EA8EWJW":
                await message.author.send("You and I make a great team! We are getting so close to getting out! Wait there is a computer here! Oh! It’s about something called MenloHacks. There are a few names here: Wesjol Ho, Xacl Eara, Kovam Nirm, Thamn Tsuo. I feel like one of them is the odd man out, but who is it?")
            if message.content.upper() == "ALEX ACRA":
                await message.author.send("You’re so awesome! Your codebreaking is unparalleled! After all, consistency is key! It’s almost a shame that the end is so near. Would you be a dear and investigate this image for me? [insert hidden image]")
                await message.author.send("https://drive.google.com/file/d/1xDgYuO_SRrKja95IbjJGX3ZyE89JF9-n/view?usp=sharing")
            if message.content.upper() == "YOURE STAYING FOREVER WITH ME UWU":
                await message.author.send("What, you think I’m holding you hostage? Of course not! UwU. Here solve this puzzle, or this letter, or this message. Here I found some more characters. What? You want to leave. Well that’s impossible. You would need all of my login information, which you will never get. Not even the MenloHacks website can help you. Now in the meantime, can you analyze this video for me please :) UWU")
                await message.author.send("monikashotelroomwithoutkey")
                await message.author.send("Type `verify123: password` to delete the account")
            if message.content == "verify123: }sJ)WIP<9ju:yhdK4cjou~LBN:Lg5BqyYiqCnX^HAiGuQzc":
                await message.author.send("Congratulations! You have deleted Monika! You are free and have solved the puzzle. Amazing job! -jgl789 and Sam0fc")
                for i in client.guilds:
                    await i.system_channel.send("Well done to "+ message.author.name + " for completing the puzzle!")

async def update_status():
    '''randomize status'''
    await client.wait_until_ready()
    while True:
        # await client.change_presence(activity=discord.Game(name=choice(STATUS_LIST)))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f"you solve puzzles {choice(STATUS_LIST)}"))
        await sleep(60) # task runs every 60 seconds

client.loop.create_task(update_status())
client.run(os.getenv("TOKEN"))
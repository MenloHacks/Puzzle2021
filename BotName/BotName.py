import discord
import os
import time
import numpy

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
 await member.guild.system_channel.send("Hail Traveler, " + member.name + "!")
 await member.guild.system_channel.send("Let's get puzzling! Check your DMs")
 await member.send("https://lyrical-brave-sailboat.glitch.me/ \n *smoke bomb*")

@client.event
async def on_ready():
 '''Called wheTh client is ready. Prints the bot's current user.'''
 print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
       if message.author == client.user:
           return
       print(message.content + " by " + message.author.name)
       if isinstance(message.channel, discord.DMChannel):
         if message.content.upper() == "POG":
           await message.author.send("https://lyrical-brave-sailboat.glitch.me/start.html \n *smoke bomb*")
         if message.content.upper() == "RICK-ASTLEY-PI":
           await message.author.send("You have done well! \n Millhall salutes you. \n Pi is a nice number. Though not as great as 4. For the next clue, you will need to look to the past. Find where the motions of this puzzle were set up, and where Millhall's conception could have been averted. \n *smoke bomb* ")
         if message.content.upper() == "WRONG-'EM-BOYO":
           await message.author.send("Congratulations, that was **quick**. Millhall is surprised that it took you only that time. For the next one, you'll have to unpack this image: https://drive.google.com/file/d/14zdKXDICrckzvYsFcKeuQwBP-HnsWV9d/view?usp=sharing \n *smoke bomb*")
         if message.content.upper() == "TYRESTY":
           await message.author.send("The lady of the house handed me this map, but she had scrawled @37.4522786,-122.1768182,21z on it. Weird huh? Anyways, I'm going to go look for the turkey for dinner. What should I play to set the mood?\n *smoke bomb*")
         if message.content.upper() == "HINT":
           await message.author.send("Millhall applauds your effort but uh,,, it's not going to be that easy. Ask Sam maybe.")
         if message.content.upper() == "D&D-COMMUNISM-MINECRAFT":
           await message.author.send("Nice Try Jono. ")
         if message.content.upper() == "MOOD":
           await message.author.send("Since the puzzle is now over, the minecraft server is no longer hosted. Thanks for playing! You have completed the puzzle.")
           for i in client.guilds:
             await i.system_channel.send("Well done to "+ message.author.name + " for completing the puzzle")

client.run(os.getenv("TOKEN"))

import discord
import random
import os

bot = discord.Client()
key = os.environ['BotKey']
copyright = 'made by GamerCodeFalse'

@bot.event
async def on_ready():
  print("IM FUCKING READY BITCH, ITS ME {0.user}".format(bot))
@bot.event
async def on_message(message):
  if(message.author == bot.user):
    return
  if(message.content.startswith('$BITCHBOYADVANCED')):
    await message.channel.send("*Moans* I am the 69 simulator type fuck to fuck me")
    if(message.content.has == "fuck"):
      await message.channel.send("*Moan*")
      if(random.random(1) > 0.5):
        await message.channel.send("Yes Daddy!")
      elif(random.random(1) > 0.1):
        await message.channel.send("Your cum is every WHERE!")
  else:
    run = True
    if(message.content.startswith('$spam')):
      while run:
        await message.channel.send("@everyone")
        if(message.content.startswith("$stop")):
          run = False
bot.run(key)
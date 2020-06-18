import discord 
import requests
import mysql.connector
import asyncio
import random
import os 
from functions import *
from chat import *



TOKEN = "NzAxNDY3MzA5MTM0NDQ2NzMz.XuufuA.toa5UmcRWdssYmeMAnN6MkS7BGA"
cid = "701467309134446733"
memcount = 0
client = discord.Client()
me = ["Friendly Banter#9568"]



@client.event
async def on_ready():
    guild = client.get_guild(286319730984353799)
    for i in guild.members:
        i = str(i)
        print(i)

    
inc = 0

@client.event
async def on_message(message):
    
    global memcount
    memcount +=1 
    

    await client.wait_until_ready() #lets the bot load all members in the server

    serverid = client.get_guild(286319730984353799)
    
    

    if message.content == "game":
        name = str(message.author)
        p1 = Person(name,0)
   
        await message.channel.send("Guess a number from 1 to 5")
        global inc
        n = random.randint(1,5)
        num = 0
        chance = 4
        counter = 0
        while num != n and counter < chance:
            msg = await client.wait_for('message')
            msg = str(msg.content)
            

            if msg.isdigit() == True:
                counter += 1
                num = int(msg)
                if counter == 4:
                    await message.channel.send("you exceeded 3 tries")
                    break
                elif num < n:
                    await message.channel.send("Too Low")
                elif num == n:
                    await message.channel.send("Perfect +2")
                    set_score(p1,2)
                
                    print("Score of p1 : " +str(get_score(p1)))
                    await message.channel.send("Your score from our database is : " + str(get_score(p1)))
                elif num > n:
                    await message.channel.send("Too High")
    
    elif message.content == "get_members()":
        await message.channel.send("{}".format(serverid.member_count))
        for i in serverid.members:
            i = str(i)
            await message.channel.send("{}".format(i))

    elif message.content == "chat":
        msg = await client.wait_for('message')
        while(msg != 'leave'):
            
            msg = str(msg.content)
            
            if msg in GREETINGS:
                print(greeting(msg))
                await message.channel.send(greeting(msg))
            else:
                print("Chatbot: " + get_response(msg))
                await message.channel.send(get_response(msg))

            msg = await client.wait_for('message')
        
        
    elif message.content == "score()":
        name = str(message.author)
        p1 = Person(name,0)
        t = get_score(p1)
        await message.channel.send("{}".format(str(t)))
    elif "HAHAAHA" in message.content:
        temp = str(message.author)
        await message.channel.send("Hello " + temp[:-5])#removes the last 5 characters in the string
        
    elif str(message.author) in me: #authorized admins
        if "exit()" in message.content:
            await message.channel.send("Shutting down..")
            await client.close()

    return



client.run(TOKEN)
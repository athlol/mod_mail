import discord

client = discord.Client()




   #the command for the mod mail thingies 




@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")


    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "] ")
        

            for file in files:
                await modmail_channel.send(file.url)
        else:     #the messaging.# 
            await modmail_channel.send("[" + message.author.display_name + "]" + message.content)
            embedVar = discord.Embed(title="Your message has been sent. ✅", description="Please await a message from our staff team.", color=0x00ff00)
        await message.channel.send(embed=embedVar)







    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)
            another_one=discord.Embed(title="sent ✅", description="your message has been sent to the user.", color=0x00ff00)
            await message.channel.send(embed=another_one)
    



    #help commands
    
    
    elif message.content.startswith('?mm help'):
     help=discord.Embed(title="Hello!", description ="**__DM (direct message) me for any form of support with the server or the bot.__**", color=0x800080)
     await message.channel.send(embed=help)
 
    










    
    
    #pinging,status & running




@client.event 

async def on_ready():
    game = discord.Game("watching your DMs 👀")
    await client.change_presence(status=discord.Status.online, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------') 

client.run("ODMwMzM5NTc5MzE1MDkzNTE0.YHFP_g.QYpW--adraPE3OWsGTgOqCx55fs")
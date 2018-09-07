import discord
import asyncio
from discord.ext import commands
import aiohttp
import async_timeout
from bs4 import BeautifulSoup
import dashtable
import html2text
import json

#bot Location CommandParent
class admin:
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(pass_context=True)
    async def admin(self,ctx):
        if ctx.message.author.server_permissions.administrator==False:
            await self.bot.say("You don't have permissions...")
        if ctx.invoked_subcommand is None:
            await self.bot.say('`No valid command entered`')

    @admin.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(title="Admin Commands", description="Admin Commands are:", color=0xeee657)
        embed.add_field(name="NOTICE", value="ONLY WORKS WITH ADMINISTRATOR PERMISSION", inline=False)
        embed.add_field(name=">admin kick [name]", value="Kicks **name** from discord server.", inline=False)
        embed.add_field(name=">admin ban [name]", value="Bans **name** from discord server", inline=False)
        embed.add_field(name=">admin chatpurge [number]", value="Purges **number** messages from chat provided it is less than 101.", inline=False)
        try:
            await self.bot.send_message(ctx.message.channel, embed=embed)
        except:
            print("Error")

    @admin.command(pass_context=True)
    async def kick(self,ctx,userName:discord.User):
        if ctx.message.author.server_permissions.administrator==True:
            await self.bot.say('Kicking '+str(userName.name))
            await self.bot.kick(userName)
        else:
            await self.bot.say("You don't have permissions...")


    @admin.command(pass_context=True)
    async def ban(self,ctx,userName:discord.User):
        if ctx.message.author.server_permissions.administrator==True:
            await self.bot.say('Banning '+str(userName.name))
            await self.bot.ban(userName)
        else:
            await self.bot.say("You don't have permissions...")


    @admin.command(pass_context=True)
    async def chatpurge(self,ctx,number):
        if ctx.message.author.server_permissions.administrator==True:
            msgs=[]
            try:
                number=int(number)
            except:
                await self.bot.say('`No valid number input, deleting 1 message`')
                number=1
            async for x in self.bot.logs_from(ctx.message.channel,limit = number):
                msgs.append(x)
            try:
                await self.bot.delete_messages(msgs)
                await self.bot.send_message(ctx.message.channel,'`PURGED '+str(number)+' MESSAGES FROM THIS CHANNEL`')
            except:
                await self.bot.say('`Can only purge up to 100 messages from a chat and messages under 14 days old.`')
        else:
            await self.bot.say("You don't have permissions...")
        
                    

        
        
                    
def setup(bot):
    bot.add_cog(admin(bot))


async def fetch(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

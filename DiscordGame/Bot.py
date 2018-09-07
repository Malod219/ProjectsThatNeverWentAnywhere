# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import random
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from datetime import datetime

#Credentials, Tokens etc
import credentials

# Modify command prefix
bot = Bot(description="DEFCON", command_prefix=">>>", pm_help = False)

#Prints generic bot information to consol
@bot.event
async def on_ready():
        print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
        print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
        print('Invitation to bring this to the server {}:'.format(bot.user.name))
        print('https://discordapp.com/oauth2/authorize?bot_id={}&scope=bot&permissions=8'.format(bot.user.id))
        print("Start time:" + datetime.now().strftime("%Y-%m-%d %H:%M"))
        bot.day=datetime.now().strftime("%Y-%m-%d")
        print(bot.day)
        presenceNum = random.randint(0,3)
        if presenceNum==0:presenceChat="NUCLEAR WARFARE"
        elif presenceNum==1:presenceChat="DEFCON 5"
        elif presenceNum==2:presenceChat="DEFCON 3"
        elif presenceNum==3:presenceChat="DEFCON 1"
        return await bot.change_presence(game=discord.Game(name=presenceChat))

        
bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx):
        embed = discord.Embed(title="Help commands", description="Help Commands are:", color=0xeee657)
        embed.add_field(name=">>>defcon help", value="Lists commands for admin", inline=False)
        embed.add_field(name=">info", value="More information on the bot.", inline=False)
        embed.add_field(name=">server info", value="More information on the bot.", inline=False)
        await bot.send_message(ctx.message.author, embed=embed)


@bot.command(pass_context=True)
async def info(ctx):
        embed = discord.Embed(title="General Information", description="General Information on DEFCON project.", color=0xeee657)
        embed.add_field(name="Who it is developed by:", value="ODST", inline=False)
        embed.add_field(name="How is it hosted:", value="On a Raspberry Pi at home like the rest of my bots", inline=False)
        embed.add_field(name="Contact Me", value="Discord@ODST#7648 Skype@perfectodst", inline=False)
        await bot.send_message(ctx.message.author, embed=embed)

        
initial_extensions=[
        'defcon'
        ]
channellist=[]


if __name__=='__main__':
        for extension in initial_extensions:
                bot.load_extension(extension)
        
bot.run(credentials.bot_token)

import discord
import asyncio
from discord.ext import commands
import json

#bot Location CommandParent
class defcon:
    def __init__(self,bot):
        self.bot = bot
    
    @commands.group(pass_context=True)
    async def defcon(self,ctx):
        if ctx.message.author.server_permissions.administrator==False:
            await self.bot.say("You don't have permissions...")
        if ctx.invoked_subcommand is None:
            await self.bot.say('`No valid command entered`')
    @defcon.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(title="DEFCON Commands/How to play", description="DEFCON Commands are:", color=0xeee657)
        embed.add_field(name="NOTICE", value="Not a balanced game.", inline=False)
        embed.add_field(name=">>>defcon silo [x,y]", value="Places a silo if in DEFCON 4, you have the money for it and in your territory.", inline=False)
        embed.add_field(name=">>>defcon icbm [SiloX,SiloY,TargetX,TargetY]", value="Launch a silo at target coordinates from silo.", inline=False)
        embed.add_field(name=">>>defcon end", value="Ends your turn, Make sure you're ready to end your turn.", inline=False)
        embed.add_field(name=">>>defcon sub [x,y]", value="Places sub at coordinates provided it's not in any territory.", inline=False)
        embed.add_field(name=">>>defcon mrbm [SubX,SubY,TargetX,TargetY]", value="Launch MRBM from Sub. Range = 5 tiles up in a square around sub.", inline=False)
        embed.add_field(name=">>>defcon airbase [x,y]", value="Places an Airbase at coordinates.", inline=False)
        embed.add_field(name=">>>defcon carrier [x,y]", value="Places a Carrier at coordinates.", inline=False)
        embed.add_field(name=">>>defcon bomber [FromX,FromY,x,y]", value="Launch Bomber to coordinates from an airbase, carrier or your own bomber.", inline=False)
        embed.add_field(name=">>>defcon bomber [FromX,FromY]", value="Launch Bomber to coordinates from an airbase, carrier or your own bomber.", inline=False)
        try:
            await self.bot.send_message(ctx.message.channel, embed=embed)
        except:
            print("Error")
    @defcon.command(pass_context=True)
    async def map(self,ctx):
        with open('currentmap.txt','r') as world:
            worldmap=world.read()
            await self.bot.send_message(ctx.message.channel,"```"+str(worldmap)+"```")

    @defcon.command(pass_context=True)
    async def join(self,ctx,country):
        country=str(country)
        if gamestateDict[country]==None:
            gamestateDict[country]=ctx.message.author
            await self.bot.send_message(ctx.message.channel,"```Joined```")
        else:
            await self.bot.send_message(ctx.message.channel,"```Someone's playing that team.```")

    @defcon.command(pass_context=True)
    async def start(self,ctx):
        if gamestateDict["state"]=="n":
            gamestateDict["state"]="y"
            gamestateDict["turn"]=0
            with open('originmap.txt','r') as world:
                worldmap=world.read()
            with open('currentmap.txt','w') as world:
                world.write(worldmap)
            await self.bot.send_message(ctx.message.channel,"```Game Started```")
            await self.bot.change_presence(game=discord.Game(name="DEFCON 5"))
        else:
            await self.bot.send_message(ctx.message.channel,"```Game in progress```")

    @defcon.command(pass_context=True)
    async def silo(self,ctx,x,y):

        with open('currentmap.txt','r') as world:
            worldmap=world.readlines()

        if gamestateDict["turn"]== 0:
            x=str(x)
            y=str(y)
            if x in validX or y in validY:
                mapX, mapY=coordDict[x], coordDict[y]

                line = list(worldmap[mapY])
                line[mapX]="^"
                line = "".join(line)
                worldmap[mapY] = line
                print(worldmap)

                with open('currentmap.txt','w+') as world:
                    for line in worldmap:
                        print(line)
                        world.write(line)
                with open('currentmap.txt','r') as world:
                    worldmap=world.read()
                await self.bot.send_message(ctx.message.channel,"```"+str(worldmap)+"```")
            else:
                await self.bot.send_message(ctx.message.channel,"```Entered illegal coordinates```")
        else:
            await self.bot.send_message(ctx.message.channel,"```It's not DEFCON 5. You can't place more silos.```")

    @defcon.command(pass_context=True)
    async def turn(self,ctx):
        gamestateDict["turn"]+=1
        turn = gamestateDict["turn"]
        if turn==1:
            await self.bot.change_presence(game=discord.Game(name="DEFCON 4"))
        elif turn==2:
            await self.bot.change_presence(game=discord.Game(name="DEFCON 3"))
        elif turn==3:
            await self.bot.change_presence(game=discord.Game(name="DEFCON 2"))
        elif turn>=4:
            await self.bot.change_presence(game=discord.Game(name="DEFCON 1"))

    @defcon.command(pass_context=True)
    async def ready(self,ctx):
        username=ctx.message.author
        for key, value in gamestateDict.items():
            if value==ctx.message.author:
                ready[key]=1
            if value==None:
                ready[key]=1
        for key, value in ready:
            if value==0:
                nextturn=True
        if nextturn==True:
            gamestateDict["turn"]+=1
            turn = gamestateDict["turn"]
            if turn==1:
                await self.bot.change_presence(game=discord.Game(name="DEFCON 4"))
            elif turn==2:
                await self.bot.change_presence(game=discord.Game(name="DEFCON 3"))
            elif turn==3:
                await self.bot.change_presence(game=discord.Game(name="DEFCON 2"))
            elif turn>=4:
                await self.bot.change_presence(game=discord.Game(name="DEFCON 1"))



def setup(bot):
    bot.add_cog(defcon(bot))


#CoordinateConverstion
coordDict={
    "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,"a":27,"b":28,"c":29,"d":30,"e":31,"f":32,"g":33,"h":34,"i":35,"j":36,"k":37,"l":38,"m":39,"n":40,"o":41,"p":42,"q":43,"r":44,"s":45,"t":46,"u":47,"v":48,"w":49,"x":50,"y":51,"z":52,"1":53,"2":54,"3":55,"4":56,"5":57,"6":58,"7":59,"8":60,"9":61,"0":62,"!":63,'"':64,"£":65,"$":66,"%":67,"^":68,"&":69,"*":70
}
#GamestateInfo
gamestateDict={
    "turn":0,
    "state":"n",
    "northamerica":None,
    "europe":None,
    "asia":None,
    "oceania":None,
    "southamerica":None,
    "russia":None
}
#resource dictionaries
northamerica={"silos":6}
southamerica={"silos":6}
asia={"silos":6}
africa={"silos":6}
oceania={"silos":6}
europe={"silos":6}
russia={"silos":6}
#Ready up
ready={"northamerica":0,"southamerica":0,"asia":0,"oceania":0,"europe":0,"russia":0,"africa":0}
#ValidCoordinates
validX=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","Y","Z"]
validY=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!",'"',"£","$","%","^","&","*"]
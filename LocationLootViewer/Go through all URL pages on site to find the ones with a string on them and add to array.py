import urllib.request
from bs4 import BeautifulSoup#Imports all the shit needed
img=None
choice="1"
selection="vagina"

def dickhead(string,choicemax,null0,null1,null2,null3,null4):
    selection=True
    while selection==True:
        try:
            choice=str(input(string))
            if choice>=str(1) and choice<=str(choicemax):
                if choice==str(1):
                    img=null0
                elif choice==str(2):
                    img=null1
                elif choice==str(3):
                    img=null2
                elif choice==str(4):
                    img=null3
                else:
                    img=null4
                selection=False
                print("Calculating... May take a few minutes...")
            else:
                print("Don't be a dumbass, pick an integer from 1 to "+str(choicemax))
        except ValueError:
            print("Don't be a dumbass, pick an integer from 1 to "+str(choicemax))

        return choice
def idickhead(string,choicemax,null0,null1,null2,null3,null4):
    selection=True
    while selection==True:
        try:
            choice=str(input(string))
            if choice>=str(1) and choice<=str(choicemax):
                if choice==str(1):
                    img=null0
                elif choice==str(2):
                    img=null1
                elif choice==str(3):
                    img=null2
                elif choice==str(4):
                    img=null3
                else:
                    img=null4
                selection=False
                print("Calculating... May take a few minutes...")
            else:
                print("Don't be a dumbass, pick an integer from 1 to "+str(choicemax))
        except ValueError:
            print("Don't be a dumbass, pick an integer from 1 to "+str(choicemax))

        return img
choice=int(dickhead("Pick a number\n1-General Resources\n2-Civilian Loot\n3-Food Loot\n4-Potion Loot\n5-Tool Loot\n6-Military Loot\n7-Room Loot\n8-Dungeon Loot",8,None,None,None,None,None))
print(choice)
if choice==1:
    img=idickhead("Pick a number\n1-Water Refill\n2-Crafting Table\n3-Farm\n4-Brewing Stand",4,'http://shotbow.net/forum/images/water_bottle.png','http://shotbow.net/forum/images/crafting_table.png','http://shotbow.net/forum/images/farm.png','http://shotbow.net/forum/images/brewing_stand.png','http://shotbow.net/forum/images/brewing_stand.png')
elif choice==2:
    img=idickhead("Pick a number\n1-Civ_Common\n2-Civ_Uncommon",2,'http://shotbow.net/forum/images/raw_fish.png','http://shotbow.net/forum/images/paper.png','http://shotbow.net/forum/images/paper.png','http://shotbow.net/forum/images/paper.png','http://shotbow.net/forum/images/paper.png')
elif choice==3:
    img=idickhead("Pick a number\n1-Food_Common\n2-Food_Uncommon\n3-Food_Rare",3,'http://shotbow.net/forum/images/melon.png','http://shotbow.net/forum/images/carrot.png','http://shotbow.net/forum/images/cake.png','http://shotbow.net/forum/images/cake.png','http://shotbow.net/forum/images/cake.png')
elif choice==4:
    img=idickhead("Pick a number\n1-Pot_Common\n2-Pot_Uncommon\n3-Pot_Rare",3,'http://shotbow.net/forum/images/health_potion.png','http://shotbow.net/forum/images/splash_health.png','http://shotbow.net/forum/images/yellowDust.png','http://shotbow.net/forum/images/yellowDust.png','http://shotbow.net/forum/images/yellowDust.png')
elif choice==5:
    img=idickhead("Pick a number\n1-Tool_Common\n2-Tool_Uncommon",2,'http://shotbow.net/forum/images/iron_shovel.png','http://shotbow.net/forum/images/button.png','http://shotbow.net/forum/images/button.png','http://shotbow.net/forum/images/button.png','http://shotbow.net/forum/images/button.png')
elif choice==6:
    img=idickhead("Pick a number\n1-Mil_Common\n2-Mil_Uncommon\n3-Mil_Rare\n4-Mil_Epic\n5-Mil_Mythic",5,'http://shotbow.net/forum/images/arrow.png','http://shotbow.net/forum/images/chain_chestplate.png','http://shotbow.net/forum/images/iron_sword.png','http://shotbow.net/forum/images/ender_pearl.png','http://shotbow.net/forum/images/gunpowder.png')
elif choice==7:
    img=idickhead("Pick a number\n1-Room_Common\n2-Room_Uncommon\n3-Room_Rare",3,'http://shotbow.net/forum/images/bow.png','http://shotbow.net/forum/images/sugar.png','http://shotbow.net/forum/images/zombie_skull.png','http://shotbow.net/forum/images/zombie_skull.png','http://shotbow.net/forum/images/zombie_skull.png')
elif choice==8:
    img=idickhead("Pick a number\n1-Dungeon_In\n2-Dungeon_Out\n3-LegendaryDispenserAnyType",3,'http://shotbow.net/forum/images/gold_apple.png','http://shotbow.net/forum/images/pumpkin_pie.png','http://shotbow.net/forum/images/gold_sword.png','http://shotbow.net/forum/images/gold_sword.png','http://shotbow.net/forum/images/gold_sword.png')

loclist = []
locnamelist=[]
datalist=[]#Declarations of lists
with urllib.request.urlopen('https://shotbow.net/forum/wiki/minez-locations/') as gay:
    html=gay.read()
    htmls=html.decode()
    a,b=htmls.split('<h2><a name="locations">')
    c,d=b.split('<h2><a name="removed-locations">')
    html=c.encode()#Splits the html page accordingly, so that only locations are listed(Removes top/bottom of page)
soup= BeautifulSoup(html, "html.parser")#Creates some soup to parse
for link in soup.find_all('a'):
    loclist.append(link.get('href'))
    locnamelist.append(link.text)#Stores in lists the Relative URLs and their texts
for n in range(len(loclist)):#Iterates through each URL in list
    try:
        with urllib.request.urlopen(('https://shotbow.net/forum/'+loclist[n])) as dick:
            soups= BeautifulSoup(dick.read(), "html.parser")#More soup
            try:
                for imgtag in soups.find_all('img'):
                    if imgtag['src']==str(img):#Image checks the tables
                        td=imgtag.findNext('td')
                        dt=td.findNext('td').get_text()
                        if dt=="":
                            dt=td.findNext('span')
                            dt=dt.findNext('span').get_text()


                        
                        if (dt.find('X')==-1 and dt.find('?')==-1):
                            datalist.append(locnamelist[n])
            except:
                selection="dick"
    except urllib.error.HTTPError:
        selection="dick"
    except TypeError:
        selection="dick"#Exceptions for any errors
print(datalist)
enter=input("Press any key to continue...")

selection=True

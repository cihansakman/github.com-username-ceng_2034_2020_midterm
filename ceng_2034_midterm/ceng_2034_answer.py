#!/usr/bin/python3
import os,requests,sys,threading

def implementation(url):
	print("PID:",os.getpid())
	load_avg = os.getloadavg()
	cpu_count = os.cpu_count()
	if(sys.platform == 'linux'):
		print("Load average is: ",load_avg)
		print("5 min load avg is:",load_avg[1],"\nCpu core count:",cpu_count) 
		if(cpu_count-load_avg[1]<0):
			exit()
		
	respond = requests.get(url)
	r_code = respond.status_code
	if(200<= r_code <300):
		print("URL code=",r_code)
		print(url,"is working.")
	elif(400<= r_code <600):
		print("URL code=",r_code)
		print(url,"is not working.")
	
urls=['https://api.github.com​','http://bilgisayar.mu.edu.tr/​','https://www.python.org/​', 'http://akrepnalan.com/ceng2034​', 'https://github.com/caesarsalad/wow​']

thread1 = threading.Thread(target = implementation, args = (urls[0],))
thread2 = threading.Thread(target = implementation, args = (urls[1],))
thread3 = threading.Thread(target = implementation, args = (urls[2],))
thread4 = threading.Thread(target = implementation, args = (urls[3],))
thread5 = threading.Thread(target = implementation, args = (urls[4],))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()






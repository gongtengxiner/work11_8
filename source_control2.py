# -*- coding:utf-8 -*-
# usrp_spectrum_sense_10.29_2的内容只输出到一个文本
import os
#import thread 
import threading
#thread.start_new_thread(os.system("python2 ./usrp_spectrum_sense_10.27.py -a serial=31DDABF -A RX2 -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 2e9 5e9"))
#thread.start_new_thread(os.system("python2 ./usrp_spectrum_sense_10.27_usrp2.py -a serial=31DD6FA -A RX2 -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 2e9 5e9"))

# thread.start_new_thread(os.system,("python2 ./usrp_spectrum_sense_10.27.py -a serial=31DDABF -A RX2 -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 2e9 5e9",))
# thread.start_new_thread(os.system,("python2 ./usrp_spectrum_sense_10.27_usrp2.py -a serial=31DD6FA -A RX2 -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 2e9 5e9",))

# os.system("python2 ./usrp_spectrum_sense_10.27.py -a serial=31DDABF -A RX2 -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 2e9 5e9")

# print "hello"

# os.system("python2 ./usrp_spectrum_sense_10.27_usrp2.py -a serial=31DD6FA -A RX2 -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 2e9 5e9")

def usrp1():
	os.system("python2 ./usrp_spectrum_sense_10.29.py -a serial=31DDABF -A TX/RX -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 1e9 3e9")

def usrp2():
	os.system("python2 ./usrp_spectrum_sense_10.29.py -a serial=31DD6FA -A TX/RX -s 50e6 -g 30 --tune-delay=0.005 --dwell-delay=0.005 -b 97656.25 -q 0 3e9 5e9")



thread=[]
thread.append(threading.Thread(target=usrp1))
thread.append(threading.Thread(target=usrp2))

print thread

if __name__=='__main__':
	for t in thread:
		t.start()


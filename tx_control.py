# -*- coding:utf-8 -*-
# 这里由于每个频段数据只发一次，效果不好。可以改改tx_ofdm.py让其对每次每个频段多发两次，可能会更好。

import os

def main_loop():
	filenum = 1.0
	while 1:
	 	if (filenum > 160.0) or (filenum < 1):
	 		filenum = 1.0
	 	os.system("python2 ./tx_ofdm_slow.py -n ./mydatafile/mydata%s.log"%filenum)
	 	filenum = filenum + 1
	 	#print 'mydata%s.log have done!'%filenum

if __name__ == '__main__':
	try:
		main_loop()

	except KeyboardInterrupt:
		pass


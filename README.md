
#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

import random
import time
import math
import os

#~ nalf = os.path.exists("/home/sveta/saperproga.txt")
#~ if nalf == False:
	#~ with open("/home/sveta/saperproga.txt", "w") as files:
		#~ rkkkkgklfsd = 0
l=[]
akb = 0
akm = 0

with open("/home/sveta/saperproga.txt", "r") as files:
	r = files.read().split("\n")
	per_str = r[0].split(" ")
	n = int(per_str[0])
	m = int(per_str[1])
	k = int(per_str[2])

for i in range(1,1+n):
	lstr = ["0"]*m
	l.append(lstr)

with open("/home/sveta/saperproga.txt", "r") as files:
	for noms in range(1,k+1):
		strs = r[noms].split(" ")
		sr = int(strs[0])-1
		st = int(strs[1])-1
		l[sr][st] = "*"

for vnu in l:
	akb = 0
	for vvnu in vnu:
		if vvnu == "*":
			ll = len(l[akm])
			#Снизу
			if ll >= akm+1:
				#Снизупросто
				if l[akm+1][akb] !="*":
					l[akm+1][akb] = str(int(l[akm+1][akb])+1)
				#Слева
				if akb-1>=0:
					#Слеваснизу
					if l[akm+1][akb-1] !="*":
						l[akm+1][akb-1] = str(int(l[akm+1][akb-1])+1)
					#Слевапросто
					if l[akm][akb-1] !="*":
						l[akm][akb-1] = str(int(l[akm][akb-1])+1)
				#Справа
				if akb+1>=len(l[akm]):
					#Справаснизу 
					if l[akm+1][akb+1] !="*":
						l[akm+1][akb+1] = str(int(l[akm][akb+1])+1)
					#Спрвапросто
					if l[akm][akb+1] !="*":
						l[akm][akb+1] = str(int(l[akm][akb+1])+1)
			#Сверху
			if akm-1 >= 0:
				#Сверхупросто
				if l[akm-1][akb] !="*":
					l[akm-1][akb] = str(int(l[akm-1][akb])+1)
				#Слева
				if akb+1<=len(vnu):
					#Слевасверху
					if l[akm-1][akb-1] !="*":
						l[akm-1][akb-1] = str(int(l[akm-1][akb-1])+1)
				#Справа
				if akb-1>=0:
					#Справаверху
					if l[akm-1][akb+1] !="*":
						l[akm-1][akb+1] = str(int(l[akm-1][akb+1])+1)
		akb = akb + 1
	akm = akm +1

for i in range(len(l)):
	print l[i]
 


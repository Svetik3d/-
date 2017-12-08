#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

li=[]

with open("/home/sveta/saperproga.txt", "r") as files:
	r = files.read().split("\n")
	per_str = r[0].split(" ")
	n = int(per_str[0])
	m = int(per_str[1])
	k = int(per_str[2])
	for i in range(1,1+n):
		listr = ["0"]*m
		li.append(listr)
	for noms in range(1,k+1):
		strs = r[noms].split(" ")
		sr = int(strs[0])-1
		st = int(strs[1])-1
		li[sr][st] = "*"

def plus(l,ab,am,x,y):
	if l[ab][am] == "*" and l[x][y] != "*":
		if x>-1 and y>-1:
			l [x][y]= str(int(l[x][y])+1)

for akb in range(0, len(li)):
	for akm in range(0, len(li[akb])):
		#Сверху
		plus(li,akb,akm,akb-1,akm)
		#Снизу
		plus(li,akb,akm,akb+1,akm)
		#Справа
		plus(li,akb,akm,akb,akm+1)
		#Слева
		plus(li,akb,akm,akb,akm-1)
		#СнизуСлева
		plus(li,akb,akm,akb+1,akm-1)
		#СнизуСправа
		plus(li,akb,akm,akb+1,akm+1)
		#СверхуСлева
		plus(li,akb,akm,akb-1,akm-1)
		#СверхуСправа
		plus(li,akb,akm,akb-1,akm+1)



for i in range(len(li)):
	print "".join(li[i])

# https-acmp.ru
Задания олимпиадные по программированию №234

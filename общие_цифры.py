#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# https-acmp.ru
#Задания олимпиадные по программированию №333


o = []
v = []
t = []
r =""

with open("INPUT.txt", "r") as files:
	n = files.read().split(" ")
	for i in n:
		v.append(i)

for x in v[0]:
	t = []
	for i in range(len(v)-1):
		if x in v[i+1]:
			t.append("+")
	if len(t) == len(v)-1:
		o.append(x)

o = list(set(o))
o.sort()

with open("OUTPUT.txt", "w") as filess:
	filess.write(str(len(o))+"\n")
	for i in o:
		r = r+i+" "
	filess.write(r)

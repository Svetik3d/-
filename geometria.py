#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

import math

t=[]


with open("INPUT.txt", "r") as files:
	r = files.read().split("\n")
	n = int(r[0])
	for i in range(1,n+1):
		x = int(r[i].split(" ")[0])
		y = int(r[i].split(" ")[1])
		p = []
		p.append(x)
		p.append(y)
		t.append(p)

p = []
s = []

for x, y in t:
	k = y/x
	if x>0 and y>0:
		pl = 1
		p = []
		p.append(pl)
		p.append(k)
		s.append(str(p))
	if x<0 and y>0:
		pl = 2
		p = []
		p.append(pl)
		p.append(k)
		s.append(str(p))
	if x>0 and y<0:
		pl = 3
		p = []
		p.append(pl)
		p.append(k)
		s.append(str(p))
	if x<0 and y<0:
		pl = 4
		p = []
		p.append(pl)
		p.append(k)
		s.append(str(p))
	if x==0 and y==0:
		pl = 0
		p = []
		p.append(pl)
		p.append(k)
		s.append(str(p))

s = set(s)

with open("OUTPUT.txt", "w") as filess:
	filess.write(str(len(s)))

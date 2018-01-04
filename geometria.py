#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

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

def opr(x,y):
	if x > 0 and y > 0:
		pl = 1
	if x < 0 and y > 0:
		pl = 2
	if x > 0 and y < 0:
		pl = 3
	if x < 0 and y < 0:
		pl = 4
	if x == 0 and y < 0:
		pl = 5
	if	x == 0 and y > 0 :
		pl = 6
	if	x > 0 and y == 0:
		pl = 7
	if	x < 0 and y == 0:
		pl = 8
	if x == 0 and y == 0:
		pl = 9
	return(pl)

p = []
s = []

for x, y in t:
	if x == 0 or y == 0:
		k = 0
	else:
		k = y/x
	pl = opr(x,y)
	p = []
	p.append(pl)
	p.append(k)
	s.append(str(p))

print(s)

s = set(s)


with open("OUTPUT.txt", "w") as filess:
	filess.write(str(len(s)))
print(len(s))
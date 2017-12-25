#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai
with open("INPUT.txt", "r") as files:
	r = files.read().split("\n")
	per_str = r[0].split(" ")
	d = per_str[0]
	na = per_str[1]

ni = []
n = []
ch = ""
ot = ""
os = ""
x = 1

with open("OUTPUT.txt", "w") as filess:
	filess.write(d + "|" + na + "\n")
	for i in d:
		i = ch+i
		ch = ""
		if int(i) < int(na):
			ch = i
			continue
		h = i
		break
	ch = ""
	o = int(h) % int(na)
	ots = str(int(d)/int(na))
	k = len(d)-len(str(int(h) - o))-2
	w = str(str(int(h) - o)+" "*k+" "+"|"+ "-"*len(ots) + "\n")
	filess.write("-" + w)
	k = len(w) - len(ots)-1
	filess.write("-"*k+"|" + str(ots)+"\n")
	d = str(o) + d[len(h):]
	for i in d:
		if int(d) == 0:
			break
		i = ch+i
		ch = ""
		i = str(os) + i
		if int(i) < int(na):
			ch = i
			continue
		os = int(i)%int(na)
		t = int(i) / int(na)
		t = int(t) * int(na)
		n.append(i)
		n.append(str(t))
		ni.append(n)
		n = []
		d = str(os) + d[len(i)-1:]
	for p, v in ni:
		filess.write(" "*x+p+"\n")
		filess.write(" "*x+"-"+v+"\n")
		filess.write(" "*x+"---"+ "\n")
		x = x+1
	filess.write(" "*x+"0"+ "\n")

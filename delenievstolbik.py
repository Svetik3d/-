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
	w = str(str(int(h) - o)+" "+"|"+ "----" + "\n")
	filess.write("-" + w)
	filess.write("----" + str(ots)+"\n")
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
		filess.write(p+"\n")
		filess.write("-"+v+"\n")
		filess.write("---"+ "\n")
	filess.write("0"+ "\n")

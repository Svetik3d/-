#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai
#ЗАДАЧА №278 	Вычислительная биология

with open("/home/sveta/INPUT.txt", "r") as files:
	r = files.read().split("\n")
	s = r[0]
	t = r[1]
n = 0

for b in t:
	if s[n] == b:
		n = n+1
		if n == len(s):
			break

with open("/home/sveta/OUTPUT.txt", "w") as filess:
	if len(s) == n:
		filess.write("YES")
	else:
		filess.write("NO")


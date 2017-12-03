#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai
#ЗАДАЧА №278 	Вычислительная биология

with open("/home/sveta/dnk.txt", "r") as files:
	r = files.read().split("\n")
	s = r[0]
	print s
	t = r[1]
	print t

n = 0

for b in t:
	print n
	print b
	print s[n]
	if s[n] == b:
		n = n+1
		if n == len(s):
			break

with open("/home/sveta/dnk.txt", "w") as filess:
	if len(s) == n:
		filess.write("YES")
	else:
		filess.write("NO")


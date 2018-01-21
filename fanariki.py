#!/usr/bin/env python3
# -*-coding: utf-8 -*-
import math

sk = 0

with open("INPUT.txt", "r") as files:
    t = files.read().split("\n")
    x1 = int(t[0].split(" ")[0])
    x2 = int(t[1].split(" ")[0])
    y1 = int(t[1].split(" ")[1])
    y2 = int(t[0].split(" ")[1])
    r = int(t[2])
    s = int(t[3])

d = abs(math.sqrt((x1-x2)**2+(y2-y1)**2))

if d == 0:
	o = 3.14*(r*r)
else:
	if d >= r*2:
	    sk = 3.14*(r*r)
	    o = sk*2
	else:
	    per = 2 * math.acos((r*r - r*r - d*d) / (2 * r * d))
	    sk = r*r * (per - math.sin(per))/2
	    o = 2*sk

with open("OUTPUT.txt", "w") as filess:
    if o > s:
       filess.write("YES")
    else:
        filess.write('NO')

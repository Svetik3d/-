#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai
#Задания олимпиадные по программированию  https-acmp.ru №278

import json
import requests
import datetime
import os

s = raw_input("Скажите последовательность - ")
t = raw_input("Скажите строку - ")
aki = 0
n = 0
ot = []

for b in t:
	if s[n] == b:
		n = n+1
		ot.append("YES")
if len(s) == len(ot):
	print "YES"
else:
	print "NO"

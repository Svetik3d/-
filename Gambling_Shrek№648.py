#!/usr/bin/env python
# -*-coding: utf-8 -*-
# vim: sw=4 ts=4 expandtab ai

with open("INPUT.txt", "r") as files:
    k = files.read().split("\n")
    kol = int(k[0])
    var_list = [ int(j) for j in k[1].split(" ")]

var_list = sorted(var_list)
part = int(kol/2)
shrek_list = var_list[part:]
kr_sum = sum(var_list[:part])
shrek_sum = sum(shrek_list)-kr_sum

with open("OUTPUT.txt", "w") as files_out:
    files_out.write(str(shrek_sum))

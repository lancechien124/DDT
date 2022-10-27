#!/usr/bin/env python
# -*- coding: utf-8 -*-

msg = "Hello welcome to Cathay 60th year anniversary"

def count_char(str):
    cal = {}
    full_str = str.replace(" ","")  ## Remove space
    new_str = list(full_str.upper()) ## Change to upper case
    sorted_list = sorted(new_str) ## Sorting char 
    for i in sorted_list:
        cal[i] = sorted_list.count(i) ## Caculate count & save into dict

    for ch in cal:
        print ( ch +" ", end = "")
        print (cal[ch])

if __name__ == '__main__':
    new_char = count_char(msg)
    

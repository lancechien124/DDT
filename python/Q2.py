#!/usr/bin/env python
# -*- coding: utf-8 -*-

msg = "Hello welcome to Cathay 60th year anniversary"

def count_char(str):
    cal = {}
    full_str = str.replace(" ","")
    new_str = list(full_str.upper())
    sorted_list = sorted(new_str)
    for i in sorted_list:
        cal[i] = sorted_list.count(i)
        print ( i +" ", end = "")
        print (cal[i])

if __name__ == '__main__':
    new_char = count_char(msg)
    

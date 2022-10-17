#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ =='__main__':
    nmax=50
    n = int(input('請輸入總人數：'))  
    num=[]
    j = 0
    k = 0
    m = 0

    for i in range(n):
        num.append(i+1)

    while m < n - 1:
        if num[j] != 0 : k += 1
        if k == 3:
            num[j] = 0
            k = 0
            m += 1
        j += 1
        if j == n : j = 0
 
    j = 0
    while num[j] == 0: j += 1
    print ('第%d順位'%(num[j]))
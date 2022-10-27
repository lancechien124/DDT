#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ =='__main__':
    nmax=50
    n = int(input('請輸入總人數：'))  
    num=[]
    j = 0 ## num的位置
    k = 0 ## 標示數到三
    m = 0 ## 用於迴圈記數,數三個數字記一次

    for i in range(n):
        num.append(i+1) ##產生序列並標示最初順序

    while m < n - 1: 
        if num[j] != 0 : k += 1 ## 值不為0就往下一個
        if k == 3: 
            num[j] = 0 ## 數到三就標0來skip
            k = 0  ## 歸零重新計數
            m += 1 ## 計算三次的次數 
        j += 1 ##持續移往下一個
        if j == n : j = 0 ## 當j=n 就歸0，從最前面再繼續
 
    j = 0 
    while num[j] == 0: j += 1 ## 值為0就往下一個
    print ('第%d順位'%(num[j])) ## 印出值不為0的順位

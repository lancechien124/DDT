#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

old_grade = [35,46,57,91,29]

def regrade(old):
    new = []
    for i in range(len(old)):
        y=old[i]%10
        x=old[i]//10
        new.append(y*10+x) 
    return new

if __name__ == '__main__':
    new_grad_list = regrade(old_grade)
    print (new_grad_list)

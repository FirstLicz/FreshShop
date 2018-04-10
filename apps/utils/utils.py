#!/usr/bin/env python
#-*- coding:utf-8 -*- 

__author__ = 'licz'
__time__ = '2018/4/10 9:59'


from random import randint


def VerificationCode(str_length=4):
    '''
       生成随机验证码
    '''
    seeds = '0123456789'
    str_random = ''
    for n in range(str_length):
        t = randint(0,9)
        str_random+=seeds[t]

    return str_random








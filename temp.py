# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input("enter the number:"))
sum=0
temp=n
while temp>0:
    rem=temp%10
    sum=sum+rem**3
    temp=temp/10
if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")

# -*- coding: utf-8 -*-
"""lv1_내적.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jzchyUlTO4w10aba4wQmpb1pdAMBOI0S
"""

def solution(a, b):
    answer = 0
    for i,j in zip(a,b) :
        answer += i*j
    return answer

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))
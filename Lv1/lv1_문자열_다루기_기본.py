# -*- coding: utf-8 -*-
"""lv1_문자열 다루기 기본.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y9fOVcOYY7rOPUdXalxVwCkSBfZBDgWb
"""

def solution(s):
    if len(s) in [4,6] and s.isdigit() == True :
        return True
    else :
        return False

print(solution("a234"))
print(solution("1234"))
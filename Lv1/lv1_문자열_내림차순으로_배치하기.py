# -*- coding: utf-8 -*-
"""lv1_문자열 내림차순으로 배치하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I3FXeVMwq492-WTsjOA6FeY1A-CLpGhw
"""

def solution(s):
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))
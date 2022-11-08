# -*- coding: utf-8 -*-
"""lv1_시저 암호.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXV8GEgMOUh99gh5MuWz7x6rz0ouYxvl
"""

# 내 풀이

def solution(s, n):
    s = list(s)   # 문자열 -> 리스트 변환
    answer = ''

    for i in s:
        if i.islower():    # 소문자인 경우
            if ord(i) + n > ord('z'):         # 알파벳을 일정거리(n)만큼 밀었을 때의 값이 z보다 큰 경우
                answer += chr(ord(i)-26+n)    # 알파벳의 개수만큼 빼준 후 n만큼 밀음
            else:                         # z를 넘지 않는 경우
                answer += chr(ord(i)+n)   # n만큼 밀음

        elif i.isupper():   # 대문자인 경우
            if ord(i)+n > ord('Z'):           # n만큼 밀었을 때 Z보다 큰 경우
                answer += chr(ord(i)-26+n)
            else:                             # Z를 넘지 않는 경우
                answer += chr(ord(i)+n)
        
        else:               # 공백인 경우
            answer += ' '

    return answer


print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))
print(solution("aAzZ", 25))
print(solution("yY zZ", 1))
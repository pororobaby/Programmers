# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10h9bTu5KScq_P-4Gu0wkd0QVBnjkdGS1
"""

def solution(array, commands):
    answer = []

    for i in commands :
        test = array[i[0]-1:i[1]]
        print(test)

        test.sort()
        print(test)

        answer.append(test[i[2]-1])
    
    return answer

print('answer :',solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# -*- coding: utf-8 -*-
"""lv1_키패드 누르기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ab0c2qoWipn0atvg6i9mG_erDKqmYfly
"""

def solution(numbers, hand):
    answer = ''   # 키패트를 누르는 손가락 순서
    phone = {1:[1,1], 2:[1,2], 3:[1,3],    # 키패드의 위치
             4:[2,1], 5:[2,2], 6:[2,3], 
             7:[3,1], 8:[3,2], 9:[3,3], 
             '*':[4,1], 0:[4,2], '#':[4,3]}
    lhand = '*'; rhand = '#'    # 엄지손가락의 현재 위치
    ldistance = rdistance = 0   # 거리차
    
    for i in numbers:
        # 입력할 번호가 1, 4, 7인 경우 왼쪽 엄지 사용
        if i in [1,4,7]:
            answer += 'L'
            lhand = i    
        # 입력할 번호가 3, 6, 9인 경우 오른쪽 엄지 사용
        elif i in [3,6,9]:
            answer += 'R'
            rhand = i 
        # 입력할 번호가 2, 5, 8, 0인 경우
        else:
            # 왼손엄지의 위치와 입력할 번호의 거리차
            ldistance = sum([abs(x-y) for x,y in zip(phone[lhand], phone[i])])
            # 오른손엄지의 위치와 입력할 번호의 거리차
            rdistance = sum([abs(x-y) for x,y in zip(phone[rhand], phone[i])])
            
            # 입력할 번호가 왼쪽 엄지에 더 가까운 경우
            if ldistance < rdistance:
                answer += 'L'
                lhand = i
            # 입력할 번호가 오른쪽 엄지에 더 가까운 경우
            elif ldistance > rdistance:
                answer += 'R'
                rhand = i
            # 두 엄지손가락의 거리가 같은 경우
            else :
                # 왼손잡이면 왼쪽 엄지 사용
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                # 오른손잡이면 오른쪽 엄지 사용
                else:
                    answer += 'R'
                    rhand = i

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
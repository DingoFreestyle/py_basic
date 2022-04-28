# #rock,siccsors, paper game making sample
#
# value = int(input())



# print(computer)
# print(user)
#
# print()
# if '가위' in option:
#     print('가위가 옵션안에 있습니다')
# else:
#     print('가위가 옵션안에 없습니다')

import random
computer = random.randint(0, 2)
option = ['가위', '바위', '보']

while True: #while 문 안에서 빙글빙글 돌리는 상황과 아닌 상황을 잘 이용하면 좋다
    player_value = input('가위 바위 보?')
    if player_value in option:
        print(f'{player_value}를 선택했습니다')
        break
    print('값을 정확히 입력해주세요')
print('while 문을 벗어났습니다')

# user_value =
# computer_value =
#
# if computer_value == user_value:
#     print('비겼습니다')
# elif user_value == '가위':
#     if




# print("인풋을 받다")
# print("값은")
# print(value)


# # while사용법 1 - 반복식
#
# x = 1 # <기본 조건이나 아래 조건에는 처음값만 적용
# while x < 10:
#     x = x+1
#     print(x) # 결과는 2~10까지 나열로 찍힘
#
#
#
# while  < 10:
#     print(x) # 결과는 무한반복 "1"로 나옴 그렇기에 잘 끊어주도록 식을 짜야 함
#             # break를 아래 써주면 무한반복을 막음


# if, elif 이해 예시
# if 금도끼 니도끼?:
#     구라ㄴㄴ
# elif 그럼 은도끼가 니도끼?:
#     구라ㄴㄴ
# elif 그럼 쇠도끼가 니도끼?:
#     오 착하구나 다가져라
# else 뭔데 너?


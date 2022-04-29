################## 내가 한 것 > 컴퓨터가 낸 값이 한 번 들어가면 계속 고정되어서 막혔음

# import random
#
# computer = random.randint(0, 2)
# option = ['가위', '바위', '보']
# computer_value = option[computer]
#
# player_value = input('가위 바위 보?')
# if player_value in option:
#     print(f'플레이어는 {player_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')
#     if computer_value == player_value:
#         print('비겼습니다')
#     elif player_value == '가위':
#         if computer_value == '바위':
#             print('졌습니다')
#         else:
#             print('이겼습니다')
#     elif player_value == '바위':
#         if computer_value == '보':
#             print('졌습니다')
#         else:
#             print('이겼습니다')
#     elif player_value == '보':
#         if computer_value == '가위':
#             print('졌습니다')
#         else:
#             print('이겼습니다')
# else:
#     print('가위 바위 보 중에서 입력해주세요')

############################### 튜터님의 대답

# import random
#
# option = ['가위', '바위', '보']
# computer = random.randint(0, 2)
# computer_value = option[computer]
#
# while True :
#     player_value = input('가위 바위 보?')
#     if player_value in option:
#         break
#     print('제대로 입력바람!!!')
#
#
# print(f'플레이어는 {player_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')
# if computer_value == player_value:
#     print('비겼습니다')
# elif player_value == '가위':
#     if computer_value == '바위':
#         print('졌습니다')
#     else:
#         print('이겼습니다')
# elif player_value == '바위':
#     if computer_value == '보':
#         print('졌습니다')
#     else:
#         print('이겼습니다')
# elif player_value == '보':
#     if computer_value == '가위':
#         print('졌습니다')
#     else:
#         print('이겼습니다')


 # 가위바위보 버전업!

import random

print('가위바위보를 시작합니다')
score = 1
count = 0

while True:
    option = ['가위', '바위', '보']
    computer = random.randint(0, 2)
    computer_value = option[computer]
    count += 1
    while True:
        player_value = input('가위 바위 보?')
        if player_value in option:
            break
        print('제대로 입력바람!!!')

    print(f'플레이어는 {player_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')
    if computer_value == player_value:
        print('비겼습니다')

    elif player_value == '가위':
        if computer_value == '바위':
            print('졌습니다')
            score -= 1
        else:
            score += 1
            print('이겼습니다')
    elif player_value == '바위':
        if computer_value == '보':
            print('졌습니다')
            score -= 1
        else:
            score += 1
            print('이겼습니다')
    elif player_value == '보':
        if computer_value == '가위':
            print('졌습니다')
            score -= 1
        else:
            score += 1
            print('이겼습니다')
    print(f'{count} 시도 중 현재 스코어는 {score}점')

    if score > 10:
        print('승리했습니다! 가위바위보의 신!')
        break
    elif score == 0:
        print('패배했습니다! 루저!')
        break

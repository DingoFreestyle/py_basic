################## def를 이용해서 가위바위보 버전업

import random

option = ['가위', '바위', '보']
print("가위바위보를 시작합니다")


def get_user_value():
    user_value = input("가위 바위 보?")
    if user_value in option:
        return user_value
    else:
        print("잘못 입력 하였습니다")


while True:
    computer = random.randint(0, 2)
    computer_value = option[computer]
    user_value = get_user_value()
    print(f'플레이어는 {user_value}를 선택, 컴퓨터는 {computer_value}를 선택했습니다')
    if computer_value == user_value:
        print('비겼습니다')
    elif user_value == '가위':
        if computer_value == '바위':
            print('졌습니다')

        else:
            print('이겼습니다')

    elif user_value == '바위':
        if computer_value == '보':
            print('졌습니다')

        else:
            print('이겼습니다')

    elif user_value == '보':
        if computer_value == '가위':
            print('졌습니다')

        else:
            print('이겼습니다')

import random
number = random.randint(1, 100)
# print(number) # 測試用

while True:
    guess = int(input('請輸入 1~100 的數字：'))
    if guess == number:
        print('終於猜對了!')
        break
    elif guess > number:
        print('數值比答案大')
    else:
        print('數值比答案小')



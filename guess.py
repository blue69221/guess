import random
number = random.randint(1, 100)
# print(number) # 測試用
count = 0

while True:
    guess = int(input('請輸入 1~100 的數字：'))
    count += 1
    if guess == number:
        print('終於猜對了!')
        print(f'總共猜了 {count} 次')
        break
    elif guess > number:
        print('數值比答案大')
    elif guess < number:
        print('數值比答案小')
    print(f'這是你猜的第 {count} 次')
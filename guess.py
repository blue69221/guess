import random

start =int(input('請輸入隨機數字範圍開始值：'))
end = int(input('請輸入隨機數字範圍結束值：'))

number = random.randint(start, end)
# print(number) # 測試用
count = 0

while True:
    guess = int(input(f'請輸入 {start} ~ {end} 的數字：'))
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
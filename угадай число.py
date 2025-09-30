import random
print("игра угадай значение")
print("я загадываю число от 1 до 10, а пытаешься угадать")
print("я отвечаю больше или меньше")
print("начнем?")
input()
nub = random.randint(1,10)
print("я загадал значение ")
us_nub = None
steps = 0

while us_nub != nub:
    user_vbr = input()
    us_nub =int(user_vbr)
    steps += 1
    if us_nub <= nub:
        print("Мое число больше")
    elif us_nub > nub:
        print("ты ошибся, моё число меньше")
    else:

        print("ты угадал")
print(f"ты угадал число {nub} за столько попыток {steps}" )
input()
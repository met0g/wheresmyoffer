from glob import escape

print("Введи значение")
try:
    User_vbr = int(input())
except ValueError:
    print("Ошибка: нужно ввести целое число!")
    exit()

print("Выбери что делать с значением")
print("1. Проверить на целость числа")
print("2. Положительное или отрицательное или 0")
print("3. Принадлежит ли диапазону от 10 до 50")

while True:
    try:
        inf_usr = int(input())
        if 1 <= inf_usr <= 3:
            break
        else:
            print("Ошибка: такой программы нет. Введите число от 1 до 3")
    except ValueError:
        print("Ошибка: нужно ввести число!")

if inf_usr == 1:
    # Проверка на целость (всегда true для int, но добавим для примера)
    if type(User_vbr) == int:
        print("Число целое")
    else:
        print("Число не целое")

elif inf_usr == 2:
    # Проверка на знак
    if User_vbr > 0:
        print("Положительное")
    elif User_vbr < 0:
        print("Отрицательное")
    else:
        print("Ноль")

elif inf_usr == 3:
    if 10 <= User_vbr < 50:
        print("Принадлежит диапазону")
    else:
        print("Не принадлежит диапазону")
print("нажмите на любую кнопку чтобы закрыть")
input()

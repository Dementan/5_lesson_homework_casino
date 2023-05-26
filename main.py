import random
number_comp = random.randint(1, 10)
color_comp = random.randint(1, 2)

#n - попытка пользователя, всего 5
n = 1
while n <= 5:
    number_client = int(input("Введите число от 1 до 10: "))
    color_client = int(input("Выберите цвет: введите  1 (красный) или 2(черный):"))
    n += 1
    if number_comp == number_client and color_comp == color_client:
        print("Вы выиграли!!!")
        break
    else:
        print("Ставка не выиграла((((")

if color_comp == 1:
    print(number_comp, "красный")
elif color_comp == 2:
    print(number_comp, "черный")

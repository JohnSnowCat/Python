'''
Задача 12: Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
Пример:
Ввод: 5 6 -> 2 3
'''
import math

flag = True
while (flag):
    number1 = int(input('Загадай число 1: '))
    number2 = int(input('Загадай число 2: '))
    if (number1 >= 0 and number2 >= 0 and number1 <= 1000 and number2 <= 1000):
        flag = False
    else:
        print('Введите число от 1 до 1000')
sum = number1 + number2
product = number1 * number2

# number1 * number2 = product
# number1 + number2 = sum
# number2 = sum - number1
# number1 ** 2 - sum * number1 + product = 0
discriminant = sum ** 2 - 4 * product
print(f" число 1: {int((sum + math.sqrt(discriminant))/2)}")
print(f" число 2: {int((sum - math.sqrt(discriminant))/2)}")

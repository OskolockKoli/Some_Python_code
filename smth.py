#Подсказка:
#''' - комментарии, чтобы запустить задачку, нужно удалить комментарии до и после неё

#оператор вывода (A)
'''
def f():
    print('Вася\n   пошёл\n      гулять.')

f()
'''
#оператор вывода (B)
'''
что-то странное 0_0
'''
#оператор вывода (C)
'''
def f():
    print('  *  \n *** \n*****\n * * \n *** ')

f()
'''
#линейные программы (C) (в C есть всё из A и B)
'''
def f():
    a = int(input('Первое число: '))
    b = int(input('Второе число: '))
    c = int(input('Третье число: '))

    s = a + b + c
    print('Сумма:', s)
    m = a*b*c
    print('Произведение:', m)
    m_a = (a + b + c)/ 3
    print('Среднее значение:', m_a)

f()
'''
#Операции с целыми числами (A)
'''
def f():
    n = int(input('Введите число секунд: '))
    count = 0
    a = n
    while n > 60:
        a = n % 60
        count = count + 1
        n = n - 60
    print(count, 'мин.', a, 'сек.')

f()
'''
#Операции с целыми числами (B)
'''
def f():
    n = int(input('Введите число секунд: '))
    c = 0
    b = 0
    a = n
    while n > 3600:
        a = n % 3600
        c = c + 1
        n = n - 3600
        while n > 60:
            a = n % 60
            b = b + 1
            n = n - 60
    print(c, 'часов',b, 'мин.', a, 'сек.')

f()
'''
#Операции с целыми числами (C)
'''
def f(c):
    if c == 1:
        print('9-25')
    if c == 2:
        print('10-20')
    if c == 3:
        print('11-05')
    if c == 4:
        print('12-00')
    if c == 5:
        print('12-55')
    if c == 6:
        print('13-50')
    if c == 7:
        print('14-45')
    if c < 1 or c > 7:
        print('Такого урока нет')

c = int(input('Введите номер урока: '))
f(c)
'''
#случайные числа (B) - доработанная (A)
'''
import random

def rand():
    r_num = random.randint(0, 90)
    return r_num

for i in range (0, 5):
    print(rand())
'''
#случайные числа (C)
'''
import random

def rand():
    n = 0
    r_num = random.randint(1, 6)
    print('Выпало очков:')
    print(r_num)
    n = n + r_num*100
    r_num = random.randint(1, 6)
    print(r_num)
    n = n + r_num*10
    r_num = random.randint(1, 6)
    print(r_num)
    n = n + r_num
    print ('Число', n, '\nЕго квадрат', n*n)

rand()
'''
#случайные числа (D)
'''
import random

def rand():
    r_num = random.randint(0, 999)
    print('Получено число:', r_num)
    return r_num

def f(n):
    count = 3
    while count > 0:
        if count == 3:
            a = 'Сотни: '
            print(a, *str(n))
            count = 2
        if count == 2:
            a = 'Десятки '
            print(a, *str(n))
            count = 1
        if count == 1:
            a = 'Еденицы '
            print(a, *str(n))
            count = 0
        count = count - 1

num = rand()
f(num)
'''
#Операции с вещественными числами (A)
'''
def f(n):
    a = 2048
    return a/n

n = float(input('Введите размер фото: '))
print('Поместиться фото:',f(n))
'''
#Операции с вещественными числами (B)
'''
def f(t):
    f = 44100
    k = 2
    r = 24
    i = f * k * r * t * 60 / 8 / 1024 / 1024
    return int(i + 1)

time = float(input('Введите время записи в минутах: '))
print('Размер файла:',f(time))
'''
#Операции с вещественными числами (C)
'''
def f(n):
    n = n*n
    while n > 100:
        n = n - 100
    while n > 10:
        n = n - 10
    while n > 1:
        n = n - 1
    a = n*10
    a = int(a%10)
    return a

n = float(input('Введите пароль: '))
print('Ответ:',f(n))
'''
#циклы с условием (A)
'''
def f():
    count = 0
    while True:
        n = input()
        if (not str(n).isnumeric()) or int(n) < 0:
            print("Введите именно положительное число: ")
        else:
            n = int(n)
            while n > 0:
                print('Привет!')
                n = n - 1
            break

print("Сколько раз повторить? ")
f()
'''
#циклы с условием (B)
'''
def f():
    count = 0
    while True:
        n = int(input())
        if not str(n).isnumeric():
            print("Введите именно число: ")
        else:
            while n > 0:
                if n % 10 == 1:
                    count = count + 1
                n//=10
            break
    return count

print("Введите число? ")
print('Едениц:', f())
'''



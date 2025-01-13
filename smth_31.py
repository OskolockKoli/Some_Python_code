
#1
'''
def f1():
    while True:
        try:
            n = int(input("Введите количество элементов списка: "))
            if n > 0:
                break
            else:
                print("Ошибка: Количество элементов должно быть положительным числом.")
        except ValueError:
            print("Ошибка: Введенное значение не является целым числом.")

    input_list = []
    for i in range(n):
        while True:
            try:
                element = int(input(f"Введите элемент {i+1}: "))
                input_list.append(element)
                break
            except ValueError:
                print("Ошибка: Введенное значение не является целым числом. Попробуйте снова.")

    unique_list = []
    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

result = f1()
print("Уникальные элементы:", result)
'''
#2
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f2(minimum, maximum):
    primes = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            primes.append(num)
    return primes

while True:
    try:
        min_num = int(input("Введите минимальное целое число: "))
        max_num = int(input("Введите максимальное целое число: "))
        break
    except ValueError:
        print("Ошибка: Введенное значение не является целым числом. Попробуйте снова.")

if min_num > max_num:
    print("Ошибка: Минимальное число больше максимального.")
else:
    result = f2(min_num, max_num)
    print("Простые числа в заданном диапазоне:", result)
'''
#3
'''
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx**2 + dy**2)

point1 = Point(3, 4)
point2 = Point(6, 8)

print("Координаты точки 1:", point1.get_coordinates())
print("Координаты точки 2:", point2.get_coordinates())

distance = point1.distance_to(point2)
print("Расстояние между точками 1 и 2:", distance)

new_x, new_y = 5, 7
point1.set_coordinates(new_x, new_y)
print("Новые координаты точки 1:", point1.get_coordinates())
'''
#4
'''
def f4(strings):
    sorted_by_length_asc = sorted(strings, key=len)
    print("Сортировка по возрастанию длины строк:", sorted_by_length_asc)
    sorted_by_length_desc = sorted(strings, key=len, reverse=True)
    print("Сортировка по убыванию длины строк:", sorted_by_length_desc)

strings = ["строка1", "строка", "строкаааа", "строк", "строка2"]
print("Исходный список строк:", strings)
f4(strings)
'''

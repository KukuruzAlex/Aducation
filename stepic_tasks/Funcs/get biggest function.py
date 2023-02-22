# возвращает наибольшее число, которое можно составить из чисел из списка numbers.
# Если список numbers пуст, функция должна вернуть число -1
import random
import math
def get_biggest(numbers):
    if numbers:
        max_len = len(str(max(numbers)))
        numbers.sort(key=lambda x: str(x) * max_len, reverse=True)
        return int("".join(map(str, numbers)))
    return -1



print(get_biggest([1, 2, 3]) == 321)
print(get_biggest([7, 71, 72]) == 77271)
print(get_biggest([0, 0, 0, 0, 0, 0]) == 0)
print(get_biggest([]) == -1)
print(get_biggest([72, 7274]) == 727472)
print(get_biggest([62, 626]) == 62662)
print(get_biggest([953, 9534]) == 9539534)
print(get_biggest([262, 26]) == 26262)
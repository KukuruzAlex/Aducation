# возвращает строку, полученную путем объединения подходящего существительного из кортежа и числа
def choose_plural(amount, declensions):
    if (amount % 100 in (tuple(range(10, 21)))) or str(amount).endswith("0"):
        return f"{amount} {declensions[2]}"
    elif amount % 10 in (tuple(range(5, 10))):
        return f"{amount} {declensions[2]}"
    elif amount % 10 in (2, 3, 4):
        return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[0]}"



print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(23424157, ('огурец', 'огурца', 'огурцов')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))




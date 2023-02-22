# возвращает строку в верхнем регистре,если больше символов верхнего регистра и наоборот, в нижнем если равное кол-во
def convert(string):
    up_ltr = 0
    lo_ltr = 0
    for i in string:
        if i.isalpha() and (128 <= ord(i) <= 159 or 65 <= ord(i) <= 90):
            up_ltr += 1
        elif i.isalpha() and (160 <= ord(i) <= 191 or 97 <= ord(i) <= 122):
            lo_ltr += 1
    if up_ltr > lo_ltr:
        return string.upper()
    elif up_ltr < lo_ltr:
        return string.lower()
    elif up_ltr == lo_ltr:
        return string.lower()


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))
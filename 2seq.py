# elements = input('Введите числа через запятую ')
# numb_shift = elements.split(',')
# print(set(numb_shift))

elements = input('Введите числа через запятую ')
numb_shift = elements.split(',')
numb = []
for number in numb_shift:
    if numb_shift.count(number) == 1:
        numb.append(number)
print(numb)

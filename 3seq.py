elements = input('Введите список чисел через запятую ')
numb_shift = elements.split(',')
elements = input('Введите  второй список чисел через запятую ')
sec_numb_shift = elements.split(',')
for numb in numb_shift:
    if numb in sec_numb_shift:
        numb_shift.remove(numb)
print(numb_shift)

elements = input('Введите список чисел через запятую ')
numb_shift = elements.split(',')
elements = input('Введите  второй список чисел через запятую ')
sec_numb_shift = elements.split(',')
for numb in numb_shift[:]:
    if numb in sec_numb_shift:
        numb_shift.remove(numb)
print(numb_shift)
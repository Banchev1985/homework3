elements = int(input('Введите количество элементов '))

n_elem = []
for i in range(elements):
    num = int(input('Введите число '))
    n_elem.append(num)

n_elem.sort()
print(n_elem)
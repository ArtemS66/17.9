def sortirovka(): #функция сортировки по возрастанию
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right): #функция бинарного поиска для нахождения индекса искомого элемента
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element and array[middle + 1] >= element :
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

try:
    array = list(map(int, input("Введите список целых чисел: ").split()))
except ValueError as e:
    print('Введите целые числа')
    array = list(map(int, input("Введите список чисел: ").split()))

try:
    element = int(input("Введите целое чило для поиска: "))
except ValueError as e:
    print('Введите целое число')
    element = int(input("Введите целое чило для поиска: "))
else:
    print(f'Список отсортирован по возростанию {sortirovka()}')
finally:
    rightgran = len(array)
    print(f'Номер позиции искомого элемента - {binary_search(array, element, 0, rightgran) + 1}, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.')



def bin_heap(mas, n, i):
    """
    Двоичная куча
    
    :param mas: Массив на отсортировку
    :type mas: list
    :param n: Длина массива
    :type n: int
    :param i: Индекс максимального элемента дерева
    :type i: int
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and mas[largest] < mas[left]:
        largest = left
    if right < n and mas[largest] < mas[right]:
        largest = right

    if largest != i:
        mas[i], mas[largest] = mas[largest], mas[i]
        bin_heap(mas, n, largest)

def heap(mas):
    """
    Пирамидальная сортировка

    :param mas: Массив на отсортировку
    :type mas: list 
    """
    n = len(mas)

    for i in range(n, -1, -1):
        bin_heap(mas, n, i)

    for i in range(n-1, 0, -1):
        mas[i], mas[0] = mas[0], mas[i]
        bin_heap(mas, i, 0)
    return mas

#mas = [4, 5, 9, 2, 1, 8, 6] 
#print(heap(mas))
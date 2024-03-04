def insert(mas):
    """
    Сортировка вставками
    
    :param mas: Массив на отсортировку
    :type mas: list 
    """
    for i in range(1, len(mas)):
        k = i - 1
        tmp = mas[i]
        while k >= 0 and mas[k] > tmp:
            mas[k + 1] = mas[k]
            k -= 1
        mas[k + 1] = tmp
    return mas

#mas = [3, 1, 6, 1, 9, 100, 3, 7, 6] 
#print(insert(mas))
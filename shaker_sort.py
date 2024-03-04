def shaker(df):
    """
    Шейкерная сортировка
    
    :param mas: Массив на отсортировку
    :type mas: list 
    """
    high = 0
    low = len(df)-1 
    while (high < low):
        for i in range(high, low):
            if df[i] > df[i + 1]:
                df[i], df[i + 1] = df[i + 1], df[i]
        low -= 1
        for i in range(low, high, -1):
            if df[i] < df[i - 1]:
                df[i], df[i - 1] = df[i - 1], df[i]
        high += 1
    return df
        

#mas = [3, 1, 6, 1, 9, 100, 3, 7, 6] 
#print(shaker(mas))
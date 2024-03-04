import pandas as pd
import time
import matplotlib.pyplot as plt

from shaker_sort import shaker
from heap_sort import heap
from insert_sort import insert

class People:
    """
    Класс информации о жителях и их месте проживания

    :param name: Полное ФИО
    :type name: str
    :param street: Название улицы проживания
    :type street: str
    :param building: Номер дома
    :type building: int
    :param flat: Номер квартиры
    :type flat: int
    :param date_of_birth: Дата рождения
    :type date_of_birth: str
    """
    def __init__(self, name:str, street:str, building:int, flat:int, date_of_birth:str):
        """
        Конструктор
        """
        self.name = name
        self.street = street
        self.building = building
        self.flat = flat
        self.date_of_birth = date_of_birth
    
    def __eq__(self, other):
        """
        Пегрузка оператора равенства

        :param other: Объект класса People
        :type  other: People
        """
        return (self.name == other.name and self.street == other.street and
            self.building == other.building and self.flat == other.flat and
            self.date_of_birth == other.date_of_birth)
    
    def __lt__(self, other):
        """
        Пегрузка оператора меньше

        :param other: Объект класса People
        :type  other: People
        """
        return ((self.street < other.street) or 
            (self.street == other.street and self.building < other.building) or
            (self.street == other.street and self.building == other.building and self.flat < other.flat) or
            (self.street == other.street and self.building == other.building and self.flat == other.flat and self.name < other.name) or
            (self.street == other.street and self.building == other.building and self.flat == other.flat and self.name == other.name and self.date_of_birth < other.date_of_birth))
    
    def __le__(self, other):
        """
        Пегрузка оператора меньше или равно

        :param other: Объект класса People
        :type  other: People
        """
        return (self < other or self == other)
    
    def __gt__(self, other):
        """
        Пегрузка оператора больше

        :param other: Объект класса People
        :type  other: People
        """
        return (not (self < other))
    
    def __ge__(self, other):
        """
        Пегрузка оператора больше или равно
        
        :param other: Объект класса People
        :type  other: People
        """
        return ((not (self < other)) or self == other)
        

df_1 = pd.read_csv('data_1.csv') #200
df_2 = pd.read_csv('data_2.csv') #500
df_3 = pd.read_csv('data_3.csv') #1000
df_4 = pd.read_csv('data_4.csv') #5000
df_5 = pd.read_csv('data_5.csv') #10000
df_6 = pd.read_csv('data_6.csv') #50000
df_7 = pd.read_csv('data_7.csv') #100000
df_8 = pd.read_csv('data_8.csv') #150000

def df_to_mas(df):
    tmp = []
    for i in range(len(df)):
        tmp.append(People(df['name'][i], df['street'][i], df['building'][i], df['flat'][i], df['date_of_birth'][i]))
    return tmp

dfs = [df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8]
mass = []
length = []
for i in dfs:
    mass.append(df_to_mas(i))
    length.append(len(i))

shaker_times = []
for (i, mas) in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    shaker(tmp)
    shaker_times.append(time.time() - start)    
    with open(f'shaker_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.name} {elem.street} {elem.building} {elem.flat} {elem.date_of_birth}\n')
print(shaker_times)
plt.semilogy(length, shaker_times, ':o', label="Shaker_sort")

insert_times = []
for (i, mas) in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    insert(tmp)
    insert_times.append(time.time() - start)    
    with open(f'insert_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.name} {elem.street} {elem.building} {elem.flat} {elem.date_of_birth}\n')
print(insert_times)
plt.semilogy(length, insert_times, ':o', label="Insert_sort")

heap_times = []
for (i, mas) in enumerate(mass):
    tmp = mas[:]
    start = time.time()
    heap(tmp)
    heap_times.append(time.time() - start)    
    with open(f'heap_{i+1}.txt', 'w') as f:
        for elem in tmp:
            f.write(f'{elem.name} {elem.street} {elem.building} {elem.flat} {elem.date_of_birth}\n')
print(heap_times)
plt.semilogy(length, heap_times, ':o', label="Heap_sort")
plt.legend()
plt.show()
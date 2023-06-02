import math

d = float(input('Введите диаметр в сантиметрах: '))
lenght = float(input('Введите длину в метрах: '))
summ_volume = 0

def metr(numb):
    numb /= 100
    return numb
def volume(lenght, D):
    R = D / 2
    S = math.pi * R ** 2
    Volume = lenght * S
    return Volume

while d != 0 and lenght != 0:
    summ_volume += round(volume(lenght, metr(d)), 4)
    print('Кубатура с единицы:', round(volume(lenght, metr(d)), 4))
    print('Общая кубатура:', summ_volume, end = '\n\n')
    d = float(input('Введите диаметр в сантиметрах: '))
    lenght = float(input('Введите длину в метрах: '))
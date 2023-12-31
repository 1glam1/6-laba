import numpy as np

def matrix(n):
    M = np.ones([n, n]) # Создаем матрицу
    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                mij = input('Введите коэффициент сравнения критерия {0} и критерия {1}: '.format(i,j))
                M[i, j] = float(mij)
                M[j, i] = 1 / float(mij)  # Добавление обратных элементов (под главной диагональю)
    
    vector = np.linalg.eig(M)[1][:, 0] # Вычисление собственного вектора матрицы M

    norm_vector = vector / vector.sum() # пронормируем вектор
    return norm_vector

while True: # Проверка ввода количества критерий
    try:
        number = int(input('Введите количество критериев: ')) 
        while True: # Проверка ввода коэффициента
            try:
                norm_vector = matrix(number) 
                # выводим результат
                print('Весовые коэффициенты')
                for x in range(len(norm_vector)): 
                    res = norm_vector[x]
                    print(f'{res:.2f}'[:-6]) # округление до сотых
                break
            except ValueError: 
                print('Введите число(без символов)!')
        break
    except ValueError:
        print('Введите число(без символов)!')

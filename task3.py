def Fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return Fibo(n-1)+Fibo(n-2)

try:
    _n = int(input('Введите номер числа Фибоначчи: '))
except:
    print('Номер числа должен быть целым числом')
else:
    if _n<1.0: print('Номер числа не может быть отрицательным')
    else: print(f'Число Фабоначчи с номером {_n}: {Fibo(_n)}')
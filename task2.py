def summ_of_all(*args):
    sum = 0
    for elem in args:
        sum += elem
    return sum

print(summ_of_all(1,2,3,4,5,6))
print(summ_of_all())
print(summ_of_all(23,25))
print(summ_of_all(3.0,2.0))
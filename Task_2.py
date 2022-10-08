#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#вывод списком
num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")

#вывод формулой
def factors(num, d=2):    
    while num > 1:
        n1, n2 = divmod(num, d)
        if n2:
            d += 1
        else:
            yield d
            num = n1
n = int(input("Введите натуральное число: "))
print('{} = {}' .format(n, ' * '.join(map(str, factors(n)))))

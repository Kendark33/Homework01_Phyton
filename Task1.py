# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

Number = int(input("Введите трехзначное число: "))
if Number > 99 and Number < 1000:
    asd = Number % 10
    Number = Number // 10
    b = Number % 10
    a = Number // 10
    result = a + b + asd
    print(f'Сумма цифр {a} + {b} + {asd} равна: {result}')
else:
    print("Не трехзначное число")
profit = int(input("Введите выручку фирмы: "))
loss = int(input("Введите издержки фирмы: "))
bal = profit-loss
marg = profit / loss
if profit > loss:
    print(f"Прибыль равна: {bal} ")
    print(f"Рентабельность равна: {marg}")
    size = int(input("Введите численность сотрудников компании: "))
    print(f"Прибыль в расчете на одного сотрудника равна: {bal/size}")
elif profit < loss:
    print(f"Убыток равен: {bal}")
else:
    print("Компания работает в ноль")
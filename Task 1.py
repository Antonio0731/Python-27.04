number_a = int(input('Введите число А: '))
number_b = int(input("Введите число B: "))
operator = str(input("Укажите математическое действие, которое необходимо произвести: "))
res_1 = number_a + number_b
res_2 = number_a - number_b
res_3 = number_a * number_b
res_4 = number_a / number_b

if operator == "+":
    print(res_1)
elif operator == "-":
    print(res_2)
elif operator == "*":
    print(res_3)
elif operator == "/":
    print(res_4)
else:
    print("Введите корректный оператор")
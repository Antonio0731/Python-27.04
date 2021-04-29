main = int(input("Введите любое число от 1 до бесконечности: "))
num = main % 10
main = main // 10
while main > 0:
    if main % 10 > num:
        num = main % 10
    main = main // 10
print(num)
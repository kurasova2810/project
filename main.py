a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = str(input('Выберите число которое обозначает действие которое вы хотите выполнить:'
      '\n1.сумма чисел '
      '\n2.разность чисел '
      '\n3.произведение чисел '
      '\n4.деление '
      '\n5.замена чисел '
      '\n0.выход'))
while c > '0':
    if c == '1':
        print(a+b)
    if c == '2':
        print(a-b)

    if c == '3':
        print(a*b)

    if c == '4':
        try:
            print(a / b)
        except ZeroDivisionError:
                print('Делить на ноль нельзя!')


    if c == '5':
        f = input('Какое число вы хотите заменить?')
        if f == '1':
            a = int(input('Введите первое число: '))
        if f == '2':
            b = int(input('Введите второе число: '))
        else:
            print('Введите другое число')
    c = input('Выберите число которое обозначает действие которое вы хотите выполнить:'
                '\n1.сумма чисел '
                '\n2.разность чисел '
                '\n3.произведение чисел '
                '\n4.деление '
                '\n5.замена чисел '
                '\n0.выход')
    if c == '0':
        break




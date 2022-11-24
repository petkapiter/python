i = 0
while i < 6:
    i += 1
    if i == 3:
        print('Пропускаем 3')
        continue
        print('Этого никто не увидет')
    else:
        print("Текущее значение {}".format(i))
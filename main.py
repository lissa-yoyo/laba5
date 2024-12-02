string1 = input("Введите первую строку: \n")
string2 = input("Введите вторую строку: \n")
if string1 == "" or string2 == "":
    exit("Вы ввели пустую строку")
else:
    res = set(string1) - set(string2)
    print("Символы, которые встречаются в первой строке, но не встречаюся во второй:")
    print(*res)

res1 = set(string1) & set(string2)
if len(res1) == 0:
    print("Совпадений не найдено")
else:
    res1 = sorted(res1)
    print("Числа, которые встречаются в обоих наборах чисел: ")
    print(*res1)
string1 = input("Введите первую строку: \n")
string2 = input("Введите вторую строку: \n")
if string1 == "" or string2 == "":
    exit("Вы ввели пустую строку")
else:
    res = set(string1) - set(string2)
    print("Символы, которые встречаются в первой строке, но не встречаюся во второй:")
    print(*res)
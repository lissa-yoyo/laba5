from random import randint, choice

print(
    "Добро пожаловать в игру!\nПравила:\nКаждый игрок берет по 1, 2 или 3 камня.\nПроигрывает тот, кто берет последний камень")
n = randint(4, 30)
print(f"В куче {n} камней")
user_fl = choice([True, False])
print(f"Первым ходит{'е вы' if user_fl else ' компьютер'}")
while n > 1:
    if user_fl:
        user_p = input(f"Сколько камней возьмете?\nОсталось {n}\n")
        try:
            user_p = int(user_p)
        except:
            exit("Вы ввели не число!")
        if user_p not in [1, 2, 3] or user_p > n:
            print("Неверный ход! Поробуйте снова")
            continue
    else:
        if n % 4 != 0:
            user_p = n % 4
        else:
            user_p = randint(1, min(3, n))
        print(f"Компьютер берет {user_p} камней")
    n -= user_p
    if n == 1:
        print(f"{'Вы выйграли!' if user_fl else 'Компьютер выйграл!'}")
        break
    user_fl = not user_fl

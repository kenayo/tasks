# Римский А.А. swordscream@yandex.ru

from game import Game

if __name__ == "__main__":

    try:
        # Создаем и запускаем игру
        g = Game()
        g.run()

    except Exception as err:
        print("Возникла ошибка: ", err, "\nИгра будет закрыта.")

# -------------
# Пример вывода (в режиме options.debug = True - карты видны):

# ==================================================
# Добро пожаловать игру "Набери наибольшую сумму"!
# Выбирайте случайную карту со стола и соревнуйтесь!
# ==================================================
# Введите кол-во карт [2; 36] и игроков [2; 5] через пробел: 6 3
# Имя игрока №1: Вася
# Имя игрока №2: Коля
# Имя игрока №3: Маша

# Игра началась!
# Карты на столе (6): 5 4 2 6 3 1
#  Выбирает Вася: 1
# Карты на столе (5): 4 2 6 3 1
#  Выбирает Коля: 3
# Карты на столе (4): 4 2 3 1
#  Выбирает Маша: 4
# Счет: Вася - 5, Коля - 6, Маша - 1
# Карты на столе (3): 4 2 3
#  Выбирает Вася: 2
# Карты на столе (2): 4 3
#  Выбирает Коля: 2
# Карты на столе (1): 4
#  Выбирает Маша: 1
# Счет: Вася - 7, Коля - 9, Маша - 5
#
# Игра закончена!
# Счет: Коля - 9, Вася - 7, Маша - 5

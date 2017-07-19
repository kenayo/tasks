# Римский А.А. swordscream@yandex.ru

from card_list import CardList


class Player:
    """Класс Player представляет игрока.

    Атрибуты экземпляра класса:
      - self.name (str): имя игрока;
      - self.card_list (CardList): выбранные карты игрока.

    Методы экземпляра класса:
      - add_card(): добавляет карту в выбранные;
      - make_choice(): возвращает индекс выбранной игроком карты.
    """

    def __init__(self, name):
        """Инициализация игрока.

        Параметры:
          - name (str): имя игрока.

        В процессе инициализации необходимо:
          - запомнить имя игрока;
          - инициализировать набор карт.
        """
        self.name = name
        self.card_list = CardList()

    def __str__(self):
        """Вернуть строковое представление класса.

        Формат: 'Имя [выбранные карты] сумма', например,
                'Иван [1 2 5] 8'.
        """
        return '{} [{}] {}'.format(self.name, str(self.card_list),
                                   self.card_list.sum())

    def add_card(self, card):
        """Добавить карту 'card' в выбранные.

        Для игрока карта должна быть открытой (лицом вверх).
        """
        card.turn_face()
        self.card_list.append(card)

    def make_choice(self):
        """Вернуть номер карты, выбранной игроком (int).

        Номер вводится с клавиатуры (первая карта - номер 1).
        """
        return int(input())

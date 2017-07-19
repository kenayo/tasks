# Римский А.А. swordscream@yandex.ru

from card import Card
from card_list import CardList
import options


class CardTable:
    """Класс CardTable представляет игорный стол.

    Умеет:
      - хранить карты, лежащие на столе;
      - "отдавать" карту;
      - определять - пуст или нет.

    Атрибуты экземпляра класса:
      - self._card_list (CardList): набор карт на столе.

    Методы экземпляра класса:
      - self.take_card(): берет карту со стола;
      - self.is_empty(): True, если на слоле нет карт.

    Свойства:
      - card_count (int): количество карт на столе.
    """

    def __init__(self, cards_count):
        """Инициализация стола.

        Параметры:
          - cards_count (int): количество карт для игры.

        При инициализации стола происходит генерация набора
        из 'cards_count' карт (номерами от 1 до 'cards_count').
        Если options.debug == True, карты должны быть лицом вверх.
        После генерации их необходимо перемешать -
        используйте self._card_list.shuffle().

        Необходимо удостовериться, что 'cards_count' > 1.
        """
        assert cards_count > 1, 'Мало карт'
        self._card_list = CardList()
        for i in range(cards_count):
            card = Card(i + 1)
            if options.debug is True:
                card.turn_face()
            self._card_list.append(card)
        self._card_list.shuffle()

    def __str__(self):
        """Вернуть строковое представление карт на столе.

        Формат:

        Карты на столе (3): X X X
        """
        return 'Карты на столе ({}): {}'.format(len(self._card_list),
                                                str(self._card_list))

    def take_card(self, index):
        """Взять (вернуть) со стола одну карту под номером 'index'.

        Параметры:
          - 'index' - номер карты, начиная с 1.

        Исключения:
          - IndexError: если не 1 <= index <= card_count.
        """
        if index < 1 or index > self.card_count:
            raise IndexError('index должен быть между 1 и card_count')
        return self._card_list.pop(index - 1)

    def is_empty(self):
        """Вернуть True, если на столе нет карт."""
        return self._card_list.is_empty()

    @property
    def card_count(self):
        """Вернуть количество карт на столе."""
        return len(self._card_list)


if __name__ == "__main__":
    tb = CardTable(5)
    print(tb)

# Римский А.А. swordscream@yandex.ru

class Card:
    """Класс Card представляет игральную карту.

    Поля экземпляра класса:
      - self._value (int): значение карты;
      - self.is_face (bool): True, если карта лежит лицом вверх.

    Методы экземпляра класса:
      - self.turn_face(): переворачивает карту лицом вверх.
      - self.turn_back(): переворачивает карту рубашкой вверх.

    Атрибуты класса:
      - BACK (str): рубашка карты.

    Свойства:
      - value (int): значение карты (только для чтения).
    """

    BACK = "X"

    def __init__(self, value):
        """Инициализация класса-карты.

        По умолчанию карта должна быть рубашкой вверх (лицом вниз).

        Параметры:
          - value (int): значение карты.

        Необходимо удостовериться, что 'value' - int (assert).
        """
        assert isinstance(value, int), 'value должно быть int'
        self._value = value
        self.is_face = False

    def __str__(self):
        """Вернуть строковое представление карты.

        Если карта рубашкой вниз, вернуть значение, иначе 'BACK'.
        """
        if self.is_face is False:
            return Card.BACK
        else:
            return str(self._value)

    def turn_face(self):
        """Перевернуть карту лицом вверх."""
        self.is_face = True

    def turn_back(self):
        """Перевернуть карту рубашкой вверх."""
        self.is_face = False

    @property
    def value(self):
        """Вернуть значение карты."""
        return self._value

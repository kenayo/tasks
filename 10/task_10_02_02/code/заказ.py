# Римский А.А. swordscream@yandex.ru
import time


class Заказ:
    """Класс Заказ содержит информацию о заказе."""

    # Переменная класса для определения номера заказа
    счетчик_заказов = 0

    def __init__(self):
        """Конструктор класса."""
        # Хранит экземпляры класса Пицца и его потомков
        self.заказанные_пиццы = []
        Заказ.счетчик_заказов += 1

    def __str__(self):
        """Вернуть содержимое заказа и его сумму.

        Формат вывода:

        Заказ №2
        1. Пицца: Пепперони | Цена: 350.00 р.
           Тесто: тонкое Соус: томатный
           Начинка: пепперони, сыр моцарелла
        2. Пицца: Барбекю | Цена: 450.00 р.
           Тесто: тонкое Соус: барбекю
           Начинка: бекон, ветчина, зелень, сыр моцарелла
        Сумма заказа: 800.00 р.

        """
        res = 'Заказ №{}\n'.format(Заказ.счетчик_заказов)
        for i in self.заказанные_пиццы:
            k = self.заказанные_пиццы.index(i)
            if self.заказанные_пиццы.index(i) < 10:
                res += str(k + 1) + '. ' + str(i) + '\n'
            else:
                res += str(k + 1) + '.' + str(i) + '\n'
        res += 'Сумма заказа: {0:.2f} p.'.format(self.сумма())
        return res

    def добавить(self, пицца):
        """Добавить пиццу в заказ."""
        self.заказанные_пиццы.append(пицца)

    def сумма(self):
        """Вернуть сумму заказа."""
        деньги = 0
        for i in self.заказанные_пиццы:
            деньги += i.цена
        return деньги

    def выполнить(self):
        """Выполнить заказ.

        Для каждой пиццы в заказе: подготовить, испечь, нарезать и упаковать.
        Сообщить, что заказ готов и пожелать приятного аппетита.

        Для визуального эффекта, каждое действие осуществляется с "задержкой",
        используя time.sleep(1).

        Формат вывода:

        Заказ поступил на выполнение...
        1. Пепперони
        Начинаю готовить пиццу Пепперони
          - замешиваю тонкое тесто...
          - добавляю соус: томатный...
          - и, конечно: пепперони, сыр моцарелла...
        Выпекаю пиццу... Готово!
        Нарезаю на аппетитные кусочки...
        Упаковываю в фирменную упаковку и готово!

        Заказ №2 готов! Приятного аппетита!
        """
        print('\nЗаказ поступил на выполнение...')

        for i in self.заказанные_пиццы:
            if self.заказанные_пиццы.index(i) < 10:
                print(str(self.заказанные_пиццы.index(i) + 1) +
                      '. ' + str(i.название))
            else:
                print(str(self.заказанные_пиццы.index(i) + 1) +
                      '.' + str(i.название))
            print(i.подготовить())
            time.sleep(1)
            print(i.испечь())
            time.sleep(1)
            print(i.нарезать())
            time.sleep(1)
            print(i.упаковать())
            time.sleep(1)
        print('\n')
        print('Заказ №{} готов! Приятного аппетита!'.
              format(Заказ.счетчик_заказов))

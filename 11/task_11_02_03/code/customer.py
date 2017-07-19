# Римский А.А. swordscream@yandex.ru

import re
import datetime


class Customer:
    """Класс Customer представляет клиента.

    Атрибуты экземпляра класса:
      - self.info: словарь-информация о клиенте; содержит следующие ключи:
        - f (str): фамилия клиента;
        - i (str): имя клиента;
        - o (str): отчество клиента;
        - birthday (datetime.date): дата рождения;
        - polis_type (str): тип полиса;
        - polis_price (int): цена оформленного полиса.
    """

    def __init__(self, info):
        """Инициализация класса.

        Аргументы:
          - info (dict): словарь-информация о клиенте (формата 'self.info')

        Необходимые проверки:
          - info - словарь и содержит необходимые ключи;
          - значения в словаре имеют нужный тип.

        Исключения:
          - ValueError - если не все проверки успешны.

        Действия:
          - установить self.info;
          - Ф, И, О и тип полиса должны быть с большой буквы.
        """

        try:
            assert 'f' in info
            assert 'i' in info
            assert 'o' in info
            assert 'birthday' in info
            assert 'polis_type' in info
            assert 'polis_price' in info
        except Exception as e:
            raise ValueError('В словаре нет необходимого ключа, ошибка:', e)

        try:
            assert type(info['f']) == str
            assert type(info['i']) == str
            assert type(info['o']) == str
            assert type(info['birthday']) == datetime.date
            assert type(info['polis_type']) == str
            assert type(info['polis_price']) == int
        except Exception as e:
            raise ValueError('Некорректный формат данных, ошибка:', e)

        for i in ['f', 'i', 'o', 'polis_type']:
            info[i] = info[i].capitalize()

        self.info = info

    def __str__(self):
        """Вернуть строковое представление клиента.

        Формат:
          'Крутов Олег Павлович 13/01/1973 Транспорт 50,000 руб.'.

        Для вывода суммы с разделителем тысяч используйте заполнитель {:,}.
        """
        newstr = self.info['f'] + ' '
        newstr += self.info['i'] + ' '
        newstr += self.info['o'] + ' '
        newstr += datetime.datetime.strftime(self.info['birthday'],
                                             '%d/%m/%Y') + ' '
        newstr += self.info['polis_type'] + ' '
        newstr += '{:,} руб.'.format(self.info['polis_price'])
        return newstr

    @classmethod
    def from_string(cls, str_value):
        """Создать и вернуть экземпляр класса Customer из строки 'str_value'.

        1. Используя регулярное выражение, проверить, что 'str_value' содержит
           информацию о клиенте:
              - ФИО клиента в произвольном регистре; в качестве разделителя
                может быть использован пробел или знак табуляции;
              - Дата рождения:
                    - день и месяц могут быть указаны с наличием/отсутствием
                      ведущего 0;
                    - год может содержать 2 или 4 цифры;
                    - в качестве разделителя может быть использован
                      '.', '/' или '-'.
              - Тип полиса: "Транспорт", "Недвижимость",
                            "Путешествия" или "Здоровье";
              - Сумма: целое число.

              Пример: 'Крутов Олег Павлович 13/01/1973 Транспорт 50,000 руб.'

           Неплохим вариантом будет использовать именованные аргументы,
           совпадающие с ключами в 'self.info', таким образом, их будет просто
           получить через 'match.groupdict()'.

           Возбудить ValueError, если не удается получить информацию из строки.

        2. При обнаружении информации, сформировать словарь найденных данных:
           - откорректировать год до 4-х знаков;
           - все числовые значения преобразовать в соответствующие типы.

        3. Создать экземпляр класса и вернуть в качестве результата.
        """
        try:
            regex_str = r'^[\s]*(?P<f>\w+)[\s]+(?P<i>\w+)+[\s]+'\
                        r'(?P<o>\w+)+[\s]+(?P<birthday>[0-9]{1,2}'\
                        r'[./-][0-9]{1,2}[./-][0-9]{2,4})[\s]+'\
                        r'(?P<polis_type>Путешествия|Здоровье|'\
                        r'Недвижимость|Транспорт)[\s]+(?P<polis_price>'\
                        r'[\d]+[,]*[\d]*)$'
            match_str = re.search(regex_str, str_value, re.I)
            dict_value = match_str.groupdict()
        except Exception as e:
            raise ValueError('Не удается получить информацию из строки,'
                             'ошибка:', e)

        try:
            regex_date = r'(?P<day>\d{1,2})[.\-\/](?P<month>\d{1,2})'\
                         r'[.\-\/](?P<year>\d{2,4})'
            match_date = re.search(regex_date, dict_value['birthday'])
            day, month, year = match_date.groups()
            day = int(day)
            month = int(month)
            year = int(year)
            if year < 100:
                year += 1900
            dict_value['birthday'] = datetime.date(year, month, day)
        except Exception as e:
            raise ValueError('Не удалось преобразовать дату рождения,'
                             'ошибка:', e)

        symbs = [',', '.']
        for sym in symbs:
            dict_value['polis_price'] = dict_value['polis_price'].\
                                        replace(sym, '')
        dict_value['polis_price'] = int(dict_value['polis_price'])

        return Customer(dict_value)

    def __getattr__(self, key):
        """Вернуть значение атрибута 'key'.

        Благодаря специальному методу '__getattr__' обращение к
        характеристике клиента, например, фамилии будет выгляеть
        как
           Customer.f,
        вместо
           Customer.info['f']
        т.е. нет необходимости объявлять отдельные методы/свойства для
        "красивого" доступа к значениям 'self.info'.
        """
        if key in self.info:
            return self.info[key]
        raise AttributeError(key)

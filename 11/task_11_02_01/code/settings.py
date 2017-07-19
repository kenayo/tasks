# Римский А.А. swordscream@yandex.ru

import json
import datetime
import re
import sys
import os.path


class Settings:
    """Класс Settings хранит настройки приложения.

    Атрибуты класса:
      - DATETIME_FORMAT - формат даты/времени;
      - DATETIME_REGEX - рег. выражение для идентификации даты/времени.

    Атрибуты экземпляра класса:
      - self._data - словарь настроек;
      - self.filename - имя файла настроек;

    Ключи в настройках:
      - "run_count": (int) - кол-во запусков;
      - "last_run_datetime": (datetime.datetime) - дата/время
                                                   последнего запуска;
      - "last_run_platform_info": (tuple) - информация о платформе
                                            последнего запуска.

    Пример файла настроек:
    {
        "last_run_datetime": "2016-01-25 18:10:34",
        "run_count": 5,
        "last_run_platform_info": [
            "Windows",
            "user-pc",
            "10",
            "10.0.14393",
            "AMD64",
            "Intel64 Family 6 Model 58 Stepping 9, GenuineIntel"
        ]
    }
    """

    # Уберите raise и дополните константы ниже
    # Формат даты: 2016-01-25 18:10:34
    DATETIME_FORMAT = '%Y-%m-%d %X'
    # Регулярное выражения для поиска даты формата DATETIME_FORMAT
    DATETIME_REGEX = r"\d{4}[-]\d{2}[-]\d{2}[ ]\d{1,2}:\d{2}:\d{2}"

    def __init__(self):
        """Инициализация класса.

        Действия:
          - инициализировать словарь 'self._data';
          - инициализировать имя файла настроек в "settings.json"
            в папке скрипта (должно быть получено абсолютное имя).
        """
        self._data = {}
        self.filename = os.path.dirname(os.path.realpath
                                        (sys.argv[0])) + '\\settings.json'

    def __str__(self):
        """Вернуть настройки 'self._data' в виде JSON-строки."""
        return json.dumps(self._data)

    def set_value(self, name, value):
        """Установить для параметра 'name' (str) значение 'value'.

        Если 'value' - дата/время, необходимо предварительно выполнить
        преобразование в строку по формату 'self.DATETIME_FORMAT'.
        """
        if type(value) == datetime.datetime:
            value = value.strftime(Settings.DATETIME_FORMAT)
        self._data[name] = value

    def get_value(self, name, default=None):
        """Вернуть значение параметра 'name' (str).

        Если 'name' найдено, тип значения - str и
            указывает на дату/время (self.DATETIME_REGEX) -
            выполнить преобразование из str в datetime.datetime
            по формату 'self.DATETIME_FORMAT';
        Если 'name' не найдено, возвращается 'default'.
        """
        if name in self._data.keys():
            if type(self._data[name]) is str:
                match = re.search(Settings.DATETIME_REGEX, self._data[name])
                if match:
                    self._data[name] = datetime.datetime.strptime(
                             self._data[name], Settings.DATETIME_FORMAT)
            return self._data[name]
        else:
            return default

    def load(self):
        """Загрузить настройки из файла 'self.filename'."""
        with open(self.filename, encoding="utf-8") as fh:
            self._data = json.loads(fh.read())

    def save(self):
        """Сохранить настройки в файл 'self.filename'."""
        with open(self.filename, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(self._data, ensure_ascii=False, indent=4))

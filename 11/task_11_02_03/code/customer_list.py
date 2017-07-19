# Римский А.А. swordscream@yandex.ru

from customer import Customer
import statistics
import datetime


class CustomerList:
    """Класс CustomerList представляет список клиентов.

    Атрибуты экземпляра класса:
        - self.customers (list из Customer): список клиентов;
        - self.filename (str): имя файла, из которого были получены клиенты;
        - self.errors (list из str): список строк с ошибками чтения файла.
    """

    def __init__(self):
        """Инициализация класса.

        Создать:
          - 'self.customers', 'self.errors', 'self.filename'.
        """
        self.customers = []
        self.errors = []
        self.filename = 'data.txt'

    def __str__(self):
        """Вернуть строковое представление класса.

        Возвращает строку со списком клиентов в алфавитном порядке.
        Для печати клиента необходимо использовать его __str__-метод.

        Формат:

        Список клиентов (3):
        1. Крутов Олег Павлович 13/01/1973 Транспорт 50,000 руб.
        2. Лягушкина Екатерина Олеговна 17/04/1958 Здоровье 15,000 руб.
        3. Смирнова Елена Юрьевна 15/12/1966 Здоровье 15,000 руб.
        """
        cust_str = 'Список клиентов ({}):'.format(len(self.customers))
        newlst = self.customers
        newlst.sort(key=lambda x: [x.f, x.i, x.o])

        i = 1
        for cust in newlst:
            cust_str += '\n{}. {}'.format(i, str(cust))
            i += 1
        return cust_str

    def open(self, filename):
        """Открыть файл 'filename' со списком клиентов.

        Аргументы:
            - filename (str): имя файла.

        1. Очистить списки клиентов и ошибок.
           Сохранить имя файла в 'self.filename'.
        2. Построчно прочитать файл "filename".
        3. Для каждой строки:
           - создать Customer.from_string() из строки;
           - добавить в 'self.customers';
           - при возникновении ошибки занести строку в 'self.errors' и
             перейти к следующей.
        4. Проверить, что прочитан хотя бы 1 клиент (assert).
        5. Отсортировать список 'self.customers' по Ф, И, О (по возрастанию).
        """
        self.customers = []
        self.errors = []
        self.filename = filename

        with open(filename, encoding="utf-8") as datafile:
            for line in datafile:
                try:
                    newcust = Customer.from_string(line)
                    self.customers.append(newcust)
                except Exception as e:
                    self.errors.append(line)
        assert len(self.customers) > 0, 'Не прочитан ни 1 клиент'

        self.customers.sort(key=lambda x: [x.f, x.i, x.o])

    def total_price(self):
        """Вернуть общую сумму контрактов."""
        return sum(customer.polis_price for customer in self.customers)

    def price_stats(self):
        """Вернуть статистические показатели (среднее, мода и медиана)
        по сумме продаж (кортеж).

        Если мода не может быть вычислена (StatisticsError) -
        вернуть вместо нее строку "не доступно".
        """
        sell_sum = []
        for cust in self.customers:
            sell_sum.append(cust.polis_price)

        try:
            stamean = statistics.mean(sell_sum)
        except Exception as e:
            stamean = 'не доступно'

        try:
            stamode = statistics.mode(sell_sum)
        except Exception as e:
            stamode = 'не доступно'

        try:
            stamed = statistics.median(sell_sum)
        except Exception as e:
            stamed = 'не доступно'

        return stamean, stamode, stamed

    def age_stats(self):
        """Вернуть статистические показатели (среднее и медиана)
        по возврасту клиентов (кортеж).

        Возраст - полное количество лет.
        """
        age_lst = []
        date_now = datetime.date.today()
        for cust in self.customers:
            delta_years = date_now - cust.birthday
            age_lst.append(delta_years.days/365)
        return int(statistics.mean(age_lst)), int(statistics.median(age_lst))

    def most_popular_polis_type(self):
        """Вернуть наиболее популярный тип полиса
        (по количеству контрактов).

        Результат: кортеж (Тип полиса, Количество контрактов),
                   например, ("Здоровье", 7).

        Подсказка: удобным способом может быть использование функции
                   sorted() с настраиваемым параметром key.
        """
        most_pop = {'Здоровье': 0, 'Путешествия': 0, 'Недвижимость': 0,
                    'Транспорт': 0}
        for cust in self.customers:
            most_pop[cust.polis_type] += 1
        return sorted(most_pop.items(), key=lambda x: x[1], reverse=True)[0]

    def most_profitable_polis_type(self):
        """Вернуть наиболее прибыльный тип полиса
        (по количеству контрактов).

        Результат: кортеж (Тип полиса, Сумма всех полисов данного типа),
                   например, ("Здоровье", 105000).

        Подсказка: удобным способом может быть использование функции
                   sorted() с настраиваемым параметром key.
        """
        most_prof = {'Здоровье': 0, 'Путешествия': 0, 'Недвижимость': 0,
                     'Транспорт': 0}
        for cust in self.customers:
            most_prof[cust.polis_type] += cust.polis_price
        return sorted(most_prof.items(), key=lambda x: x[1], reverse=True)[0]

    def print_report(self):
        """Напечатать отчет.

        Выводит на экран сводку по запрошенным показателям.

        Формат:

        "
Сумма контрактов = 305,000 руб.

Статистика продаж:
  - Цена: 30,500 руб. (среднее), 15,000 руб. (мода), 15,000.0 руб. (медиана)
  - Возраст: 51.6 л. (среднее), 53.5 л. (медиана)
  - Самый популярный тип страхового полиса: Здоровье (7)
  - Самый прибыльный тип страхового полиса: Здоровье (105,000 руб.)
        "

        Сформируйте строку 'report', которую в конце выведите на экран.
        """
        report = 'Сумма контрактов = {:,} руб.'.format(self.total_price())
        report += '\n\nСтатистика продаж:\n'
        price = self.price_stats()
        report += '  - Цена: {:,} руб. (среднее), {:,} руб. (мода), '\
                  '{:,} руб. (медиана)\n'.format(price[0], price[1], price[2])
        age = self.age_stats()
        report += '  - Возраст: {}.0 л. (среднее), {}.0 л. (медиана)\n'\
                  .format(age[0], age[1])
        pop = self.most_popular_polis_type()
        report += '  - Самый популярный тип страхового полиса: {} ({})\n'\
                  .format(pop[0], pop[1])
        profit = self.most_profitable_polis_type()
        report += '  - Самый прибыльный тип страхового полиса: {} ({:,} руб.)'\
                  .format(profit[0], profit[1])
        print(report)

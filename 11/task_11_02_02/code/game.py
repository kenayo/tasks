# Римский А.А. swordscream@yandex.ru

import sys

from card_table import CardTable
from player import Player
from messages import \
    MSG_GAME_TITLE,                  \
    MSG_CHECK_VALUES_AND_TRY_AGAIN,  \
    MSG_CARD_AND_PLAYER_COUNT,       \
    MSG_PLAYER_NUMBER,               \
    MSG_CURRENT_SCORE,               \
    MSG_GAME_BEGAN,                  \
    MSG_PLAYER_IS_MAKING_A_CHOICE,   \
    MSG_NO_CARD_WITH_NUMBER,         \
    MSG_GAME_OVER


class Game:
    """Класс Game реализует логику игры.

    Методы:
      - run(): запуск игры;
      - _...: дополнительные методы.
    """

    CARDS_COUNT_MIN = 2    # Минимальное кол-во карт на столе
    CARDS_COUNT_MAX = 36   # Максимальное кол-во игроков
    PLAYERS_COUNT_MIN = 2  # Минимальное кол-во игроков
    PLAYERS_COUNT_MAX = 5  # Максимальное кол-во игроков

    def _can_run(self, cards_count, players_count):
        """Вернуть True, если находятся в допустимом диапазоне:
          - 'cards_count': [Game.CARDS_COUNT_MIN, Game.CARDS_COUNT_MAX];
          - 'players_count': [Game.PLAYERS_COUNT_MIN, Game.PLAYERS_COUNT_MIN].
        """
        cards_range = range(Game.CARDS_COUNT_MIN, Game.CARDS_COUNT_MAX + 1)
        pl_range = range(Game.PLAYERS_COUNT_MIN, Game.PLAYERS_COUNT_MAX + 1)
        if cards_count in cards_range and players_count in pl_range:
            return True
        return False

    def _get_game_params(self):
        """Запросить параметры игры: кол-во карт и кол-во игроков.

        В первую очередь  необходимо проверить параметры командной строки:

         -cards_count -players_count

        Если они доступны и подходят для параметров игры - взять их.
        В противном случае - спросить у пользователя.
        """
        cmd_params = False
        if len(sys.argv) == 3:
            try:
                cards_count, players_count = int(sys.argv[1]), \
                                             int(sys.argv[2])
                cmd_params = True
            except Exception:
                # При отсутствии параметров командной строки
                pass

        while True:
            try:
                print(
                    MSG_CARD_AND_PLAYER_COUNT.format(
                        Game.CARDS_COUNT_MIN, Game.CARDS_COUNT_MAX,
                        Game.PLAYERS_COUNT_MIN, Game.PLAYERS_COUNT_MAX),
                    end="")

                # Если параметры получены - печатаем, иначе -
                # спрашиваем у пользователя
                if cmd_params:
                    print(cards_count, players_count,
                          "(аргументы командной строки)")
                    cmd_params = False
                else:
                    params = input()
                    cards_count, players_count = map(int, params.split())

                # Проверка значений на допустимость
                assert self._can_run(cards_count, players_count)
                break
            except (AssertionError, ValueError):
                print(MSG_CHECK_VALUES_AND_TRY_AGAIN)
            except Exception:
                raise

        return cards_count, players_count

    def _get_players_names(self, players_count):
        """Вернуть список из 'players_count' имен с клавиатуры.

        Параметры:
          - players_count (int): количество игроков."""
        pl_list = []
        for i in range(players_count):
            pl_list.append(input(MSG_PLAYER_NUMBER.format(i + 1)))
        return pl_list

    def _get_current_score(self, players):
        """Вернуть строку с текущим счетом для каждого из игроков 'players'.

        Параметры:
          - players (list из Player): список игроков.

        Результат:
          - Строка вида 'Имя_игрока_1 - 21, Имя_игрока_2 - 36'.
        """
        cur_str = ''
        for player in players:
            if player != players[0]:
                cur_str += ', '
            cur_str += player.name + ' - ' + str(player.card_list.sum())
        return cur_str

    def _sorted_by_score_and_name(self, players):
        """Отсортировать и вернуть список игроков 'players'
        убыванию кол-ва очков и по алфавиту.

        Параметры:
          - players (list из Player): список игроков.

        Результат:
          - players (list из Player): список игроков.
        """
        players.sort(key=lambda x: [x.card_list.sum(), x.name], reverse=True)
        return players

    def run(self):
        """Начать новую игру.

        Ход игры:
        1. Узнать параметры (кол-во карт, кол-во игроков, их имена).
        2. Запустить игру.
        3. Показать итоговый рейтинг.
        """
        print(MSG_GAME_TITLE)

        # 1. Параметры игры
        cards_count, players_count = self._get_game_params()
        players_names = self._get_players_names(players_count)

        # 2. Запуск игры
        table = CardTable(cards_count)
        players = [Player(name) for name in players_names]

        print("\n" + MSG_GAME_BEGAN)
        while not table.is_empty():
            for player in players:
                # 2.1. Показать стол
                print(table)

                # 2.2. Выбор карты
                while True:
                    try:
                        print(
                            "  " +
                            MSG_PLAYER_IS_MAKING_A_CHOICE.format(player.name),
                            end="")
                        index = player.make_choice()
                        card = table.take_card(index)
                        player.add_card(card)
                        break
                    except ValueError:
                        print(MSG_CHECK_VALUES_AND_TRY_AGAIN)
                    except IndexError:
                        print(MSG_NO_CARD_WITH_NUMBER.format(index))

                # 2.3. После хода стол пуст?
                if table.is_empty():
                    break

            # 2.2. Вывод текущего счета на экран
            # печать текущего счета, используя сообщение
            # MSG_CURRENT_SCORE и _get_current_score(players)
            print(MSG_CURRENT_SCORE.format(self._get_current_score(players)))

        # 3. Итог игры
        print("\n" + MSG_GAME_OVER)
        # получить список игроков в отсортированном виде
        rating = self._get_current_score(self._sorted_by_score_and_name(
                                                               players))
        print(MSG_CURRENT_SCORE.format(rating))

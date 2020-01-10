import random
import sys
class Fool_game:
    def __init__(self):
        cards_set = []
        self.cards_set_6_10 = [x for x in range(6, 11)] # генерируем список карт от 6 до 10
        # создаем список cards_set_1_suit - карты одной масти
        cards_set_1_suit = list(map(str, self.cards_set_6_10)) + 'Валет Дама Король Туз'.split()
        # self.suit - 4 масти из Unicode
        self.suit = u'\u2660,\u2665,\u2663,\u2666'.split(',')

        # Делаем словарь cards_dict
        # присваиваем значения ключам - картам одной масти ('6':0, '7':1 и т.д.)

        #self._card_deck - словарь полной колоды карт
        self._card_deck_dict = {}
        # создаем словарь со значениями для одной масти
        self._cards_dict = {cards_set_1_suit[i]: i for i in range(len(cards_set_1_suit))}
        print(self._cards_dict)
        # создаем словарь со значениями для 4 мастей
        for i in range(len(self.suit)):  # в каждой из 4 мастей
            for keys, values in self._cards_dict.items():  # для каждого ключа словаря
                keys = self.suit[i] + keys # ключ - это масть (значок Unicode) и первоначальный ключ('6','7','Валет' и т.д.)
                #print(keys, values)
                self._card_deck_dict[keys] = values #словарь полной колоды карт со значениями
        #print('Словарь без козырей:', self._card_deck_dict)


    def cards_shuffle(self):
        self._card_deck_list = list(self._card_deck_dict)
        random.shuffle(self._card_deck_list)
        print('Карты перемешаны')
        #print('Карты перемешаны: #{}. Всего {} карт'.format(self._card_deck_list, len(self._card_deck_list)))


    def hand_cards(self):
        self.player_hand = self._card_deck_list[-6:] # раздаем игроку 6 карт, которые расположены "вверху" колоды
        self._computer_hand = self._card_deck_list[-12:-6] # раздаем Компьютеру 6 карт, которые расположены в колоде ниже карт Игрока
        print('Ваши карты:\n{}'.format(self.player_hand))  # выводим карты Игрока на экран
        del self._card_deck_list[-12:] # удаляем из колоды розданные карты

    def trump_random(self):
        self.trump = self._card_deck_list.pop() # после раздачи карт верхняя карта - козырь
        self._card_deck_list.insert(0, self.trump) # переставляем козырь вниз колоды
        print('Козырь: ', self.trump)

        #создаем колоду, где у козырей повышенные значения
        self._card_deck_dict_trump = {}
        #print(self.trump[0:1])
        self.trump_advantage = 10 # увеличиваем силу козыря на 10 по сравнению с обычными картами
        for keys, values in self._card_deck_dict.items():
            if self.trump[0:1] in keys: # определяем козырь по первому символу в строке
                values += self.trump_advantage
                self._card_deck_dict_trump[keys] = values
            else:
                self._card_deck_dict_trump[keys] = values
        #print('Словарь с козырями)', self._card_deck_dict_trump)
        #print('Перемешанные карты с козырем {}. Всего {} карт.'.format(self._card_deck_list,len(self._card_deck_list)))

    def how_many_cards_in_deck(self):
        # сколько карт в колоде
        print('Всего в колоде: {}'.format(len(self._card_deck_list)))

    def who_goes_firts(self):
        # определяет случайным образом, кто ходит первым - Игрок или Компьютер
        if random.randint(1, 2) == 1:
            print('Ходит Игрок')
            return 'Ходит Игрок'
        else:
            print('Ходит Компьютер')
            return 'Ходит Компьютер'

    def player_move(self):
        # ход Игрока
        print('Ваши карты:\n{}'.format(self.player_hand))
        self.player_move_cards = [] # список карт, которыми пошел Игрок
        i = 0 # количество выбранных карт
        self.player_choice = 37 # переменная для ввода значения
        player_hand_len = [] # количество карт в рукаве (Игрок выбирает карту, считая слева направо)
        for i in range(len(self.player_hand)): # выводим для удобства цифры (сколько карт в рукаве) для пользователя
            player_hand_len.append(i+1)
        move_is_right = False
        while move_is_right == False:
            while self.player_choice not in player_hand_len or self.player_choice != 0:
                # пока ввод не является цифрой из player_hand_len (сколько карт в рукаве)
                # или не является 0 (обозначает действие-ход)
                # предлагать выбрать карту (благодаря циклу, можно выбрать две и больше)
                # записываем выбранные карты в список self.player_move
                self.player_choice = int(input('Введите карту, которой желаете пойти: {} и \'0\', чтобы сделать ход'.format(player_hand_len)))

                if self.player_choice == 0: # вводе 0 обозначает, что Игрок ходит выбранными картами
                    print('Ваш ход: {}'.format(self.player_move_cards))
                    input('Нажмите Enter для подтверждения')
                    move_is_right = True
                    break



                if self.player_choice in player_hand_len: # если введенное значение входит в количество карт на руках у Игрока
                    self.player_move_cards.append(self.player_hand[self.player_choice-1]) #добавлем карту в список карт, которыми пошел Игрок
                    i+=1
                else:
                    input('Нажмите Enter и выберите карту из имеющихся по порядковому номеру слева направо {}'.format(player_hand_len))

        if len(self.player_move_cards) == 1:
            print('Ваш ход выполнен: {}'.format(self.player_move_cards))
        '''if len(self.player_move_cards) == 2:
            for i in range(len(self.player_move_cards)+1):
                if self._card_deck_dict[self.player_move_cards[0]] == self._card_deck_dict[self.player_move_cards[1]]:
                    print('Ваш ход выполнен: {}'.format(self.player_move_cards))
                    #print(self._card_deck_dict[self.player_move[i]])
                    break
                else:
                    print('Ваш ход не выполнен. Выберите карты одинаковых значений.')
                    continue'''

        for el in self.player_hand:
            if el in self.player_move_cards:
                self.player_hand.remove(el) # Удаляем карту из рук Игрока
                continue

        print('Ваши карты: {}'.format(self.player_hand))

    def computer_answer(self):
    # Сравнить выбранную Игроком карту с картами Компьютера.
    # Если у Компьютера есть карта больше, то побить
    # результат - бита либо Компьютер берет
    # self.player_move - карты Игрока, которые надо побить
        # для одной карты
        answer_cards = [] # список простых карт, которыми может побить Компьютер
        answer_cards_trump = [] # список козырных карт, которыми может побить Компьютер
        not_trump = False # сначала проверяем, есть ли простые карты, если есть, меняем значение на True
        if len(self.player_move_cards) == 1: # если Игрок пошел одной картой
            for card in self._computer_hand:
                for player_card in self.player_move_cards:
                    if (card[0:1] == player_card[0:1]): # проверяем сходство мастей
                        if self._card_deck_dict_trump[card] > self._card_deck_dict_trump[player_card]: # по словарю проверяем значения
                            not_trump = True
                            answer_cards.append(card)

                    if (card[0:1] == self.trump[0:1]): # если карта - козырь
                        if self._card_deck_dict_trump[card] > self._card_deck_dict_trump[player_card]: # сравниваем значения карт Игрока и Компьютера
                            answer_cards_trump.append(card)

        # если есть простые карты, которыми можно отбить, используем их
        if not_trump == True:
            self.computer_move = answer_cards[0] #выбираем первую карту из списка
            self._computer_hand.remove(self.computer_move) # удаляем карту из рук Компьютера
            print('Карта Компьютера {} бьет Вашу карту.\nБита.'.format(self.computer_move))
            return 'Ход Компьютера'
        # если нет, используем козыри
        elif not_trump == False:
            if len(answer_cards_trump) > 0: # если список не пуст, выбираем рандомный козырь
                self.computer_move = random.choice(answer_cards_trump)
                self._computer_hand.remove(self.computer_move) # удаляем карту из рук Компьютера
                print('Карта Компьютера {} бьет Вашу карту.\nБита.'.format(self.computer_move))
                return 'Ход Компьютера'
            # иначе - Компьютер берет
            else:
                print('Компьютер берет.')
                self._computer_hand.append(self.player_move_cards)
                return 'Ход Игрока'

    def new_cards(self):
        #осуществить добор
        # если у Игрока меньше 6 карт и в колоде есть карты, добавляем последнюю карту из колоды в руки Игрока, удаляем карту из колоды
        if (len(self.player_hand) < 6) and (len(self._card_deck_list) > 0):
            self.player_hand.append(self._card_deck_list[-1])
            del self._card_deck_list[-1]
            #print('Ваши карты:\n{}'.format(self.player_hand))
            print('Карту Игроку. Осталось карт в колоде: {}'.format(len(self._card_deck_list)))
        # если у Компьютера меньше 6 карт и в колоде есть карты, добавляем последнюю карту из колоды в руки Компьютера, удаляем карту из колоды
        if (len(self._computer_hand) < 6) and (len(self._card_deck_list) > 0):
            self._computer_hand.append(self._card_deck_list[-1])
            del self._card_deck_list[-1]
            #print('Карты компьютера:\n{}'.format(self._computer_hand))
            print('Карту Компьютеру. Осталось карт в колоде: {}'.format(len(self._card_deck_list)))
            print('Всего карт у Компьютера: {}'.format(len(self._computer_hand)))

    def computer_ai_move(self):
        # Компьютер ходит, выбирая карту с минимальным значением
        if len(self._computer_hand) > 0:  # если у Компьютера есть карты
            self.min_computer_card = 20 # чтобы определить минимальную карту, сначала сравним первую карту со значением 20
            self.computer_move = '' # self.computer_move - это карта, которой ходит компьютер
            for card in range(len(self._computer_hand)): # из карт, которые на руках у Компьютера, выбираем минимальную (смотрим значения по словарю)
                self.computer_move = str(self._computer_hand[card]) # приводим к типу строка (выдавал ошибку, что unhashable type: list)
                if self._card_deck_dict_trump[self.computer_move] < self.min_computer_card:
                    self.min_computer_card = self._card_deck_dict_trump[self.computer_move]
                    self.computer_move_int = self._card_deck_dict_trump[self.computer_move] #
            self._computer_hand.remove(self.computer_move) #удаляем карту из рук компьютера
            print('Ход компьютера: {}'.format(self.computer_move))
            #print('Карты Компьютера: {}'.format(self._computer_hand))

    def player_answer_move(self):
        # ответный ход Игрока
        while True:
            print('Ваши карты:\n{}'.format(self.player_hand))
            player__answer_hand_len = []  # количество карт в рукаве (Игрок выбирает карту, считая слева направо)
            for i in range(len(self.player_hand)):  # выводим для удобства цифры (сколько карт в рукаве) для пользователя
                player__answer_hand_len.append(i + 1)
            player_answer_cards = int(input('Введите карту {}, чтобы побить Компьютер.\nВведите 0, чтобы забрать карту.'.format(player__answer_hand_len)))
            if player_answer_cards == 0: # если Игрок вводит 0, он берет карту, то есть
                self.player_hand.append(self.computer_move) # карта Компьютера добавляется в руки Игрока
                print('Вы взяли. У вас {} карт.\nВаши карты: {}'.format(len(self.player_hand), self.player_hand))
                return 'Ход Компьютера' # если не может побить, возвращается значение 'Ход Компьютера'


            # проверяем, может ли карта побить карту компьютера:
            # 1) значение карты Игрока должно быть больше
            # 2) масти должны либо совпадать, либо масть должна быть козырная
            if (self._card_deck_dict_trump[self.player_hand[player_answer_cards-1]] > self.computer_move_int) and ((self.player_hand[player_answer_cards-1][0:1] == self.computer_move[0:1]) or (self.player_hand[player_answer_cards-1][0:1] == self.trump[0:1])):
                print('Карта Игрока {} бьет карту Компьютера.\nБита.'.format(self.player_hand[player_answer_cards - 1]))
                self.player_hand.remove(self.player_hand[player_answer_cards-1])
                return 'Ход Игрока' # возвращает значение 'Ход Игрока', чтобы можно быть менять ходы
            else:
                print('Эта карта не может побить карту Компьютера. Введите заново либо возьмите карту.')
                continue

    def is_winner(self):
        # если у Компьютера карт не остается, Компьтер победил
        # если у Игрока карт не остается, Игрок победил
        if len(self.player_hand) == 0:
            return 'Игрок победил'
        if len(self._computer_hand) == 0:
            return 'Компьютер победил'






# print('Игра "Дурак"')
#
# while True:
#
#     play = Fool_game() # Начинается игра, созается колода
#     play.cards_shuffle() # Перемешивается колода
#     play.hand_cards() # Раздаются карты
#     play.trump_random() # Определяется козырь
#     play.how_many_cards_in_deck() # Показывает, сколько осталось карт в колоде
#     turn_start = play.who_goes_firts() # Определяет, кто ходит первым
#     turn = ''
#
#     while True:
#         while turn_start == 'Ходит Игрок' or turn == 'Ход Игрока':
#             play.player_move() #ходит Игрок
#             turn = play.computer_answer() # в зависимости от ответного хода Компьютера опреледяется, кто ходит дальше (turn)
#             if play.is_winner(): # проверяется, остались ли карты у Игрока/Компьютера (определяется победа)
#                 print(play.is_winner())
#                 sys.exit() # если победа, то выход из программы
#             play.new_cards() # раздаются карты после ходов
#             if turn == 'Ход Игрока': # если сохраняется ход Игрока, то цикл начинается заново
#                 continue
#             else: # иначе программа переходит к следующему циклу
#                 break
#         while turn_start == 'Ходит Компьютер' or turn == 'Ход Компьютера':
#             play.computer_ai_move() # ходит компьютер
#             turn = play.player_answer_move()  # в зависимости от ответного хода Игрока опреледяется, кто ходит дальше (turn)
#             if play.is_winner(): # проверяется, победил ли Игрок/Компьютер
#                 print(play.is_winner())
#                 sys.exit() # если победа, то выход из программы
#             play.new_cards() # раздаются карты после ходов
#             if turn == 'Ход Компьютера': # если сохраняется ход Компьютера, то цикл начинается заново
#                 continue
#             else: # иначе программа переходит к следующему циклу (Ход Игрока)
#                 break

import unittest
from fool_game_module import Fool_game

class Test_Fool_unittest(unittest.TestCase):
    def setUp(self):
        print('Start test!')
        self.play_1 = Fool_game()

    def tearDown(self):
        print('Test completed!')

    def test_init_len_deck(self):
        self.assertEqual(len(self.play_1.cards_set_6_10), 5)

    def test_init_cards_1_suit(self):
        self.assertEqual (self.play_1._cards_dict, {'6': 0, '7': 1, '8': 2, '9': 3, '10': 4, 'Валет': 5, 'Дама': 6, 'Король': 7, 'Туз': 8})

    def test_init_full_deck_no_trumps(self):
        self.assertEqual(self.play_1._card_deck_dict, {'♠6': 0, '♠7': 1, '♠8': 2, '♠9': 3, '♠10': 4, '♠Валет': 5, '♠Дама': 6, '♠Король': 7, '♠Туз': 8, '♥6': 0, '♥7': 1, '♥8': 2, '♥9': 3, '♥10': 4, '♥Валет': 5, '♥Дама': 6, '♥Король': 7, '♥Туз': 8, '♣6': 0, '♣7': 1, '♣8': 2, '♣9': 3, '♣10': 4, '♣Валет': 5, '♣Дама': 6, '♣Король': 7, '♣Туз': 8, '♦6': 0, '♦7': 1, '♦8': 2, '♦9': 3, '♦10': 4, '♦Валет': 5, '♦Дама': 6, '♦Король': 7, '♦Туз': 8})

    def test_trump_advantage(self):
        self.play_1._card_deck_list = list(self.play_1._card_deck_dict)
        self.play_1.trump_random()
        self.assertEqual(self.play_1.trump_advantage, 10)

    def test_hand_cards(self):
        self.play_1._card_deck_list = list(self.play_1._card_deck_dict)
        self.play_1.cards_shuffle()
        self.play_1.hand_cards()
        self.assertEqual(len(self.play_1.player_hand), 6)


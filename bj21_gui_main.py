import sys
import random
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic
from bj21_ui import Ui_MainWindow


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # creating new object from Ui_LoginForm, from login.ui
        self.ui = Ui_MainWindow()

        # calling method from class above, from login.ui
        self.ui.setupUi(self)

        # constants for card suits and ranks , obv.
        self.SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                       'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.TABLE_POT = 0

        # center app/ widget
        qr = self.frameGeometry()
        cp = qtw.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # set card icons
        self.ui.icon1.setIcon(qtg.QIcon('ace1.png'))
        self.ui.icon1.setIconSize(qtc.QSize(80, 81))
        self.ui.icon2.setIcon(qtg.QIcon('ace2.png'))
        self.ui.icon2.setIconSize(qtc.QSize(80, 81))
        self.show()

        # get username
        ask_name, bool1 = qtw.QInputDialog.getText(
            self, 'Welcome!', 'Welcome to Black Jack 21!\nEnter your name Player: ')

        # Setup deck,hands
        self.deck = Deck(self)
        self.deck.shuffle()
        self.dealer = Dealer()
        self.human_player = Player(ask_name, self)
        self.ui.player_name.setText(f"{self.human_player}'s Cards")

        # deal chips and update gui
        print(f'{self.human_player.name} has {self.human_player.chips} chips.')
        print(f'Dealer has {self.dealer.chips} chips.')
        self.ui.player_chips.setText(f'Chips: {self.human_player.chips}')
        self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
        self.deck.deal_two(self.dealer)
        self.deck.deal_two(self.human_player)
        self.ui.dealer_card1.setText('CARD HIDDEN')
        self.ui.dealer_card2.setText(f'{self.dealer.hand_cards[1]}')
        self.ui.player_card1.setText(f'{self.human_player.hand_cards[0]}')
        self.ui.player_card2.setText(f'{self.human_player.hand_cards[1]}')

        # request bet, check avail chips...
        self.ui.enter_buttton.clicked.connect(self.make_bet)

    def make_bet(self):

        try:
            bet_amount = int(self.ui.bet_amount_edit.text())
            self.ui.player_textbox.setText('Enter Bet Amount ...')
            if self.human_player.chips >= bet_amount and self.dealer.chips >= bet_amount:
                print(self.human_player.chips >=
                      bet_amount and self.dealer.chips >= bet_amount)
                self.TABLE_POT += self.human_player.bet_chips(bet_amount)
                self.TABLE_POT += self.dealer.bet_chips(bet_amount)
                self.ui.pot_total.setText(f'Pot Total: {self.TABLE_POT}')
                self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
                self.ui.player_chips.setText(
                    f'Chips: {self.human_player.chips}')
                self.ui.player_total.setText(
                    f'Total: {self.human_player.total()}')
                self.ui.dealer_total.setText(
                    f'Total: {self.dealer.total_visible()}')

                print(f'Table Pot: {self.TABLE_POT}\n')
                self.ui.bet_amount_edit.setVisible(False)
                self.ui.enter_buttton.setVisible(False)
                self.ui.player_textbox.setText('Hit or Hold?')
            else:
                self.ui.player_textbox.setText(
                    'Not enough chips in the bank, try again.')
        except ValueError:
            self.ui.player_textbox.setText('Must be a number, try again.')

    def stay(self):
        pass
    # dealer actions now...
     # # sub loop, dealers turn, keep adding cards if total cards < 17
        # while DEALERS_TURN and self.dealer.total() < 17:
        #     if not self.dealer.bust():
        #         print('--------------------')
        #         self.deck.deal_one(self.dealer)
        #         print(f'Dealers Cards: {self.dealer.hand_cards[0]}.')
        #         for card4 in self.dealer.hand_cards[2:]:
        #             print(f'Dealers Cards: {card4}.')
        #     elif self.dealer.bust():
        #         print('DEALER BUSTS!')
        #         DEALERS_TURN = False

    def hit_me(self):
        if not self.human_player.bust():
            self.deck.deal_one(self.human_player)
        elif self.human_player.bust():
            print(f'{self.human_player.name} BUSTS!')

        # # determine winner, add chips to players total
        # print('--------------------')
        # print(f'Dealer Total: {self.dealer.total()}')
        # print(f'Player Total: {self.human_player.total()}')
        # print('--------------------')
        # if self.dealer.bust():
        #     print(f'{self.human_player.name} wins!!!')
        #     self.human_player.add_chips(self.TABLE_POT)
        # elif self.human_player.bust():
        #     print('Dealer Wins!!!')
        #     self.dealer.add_chips(self.TABLE_POT)
        # elif self.dealer.total() == self.human_player.total():
        #     print('TIE !!!')
        # elif self.dealer.total() > self.human_player.total():
        #     print('Dealer Wins!!!')
        #     self.dealer.add_chips(self.TABLE_POT)
        # elif self.dealer.total() < self.human_player.total():
        #     print(f'{self.human_player.name} wins!!!')
        #     self.human_player.add_chips(self.TABLE_POT)

        # # replay
        # if self.human_player.chips == 0 or self.dealer.chips == 0:
        #     print('One player out of chips, GAME OVER.')
        #     print('\nGoodbye!')
        #     GAME_ON = False

        # again = input('\nPlay again? (y/n) ')
        # if again == 'y':
        #     self.deck.all_cards.extend(self.dealer.hand_cards)
        #     self.deck.all_cards.extend(self.human_player.hand_cards)
        #     self.dealer.hand_cards.clear()
        #     self.human_player.hand_cards.clear()
        #     self.TABLE_POT = 0
        #     # system('clear')
        #     # continue

        # print('\nGoodbye!')


class Card():
    """ class for the individual cards in the game. """

    def __init__(self, suit, rank, win_obj):
        self.suit = suit
        self.rank = rank
        self.value = win_obj.VALUES[rank]

    def __repr__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """ class for the whole card deck and its use. """

    def __init__(self, win_obj):

        self.all_cards = []
        for suit in win_obj.SUITS:
            for rank in win_obj.RANKS:
                self.all_cards.append(Card(suit, rank, win_obj))
        print(f'Deck has {len(self.all_cards)} cards.')

    def shuffle(self):
        """ randomizes all the cards in the deck"""
        random.shuffle(self.all_cards)
        print('Cards have been shuffled.')

    def deal_one(self, player):
        """ adds one card to (player), removing it from the deck. """
        print(f'One card dealt to {player}.')
        player.hand_cards.append(self.all_cards.pop(0))

    def deal_two(self, player):
        """ adds two cards to the (player), removing it from the deck. """
        print(f'Two card dealt to {player}.')
        for _ in range(2):
            player.hand_cards.append(self.all_cards.pop(0))


class Player:
    """ class for the user. to hold cards and methods. """

    def __init__(self, name, win_obj):
        self.name = name
        self.chips = 100
        self.hand_cards = []

    def add_chips(self, chips):
        """ add (chips) to player total. """
        self.chips += chips
        print(f'{chips} chips added to {self.name}.')

    def bet_chips(self, chips):
        """ return number of (chips) the player bets. """
        self.chips -= chips
        print(f'{self.name} bets {chips} chips.')
        return chips

    def bust(self):
        """ checks for a bust condition, over 21. returns boolean. """
        card_total = 0
        for card2 in self.hand_cards:
            card_total += card2.value
        return card_total > 21

    def total(self):
        """ calculates total value of cards in hand. return value."""
        temp_total = 0
        for card3 in self.hand_cards:
            temp_total += card3.value
        return temp_total

    def __repr__(self):
        return self.name


class Dealer:
    """ class for Dealer/ computer player, and its methods. """

    def __init__(self):

        self.hand_cards = []
        self.chips = 100
        self.name = 'Dealer'

    def add_chips(self, chips):
        """ add (chips) to Dealer total. """
        self.chips += chips
        print(f'{chips} chips added to {self.name}.')

    def bet_chips(self, chips):
        """ return number of (chips) the Dealer bets. """
        self.chips -= chips
        print(f'{self.name} bets {chips} chips.')
        return chips

    def bust(self):
        """ checks for a bust condition, over 21. returns boolean. """
        card_total = 0
        for card1 in self.hand_cards:
            card_total += card1.value
        return card_total > 21

    def total(self):
        """ calculates total value of cards in hand. return value."""
        temp_total = 0
        for card3 in self.hand_cards:
            temp_total += card3.value
        return temp_total

    def total_visible(self):
        """ calculates total value of cards visible. return value."""
        print('Total_visible running...')
        temp_total = 0
        print(self.hand_cards[1:])
        for card3 in self.hand_cards[1:]:
            print(card3.value)
            temp_total += card3.value
        return temp_total

    def __repr__(self):
        return self.name
        GAME_ON = False


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())

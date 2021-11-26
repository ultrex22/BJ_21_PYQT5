""" 
Simple BlackJack 21 card game using PYQT5 GUI. 
Author: Ron Brilhante
Date: 11/21/21
Version 1.0

"""

import sys
import random
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtTest
from bj21_ui import Ui_MainWindow

# globals to retain chips totals from round to round. resets when game exits.
# these get modified by player and dealer classes and replay() method.
GLOBAL_SETTINGS = {'PLAYER_CHIPS': 200,
                   'DEALER_CHIPS': 200,
                   'PLAYER_HAS_NAME': False,
                   'PLAYER_CURRENT_NAME': ''}


class MainWindow(qtw.QMainWindow):
    """ Sets up the main windows gui """
    # Set unique exit code used for newApp restart
    EXIT_CODE_REBOOT = -12345678

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # creating new object from Ui_LoginForm, from login.ui
        self.ui = Ui_MainWindow()

        # calling method from class above, from login.ui
        self.ui.setupUi(self)

        # center newApp/ widget
        frame_geo = self.frameGeometry()
        window_center = qtw.QDesktopWidget().availableGeometry().center()
        frame_geo.moveCenter(window_center)
        self.move(frame_geo.topLeft())

        # set card icons
        self.ui.icon1.setIcon(qtg.QIcon('Static/Icons/ace1.png'))
        self.ui.icon1.setIconSize(qtc.QSize(90, 95))
        self.ui.icon2.setIcon(qtg.QIcon('Static/Icons/ace2.png'))
        self.ui.icon2.setIconSize(qtc.QSize(90, 95))
        self.ui.dealer_chips.setText(
            f"Chips: {GLOBAL_SETTINGS['DEALER_CHIPS']}")
        self.ui.player_chips.setText(
            f"Chips: {GLOBAL_SETTINGS['PLAYER_CHIPS']}")
        self.show()
        self.game_on()

    def game_on(self):
        """ Sets up the main components of the game, and deals first round """
        global PLAYER_CURRENT_NAME, PLAYER_HAS_NAME
        self.SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                       'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.TABLE_POT = 0
        self.next_card_slot_idx = 2

        # check for existing player name from previous round , if not then ask for one
        if not GLOBAL_SETTINGS["PLAYER_HAS_NAME"]:
            ask_name, bool1 = qtw.QInputDialog.getText(
                self, 'Welcome!', 'Welcome to Black Jack 21!\n    What is your name?: ')
            PLAYER_CURRENT_NAME = ask_name
            PLAYER_HAS_NAME = True
        else:
            ask_name = GLOBAL_SETTINGS["PLAYER_CURRENT_NAME"]

        # Setup deck,hands
        self.deck = Deck(self)
        self.deck.shuffle()
        self.dealer = Dealer()
        self.human_player = Player(ask_name.title())
        self.ui.player_name.setText(f"{self.human_player}'s Cards")

        # deal chips and first 2 cards
        self.ui.hit_me_button.setEnabled(False)
        self.ui.hold_button.setEnabled(False)
        self.ui.player_chips.setText(f'Chips: {self.human_player.chips}')
        self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
        self.deck.deal_two(self.dealer)
        self.deck.deal_two(self.human_player)
        self.ui.dealer_card1.setText('CARD HIDDEN')
        self.ui.dealer_card2.setText(f'{self.dealer.hand_cards[1]}')
        self.ui.player_card1.setText(f'{self.human_player.hand_cards[0]}')
        self.ui.player_card2.setText(f'{self.human_player.hand_cards[1]}')
        self.ui.player_total.setText(
            f'Total: {self.human_player.total()}')
        self.ui.dealer_total.setText(
            f'Total: {self.dealer.total_visible()}')
        self.ui.player_textbox.setText(
            'How many chips do you want to bet?')
        self.ui.enter_buttton.clicked.connect(self.player_makes_bet)

    def player_makes_bet(self):
        """ Requests number of chips to bed from player, updates values, and text. """

        try:
            bet_amount = int(self.ui.bet_amount_edit.text())
            self.ui.player_textbox.setText(
                'How many chips do you want to bet?')

            if self.human_player.chips >= bet_amount and self.dealer.chips >= bet_amount:
                self.TABLE_POT += self.human_player.bet_chips(bet_amount)
                self.TABLE_POT += self.dealer.bet_chips(bet_amount)
                self.ui.pot_total.setText(f'Pot Total: {self.TABLE_POT}')
                self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
                self.ui.player_chips.setText(
                    f'Chips: {self.human_player.chips}')
                self.ui.bet_amount_edit.setEnabled(False)
                self.ui.enter_buttton.setEnabled(False)
                self.ui.player_textbox.setText('Hit or Hold?')
                self.ui.hit_me_button.clicked.connect(self.players_turn)
                self.ui.hold_button.clicked.connect(self.dealers_turn)
                self.ui.hit_me_button.setEnabled(True)
                self.ui.hold_button.setEnabled(True)

            else:
                self.ui.player_textbox.setText(
                    'You or the Dealer does not have enough chips!')

        except ValueError:
            self.ui.player_textbox.setText('Must be a number, try again.')

    def players_turn(self):
        """ Deals one card per click of hit-me button for player """
        self.deck.deal_one(self.human_player)

        try:
            if self.next_card_slot_idx == 2:
                self.ui.player_card3.setText(
                    f'{self.human_player.hand_cards[self.next_card_slot_idx]}')
            if self.next_card_slot_idx == 3:
                self.ui.player_card4.setText(
                    f'{self.human_player.hand_cards[self.next_card_slot_idx]}')
            if self.next_card_slot_idx == 4:
                self.ui.player_card5.setText(
                    f'{self.human_player.hand_cards[self.next_card_slot_idx]}')
            if self.next_card_slot_idx == 5:
                self.ui.player_card6.setText(
                    f'{self.human_player.hand_cards[self.next_card_slot_idx]}')
        except IndexError:
            self.next_card_slot_idx += 1
        self.ui.player_total.setText(
            f'Total: {self.human_player.total()}')

        if self.human_player.bust():
            self.ui.hit_me_button.setEnabled(False)
            self.ui.hold_button.setEnabled(False)
            self.dealers_turn()

    def dealers_turn(self):
        """ Deals one card for dealer as long as total value of cards in hand is < 17. """
        # sub loop, dealers turn, keep adding cards if total cards < 17
        self.ui.hit_me_button.setEnabled(False)
        self.ui.hold_button.setEnabled(False)
        self.next_card_slot_idx = 2
        self.ui.dealer_card1.setText(f'{self.dealer.hand_cards[0]}')

        while self.dealer.total() < 17:
            self.deck.deal_one(self.dealer)

            if self.next_card_slot_idx == 2:
                self.ui.dealer_card3.setText(
                    f'{self.dealer.hand_cards[self.next_card_slot_idx]}')
            if self.next_card_slot_idx == 3:
                self.ui.dealer_card4.setText(
                    f'{self.dealer.hand_cards[self.next_card_slot_idx]}')
            if self.next_card_slot_idx == 4:
                self.ui.dealer_card5.setText(
                    f'{self.dealer.hand_cards[self.next_card_slot_idx]}')
            if self.next_card_slot_idx == 5:
                self.ui.dealer_card6.setText(
                    f'{self.dealer.hand_cards[self.next_card_slot_idx]}')

            self.next_card_slot_idx += 1
        self.end_game()

    def end_game(self):
        """Determines Winner or Tie and prompts player for replay"""
        # show dealer hidden card, and total including hidden card value
        self.ui.player_total.setText(
            f'Total: {self.human_player.total()}')
        self.ui.dealer_total.setText(
            f'Total: {self.dealer.total()}')
        self.ui.dealer_card1.setText(
            f'{self.dealer.hand_cards[0]}')

        # dealer busts, add pot chips to player
        if self.dealer.bust():
            self.ui.player_textbox.setText(
                f'Dealer Busts.\n{self.human_player.name} Wins!')
            self.human_player.add_chips(self.TABLE_POT)

        # player busts, add chips to dealer
        elif self.human_player.bust():
            self.ui.player_textbox.setText(
                f'{self.human_player} Busts.\nDealer Wins!')
            self.dealer.add_chips(self.TABLE_POT)

        # tie, pot remains
        elif self.dealer.total() == self.human_player.total():
            self.ui.player_textbox.setText('''It's A Tie...''')

        # dealer wins, add chips to dealer pot
        elif self.dealer.total() > self.human_player.total():
            self.ui.player_textbox.setText('Dealer Wins!')
            self.dealer.add_chips(self.TABLE_POT)

        # player wins, add chips to player
        elif self.dealer.total() < self.human_player.total():
            self.ui.player_textbox.setText(
                f'{self.human_player.name} Wins!')
            self.human_player.add_chips(self.TABLE_POT)

        self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
        self.ui.player_chips.setText(
            f'Chips: {self.human_player.chips}')
        self.ui.pot_total.setText('Pot: 0')
        QtTest.QTest.qWait(4000)

        if self.human_player.chips <= 0 or self.dealer.chips <= 0:
            self.ui.player_textbox.setText(
                'One player out of chips\nGAME OVER.')
            QtTest.QTest.qWait(4000)
            newApp.quit()
        else:
            self.ui.hit_me_button.setEnabled(True)
            self.ui.hold_button.setEnabled(True)
            self.ui.enter_buttton.setText('')
            self.ui.bet_amount_edit.setText('')
            self.ui.player_textbox.setText(' Do you want to\nplay again?')
            self.ui.hit_me_button.setText(' YES ')
            self.ui.hold_button.setText(' NO ')
            # remove previous connect signal from buttons
            self.ui.hit_me_button.disconnect()
            self.ui.hold_button.disconnect()
            # set new signals
            self.ui.hold_button.clicked.connect(exit)
            self.ui.hit_me_button.clicked.connect(self.replay)

    def replay(self):
        """saves the round settings, and restarts newApp"""
        # global PLAYER_CHIPS, DEALER_CHIPS
        GLOBAL_SETTINGS['PLAYER_CHIPS'] = self.human_player.chips
        GLOBAL_SETTINGS["DEALER_CHIPS"] = self.dealer.chips
        newApp.exit(MainWindow.EXIT_CODE_REBOOT)  # needed for newApp restart


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

    def shuffle(self):
        """ randomizes all the cards in the deck"""
        random.shuffle(self.all_cards)

    def deal_one(self, player):
        """ adds one card to (player), removing it from the deck. """
        player.hand_cards.append(self.all_cards.pop(0))

    def deal_two(self, player):
        """ adds two cards to the (player), removing it from the deck. """
        for _ in range(2):
            player.hand_cards.append(self.all_cards.pop(0))


class Player:
    """ class for the user. to dealers_turn cards and methods. """

    # global PLAYER_CHIPS

    def __init__(self, name):
        self.name = name
        self.chips = GLOBAL_SETTINGS['PLAYER_CHIPS']
        self.hand_cards = []

    def add_chips(self, chips):
        """ add (chips) to player total. """
        self.chips += chips

    def bet_chips(self, chips):
        """ return number of (chips) the player bets. """
        self.chips -= chips
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
            if card3.rank == 'Ace' and temp_total > 21:
                temp_total -= 10
        return temp_total

    def __repr__(self):
        return self.name


class Dealer:
    """ class for Dealer/ computer player, and its methods. """

    # global DEALER_CHIPS

    def __init__(self):
        self.hand_cards = []
        self.chips = GLOBAL_SETTINGS["DEALER_CHIPS"]
        self.name = 'Dealer'

    def add_chips(self, chips):
        """ add (chips) to Dealer total. """
        self.chips += chips

    def bet_chips(self, chips):
        """ return number of (chips) the Dealer bets. """
        self.chips -= chips
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
        temp_total = 0
        for card3 in self.hand_cards[1:]:
            temp_total += card3.value
        return temp_total

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    currentExitCode = MainWindow.EXIT_CODE_REBOOT

    # will keep restarting the newApp as long as 'currentExitCode = MainWindow.EXIT_CODE_REBOOT'
    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        newApp = qtw.QApplication(sys.argv)
        newWindow = MainWindow()
        currentExitCode = newApp.exec_()
        newApp = None

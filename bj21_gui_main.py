import sys
import random
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic
from bj21_ui import Ui_MainWindow
from PyQt5 import QtTest


class MainWindow(qtw.QMainWindow):
    # or whatever number not already taken--needed for app restart
    EXIT_CODE_REBOOT = -12345678

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # creating new object from Ui_LoginForm, from login.ui
        self.ui = Ui_MainWindow()

        # calling method from class above, from login.ui
        self.ui.setupUi(self)

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
        self.play()

    def play(self):
        # constants for card suits and ranks , obv.
        self.SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                      'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                       'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
        self.TABLE_POT = 0
        self.next_card_slot_idx = 2

        # get username
        ask_name, bool1 = qtw.QInputDialog.getText(
            self, 'Welcome!', 'Welcome to Black Jack 21!\nEnter your name Player: ')

        # Setup deck,hands
        self.deck = Deck(self)
        self.deck.shuffle()
        self.dealer = Dealer()
        self.human_player = Player(ask_name.title(), self)
        self.ui.player_name.setText(f"{self.human_player}'s Cards")

        # deal chips and first 2 cards
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
        self.ui.enter_buttton.clicked.connect(self.make_bet)

    def make_bet(self):
        # request bet, check avail chips...

        try:
            bet_amount = int(self.ui.bet_amount_edit.text())
            self.ui.player_textbox.setText('Enter Bet Amount ...')

            if self.human_player.chips >= bet_amount and self.dealer.chips >= bet_amount:
                self.TABLE_POT += self.human_player.bet_chips(bet_amount)
                self.TABLE_POT += self.dealer.bet_chips(bet_amount)
                self.ui.pot_total.setText(f'Pot Total: {self.TABLE_POT}')
                self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
                self.ui.player_chips.setText(
                    f'Chips: {self.human_player.chips}')
                # self.ui.bet_amount_edit.setVisible(False)
                # self.ui.enter_buttton.setVisible(False)
                self.ui.bet_amount_edit.setEnabled(False)
                self.ui.enter_buttton.setEnabled(False)
                self.ui.player_textbox.setText('Hit or Hold?')
                self.ui.hit_me_button.clicked.connect(self.hit_me)
                self.ui.hold_button.clicked.connect(self.hold)

            else:
                self.ui.player_textbox.setText(
                    'Not enough chips in the bank, try again.')

        except ValueError:
            self.ui.player_textbox.setText('Must be a number, try again.')

    def hit_me(self):

        self.deck.deal_one(self.human_player)

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
        self.next_card_slot_idx += 1

        self.ui.player_total.setText(
            f'Total: {self.human_player.total()}')

        if self.human_player.bust():
            self.ui.hit_me_button.setEnabled(False)
            self.ui.hold_button.setEnabled(False)
            self.ui.player_total.setText(
                f'Total: {self.human_player.total()}')
            # self.ui.player_textbox.setText('Player Busts!!\nGame Over!')
            self.hold()

    def hold(self):
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

            if self.dealer.bust():
                self.ui.dealer_total.setText(
                    f'Total: {self.dealer.total()}')
        self.winner_is()

    def winner_is(self):
        # determine winner, add chips to players total etc

        # show dealer hidden card, and total including hidden card value
        self.ui.dealer_total.setText(
            f'Total: {self.dealer.total()}')
        self.ui.dealer_card1.setText(
            f'{self.dealer.hand_cards[0]}')

        # dealer busts, add pot chips to player
        if self.dealer.bust():
            self.ui.player_textbox.setText(
                f'Dealer Busts.{self.human_player.name} Wins!')
            self.human_player.add_chips(self.TABLE_POT)
            self.ui.player_chips.setText(
                f'Chips: {self.human_player.chips}')
            self.ui.pot_total.setText(f'Pot: 0')
        # player busts, add chips to dealer

        elif self.human_player.bust():
            self.ui.player_textbox.setText(
                f'{self.human_player} Busts.\nDealer Wins!')
            self.dealer.add_chips(self.TABLE_POT)
            self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
            self.ui.pot_total.setText(f'Pot: 0')

        # tie, pot remains
        elif self.dealer.total() == self.human_player.total():
            self.ui.player_textbox.setText('''It's A Tie...''')

        # dealer wins, add chips to dealer pot
        elif self.dealer.total() > self.human_player.total():
            self.ui.player_textbox.setText('Dealer Wins!')
            self.dealer.add_chips(self.TABLE_POT)
            self.ui.dealer_chips.setText(f'Chips: {self.dealer.chips}')
            self.ui.pot_total.setText(f'Pot: 0')

        # player wins, add chips to player
        elif self.dealer.total() < self.human_player.total():
            self.ui.player_textbox.setText(
                f'{self.human_player.name} Wins!')
            self.human_player.add_chips(self.TABLE_POT)
            self.ui.player_chips.setText(
                f'Chips: {self.human_player.chips}')
            self.ui.pot_total.setText(f'Pot: 0')

        QtTest.QTest.qWait(4000)
        if self.human_player.chips == 0 or self.dealer.chips == 0:
            self.ui.player_textbox.setText(
                'One player out of chips\nGAME OVER.')
            QtTest.QTest.qWait(4000)
            app.quit()
        else:
            self.ui.hit_me_button.setEnabled(True)
            self.ui.hold_button.setEnabled(True)
            self.ui.enter_buttton.setText(' ')
            self.ui.bet_amount_edit.setText(' ')
            self.ui.player_textbox.setText(' Do you want to\nPlay again?')
            self.ui.hit_me_button.setText(' YES ')
            self.ui.hold_button.setText(' NO ')
            self.ui.hold_button.clicked.connect(exit)
            self.ui.hit_me_button.clicked.connect(self.replay)

    def replay(self):
        app.exit(MainWindow.EXIT_CODE_REBOOT)  # needed for app restart
        # del self.deck
        # del self.dealer
        # del self.human_player

        # self.play()


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
    """ class for the user. to hold cards and methods. """

    def __init__(self, name, win_obj):
        self.name = name
        self.chips = 100
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
            if 'Ace' == card3.rank and temp_total > 21:
                temp_total -= 10
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
        GAME_ON = False


if __name__ == '__main__':
    currentExitCode = MainWindow.EXIT_CODE_REBOOT

    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        app = qtw.QApplication(sys.argv)
        w = MainWindow()
        currentExitCode = app.exec_()
        app = None

    # return currentExitCode

    # app = qtw.QApplication(sys.argv)
    # w = MainWindow()
    # sys.exit(app.exec())

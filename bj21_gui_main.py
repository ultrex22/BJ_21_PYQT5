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
        deck = Deck(self)
        deck.shuffle()
        dealer = Dealer()
        human_player = Player(ask_name, self)
        self.ui.player_name.setText(f"{human_player}'s Cards")

        # deal chips and update gui
        print(f'{human_player.name} has {human_player.chips} chips.')
        print(f'Dealer has {dealer.chips} chips.')
        self.ui.player_chips.setText(f'Chips: {human_player.chips}')
        self.ui.dealer_chips.setText(f'Chips: {dealer.chips}')
        deck.deal_two(dealer)
        deck.deal_two(human_player)
        self.ui.dealer_card1.setText('CARD HIDDEN')
        self.ui.dealer_card2.setText(f'{dealer.hand_cards[1]}')
        self.ui.player_card1.setText(f'{human_player.hand_cards[0]}')
        self.ui.player_card2.setText(f'{human_player.hand_cards[1]}')

        # request bet, check avail chips...
        bet = True
        while bet == True:
            try:
                bet_amount, bool2 = qtw.QInputDialog.getText(
                    self, 'Bet', 'How much do you want to bet? ')
                bet_amount = int(bet_amount)
            except ValueError:
                print('Must be a number.')
                continue
            if human_player.chips >= bet_amount and dealer.chips >= bet_amount:
                print(human_player.chips >=
                      bet_amount and dealer.chips >= bet_amount)
                self.TABLE_POT += human_player.bet_chips(bet_amount)
                self.TABLE_POT += dealer.bet_chips(bet_amount)
                self.ui.pot_total.setText(f'Pot Total: {self.TABLE_POT}')
                self.ui.dealer_chips.setText(f'Chips: {dealer.chips}')
                self.ui.player_chips.setText(f'Chips: {human_player.chips}')
                self.ui.player_total.setText(f'Total: {human_player.total()}')
                self.ui.dealer_total.setText(
                    f'Total: {dealer.total_visible()}')

                print(f'Table Pot: {self.TABLE_POT}\n')
                bet = False
                break
            else:
                print('Not enough chips in the bank to bet that amount.\n')

        # --- main game loops ---
        # players turn
        PLAYERS_TURN = True
        while PLAYERS_TURN:

            # print cards in hands
            print(f'Dealers Face Card: {dealer.hand_cards[0]}.')
            print('--------------------')
            print(f"\n{human_player.name}'s Hand:",
                  *human_player.hand_cards, sep="\n ")
            print(f'{human_player.name} Cards Total: {human_player.total()}')
            # see if player wants another card , check for bust.
            if not human_player.bust():
                hit_me = input(
                    'Do you want to Hit and take another card (y/n) ? \n').lower()
                if hit_me == 'y':
                    # system('clear')
                    deck.deal_one(human_player)

                else:
                    DEALERS_TURN = True
                    break
            elif human_player.bust():
                print(f'{human_player.name} BUSTS!')
                DEALERS_TURN = False
                PLAYERS_TURN = False

        # sub loop, dealers turn, keep adding cards if total cards < 17
        while DEALERS_TURN and dealer.total() < 17:
            if not dealer.bust():
                print('--------------------')
                deck.deal_one(dealer)
                print(f'Dealers Cards: {dealer.hand_cards[0]}.')
                for card4 in dealer.hand_cards[2:]:
                    print(f'Dealers Cards: {card4}.')
            elif dealer.bust():
                print('DEALER BUSTS!')
                DEALERS_TURN = False

        # determine winner, add chips to players total
        print('--------------------')
        print(f'Dealer Total: {dealer.total()}')
        print(f'Player Total: {human_player.total()}')
        print('--------------------')
        if dealer.bust():
            print(f'{human_player.name} wins!!!')
            human_player.add_chips(self.TABLE_POT)
        elif human_player.bust():
            print('Dealer Wins!!!')
            dealer.add_chips(self.TABLE_POT)
        elif dealer.total() == human_player.total():
            print('TIE !!!')
        elif dealer.total() > human_player.total():
            print('Dealer Wins!!!')
            dealer.add_chips(self.TABLE_POT)
        elif dealer.total() < human_player.total():
            print(f'{human_player.name} wins!!!')
            human_player.add_chips(self.TABLE_POT)

        # replay
        if human_player.chips == 0 or dealer.chips == 0:
            print('One player out of chips, GAME OVER.')
            print('\nGoodbye!')
            GAME_ON = False

        again = input('\nPlay again? (y/n) ')
        if again == 'y':
            deck.all_cards.extend(dealer.hand_cards)
            deck.all_cards.extend(human_player.hand_cards)
            dealer.hand_cards.clear()
            human_player.hand_cards.clear()
            self.TABLE_POT = 0
            # system('clear')
            # continue

        print('\nGoodbye!')


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

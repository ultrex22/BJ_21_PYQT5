# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bj21.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #eeeeee;\n"
"color: rgb(54, 54, 54)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(240, 50, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setItalic(True)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(0, 0, 127)")
        self.title.setObjectName("title")
        self.dealer_name = QtWidgets.QLabel(self.centralwidget)
        self.dealer_name.setGeometry(QtCore.QRect(20, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.dealer_name.setFont(font)
        self.dealer_name.setStyleSheet("color:rgb(255, 0, 0)")
        self.dealer_name.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_name.setObjectName("dealer_name")
        self.player_name = QtWidgets.QLabel(self.centralwidget)
        self.player_name.setGeometry(QtCore.QRect(400, 170, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.player_name.setFont(font)
        self.player_name.setStyleSheet("color:black;")
        self.player_name.setAlignment(QtCore.Qt.AlignCenter)
        self.player_name.setWordWrap(True)
        self.player_name.setObjectName("player_name")
        self.pot_total = QtWidgets.QLabel(self.centralwidget)
        self.pot_total.setGeometry(QtCore.QRect(230, 410, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pot_total.setFont(font)
        self.pot_total.setFrameShape(QtWidgets.QFrame.Box)
        self.pot_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pot_total.setAlignment(QtCore.Qt.AlignCenter)
        self.pot_total.setObjectName("pot_total")
        self.dealer_card1 = QtWidgets.QLabel(self.centralwidget)
        self.dealer_card1.setGeometry(QtCore.QRect(30, 230, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dealer_card1.setFont(font)
        self.dealer_card1.setStyleSheet("color: rgb(255, 0, 0);")
        self.dealer_card1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dealer_card1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dealer_card1.setText("")
        self.dealer_card1.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_card1.setObjectName("dealer_card1")
        self.dealer_card2 = QtWidgets.QLabel(self.centralwidget)
        self.dealer_card2.setGeometry(QtCore.QRect(30, 280, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dealer_card2.setFont(font)
        self.dealer_card2.setStyleSheet("color: rgb(255, 0, 0);")
        self.dealer_card2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dealer_card2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dealer_card2.setText("")
        self.dealer_card2.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_card2.setObjectName("dealer_card2")
        self.dealer_card3 = QtWidgets.QLabel(self.centralwidget)
        self.dealer_card3.setGeometry(QtCore.QRect(30, 330, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dealer_card3.setFont(font)
        self.dealer_card3.setStyleSheet("color: rgb(255, 0, 0);")
        self.dealer_card3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dealer_card3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dealer_card3.setText("")
        self.dealer_card3.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_card3.setObjectName("dealer_card3")
        self.dealer_card4 = QtWidgets.QLabel(self.centralwidget)
        self.dealer_card4.setGeometry(QtCore.QRect(30, 380, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dealer_card4.setFont(font)
        self.dealer_card4.setStyleSheet("color: rgb(255, 0, 0);")
        self.dealer_card4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dealer_card4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dealer_card4.setText("")
        self.dealer_card4.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_card4.setObjectName("dealer_card4")
        self.dealer_card5 = QtWidgets.QLabel(self.centralwidget)
        self.dealer_card5.setGeometry(QtCore.QRect(30, 430, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dealer_card5.setFont(font)
        self.dealer_card5.setStyleSheet("color:red;")
        self.dealer_card5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.dealer_card5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.dealer_card5.setText("")
        self.dealer_card5.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_card5.setObjectName("dealer_card5")
        self.dealer_total = QtWidgets.QLabel(self.centralwidget)
        self.dealer_total.setGeometry(QtCore.QRect(90, 470, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dealer_total.setFont(font)
        self.dealer_total.setStyleSheet("color:rgb(255, 0, 0)")
        self.dealer_total.setFrameShape(QtWidgets.QFrame.Box)
        self.dealer_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dealer_total.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_total.setObjectName("dealer_total")
        self.player_total = QtWidgets.QLabel(self.centralwidget)
        self.player_total.setGeometry(QtCore.QRect(390, 470, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.player_total.setFont(font)
        self.player_total.setStyleSheet("color:black")
        self.player_total.setFrameShape(QtWidgets.QFrame.Box)
        self.player_total.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_total.setAlignment(QtCore.Qt.AlignCenter)
        self.player_total.setObjectName("player_total")
        self.player_card2 = QtWidgets.QLabel(self.centralwidget)
        self.player_card2.setGeometry(QtCore.QRect(420, 280, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.player_card2.setFont(font)
        self.player_card2.setStyleSheet("color: rgb(0, 0, 0);")
        self.player_card2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.player_card2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_card2.setText("")
        self.player_card2.setAlignment(QtCore.Qt.AlignCenter)
        self.player_card2.setObjectName("player_card2")
        self.player_card3 = QtWidgets.QLabel(self.centralwidget)
        self.player_card3.setGeometry(QtCore.QRect(420, 330, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.player_card3.setFont(font)
        self.player_card3.setStyleSheet("color: rgb(0, 0, 0);")
        self.player_card3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.player_card3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_card3.setText("")
        self.player_card3.setAlignment(QtCore.Qt.AlignCenter)
        self.player_card3.setObjectName("player_card3")
        self.player_card1 = QtWidgets.QLabel(self.centralwidget)
        self.player_card1.setGeometry(QtCore.QRect(420, 230, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.player_card1.setFont(font)
        self.player_card1.setStyleSheet("color: rgb(0, 0, 0);")
        self.player_card1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.player_card1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_card1.setText("")
        self.player_card1.setAlignment(QtCore.Qt.AlignCenter)
        self.player_card1.setObjectName("player_card1")
        self.player_card4 = QtWidgets.QLabel(self.centralwidget)
        self.player_card4.setGeometry(QtCore.QRect(420, 380, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.player_card4.setFont(font)
        self.player_card4.setStyleSheet("color: rgb(0, 0, 0);")
        self.player_card4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.player_card4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_card4.setText("")
        self.player_card4.setAlignment(QtCore.Qt.AlignCenter)
        self.player_card4.setObjectName("player_card4")
        self.player_card5 = QtWidgets.QLabel(self.centralwidget)
        self.player_card5.setGeometry(QtCore.QRect(420, 430, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.player_card5.setFont(font)
        self.player_card5.setStyleSheet("color: rgb(0, 0, 0);")
        self.player_card5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.player_card5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.player_card5.setText("")
        self.player_card5.setAlignment(QtCore.Qt.AlignCenter)
        self.player_card5.setObjectName("player_card5")
        self.dealer_chips = QtWidgets.QLabel(self.centralwidget)
        self.dealer_chips.setGeometry(QtCore.QRect(110, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dealer_chips.setFont(font)
        self.dealer_chips.setStyleSheet("color:rgb(255, 0, 0)")
        self.dealer_chips.setFrameShape(QtWidgets.QFrame.Box)
        self.dealer_chips.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dealer_chips.setAlignment(QtCore.Qt.AlignCenter)
        self.dealer_chips.setObjectName("dealer_chips")
        self.player_chips = QtWidgets.QLabel(self.centralwidget)
        self.player_chips.setGeometry(QtCore.QRect(370, 520, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.player_chips.setFont(font)
        self.player_chips.setStyleSheet("color:black")
        self.player_chips.setFrameShape(QtWidgets.QFrame.Box)
        self.player_chips.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_chips.setAlignment(QtCore.Qt.AlignCenter)
        self.player_chips.setObjectName("player_chips")
        self.icon1 = QtWidgets.QPushButton(self.centralwidget)
        self.icon1.setGeometry(QtCore.QRect(80, 30, 61, 81))
        self.icon1.setText("")
        self.icon1.setFlat(True)
        self.icon1.setObjectName("icon1")
        self.icon2 = QtWidgets.QPushButton(self.centralwidget)
        self.icon2.setGeometry(QtCore.QRect(150, 50, 61, 81))
        self.icon2.setText("")
        self.icon2.setFlat(True)
        self.icon2.setObjectName("icon2")
        self.player_textbox = QtWidgets.QLabel(self.centralwidget)
        self.player_textbox.setGeometry(QtCore.QRect(200, 160, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.player_textbox.setFont(font)
        self.player_textbox.setStyleSheet("color:green;")
        self.player_textbox.setAlignment(QtCore.Qt.AlignCenter)
        self.player_textbox.setWordWrap(True)
        self.player_textbox.setObjectName("player_textbox")
        self.hit_me_button = QtWidgets.QToolButton(self.centralwidget)
        self.hit_me_button.setGeometry(QtCore.QRect(240, 320, 111, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hit_me_button.setFont(font)
        self.hit_me_button.setIconSize(QtCore.QSize(16, 16))
        self.hit_me_button.setObjectName("hit_me_button")
        self.hold_button = QtWidgets.QToolButton(self.centralwidget)
        self.hold_button.setGeometry(QtCore.QRect(240, 360, 111, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hold_button.setFont(font)
        self.hold_button.setIconSize(QtCore.QSize(16, 16))
        self.hold_button.setObjectName("hold_button")
        self.bet_amount_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.bet_amount_edit.setGeometry(QtCore.QRect(240, 240, 113, 32))
        self.bet_amount_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.bet_amount_edit.setObjectName("bet_amount_edit")
        self.enter_buttton = QtWidgets.QPushButton(self.centralwidget)
        self.enter_buttton.setGeometry(QtCore.QRect(240, 280, 111, 34))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.enter_buttton.setFont(font)
        self.enter_buttton.setIconSize(QtCore.QSize(16, 16))
        self.enter_buttton.setObjectName("enter_buttton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Black Jack 21 - The Game"))
        self.title.setText(_translate("MainWindow", "Black Jack 21"))
        self.dealer_name.setText(_translate("MainWindow", "Dealer Cards"))
        self.player_name.setText(_translate("MainWindow", "Player Cards"))
        self.pot_total.setText(_translate("MainWindow", "Pot Total: 0"))
        self.dealer_total.setText(_translate("MainWindow", "Total: 0"))
        self.player_total.setText(_translate("MainWindow", "Total: 0"))
        self.dealer_chips.setText(_translate("MainWindow", "Chips:  100"))
        self.player_chips.setText(_translate("MainWindow", "Chips:  100"))
        self.player_textbox.setText(_translate("MainWindow", "Enter Bet Below..."))
        self.hit_me_button.setText(_translate("MainWindow", "Hit Me!"))
        self.hold_button.setText(_translate("MainWindow", "Hold"))
        self.bet_amount_edit.setPlaceholderText(_translate("MainWindow", "Bet $"))
        self.enter_buttton.setText(_translate("MainWindow", "ENTER"))

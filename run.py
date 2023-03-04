import logging
import sys

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from typing import List

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

# maybe implement with an on-map and off-map
class SuitButton(QAbstractButton):
    def __init__(self, pixmaps=[], parent=None):
        super(SuitButton, self).__init__(parent)
        self.pixmaps = pixmaps
        self.i = 0

    def reset(self, count=0):
        self.i = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmaps[self.i])

    def sizeHint(self):
        return self.pixmaps[self.i].size() / 6

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.i = (self.i + 1) % len(self.pixmaps)
        elif event.button() == Qt.MouseButton.RightButton:
            self.i = (self.i - 1) % len(self.pixmaps)
        self.update()


class PicButton(QAbstractButton):
    def __init__(self, pixmap, parent=None, count=3):
        super(PicButton, self).__init__(parent)
        self.pixmap = pixmap
        self.count = count
        self.start_count = self.count

        # self.pressed.connect(self.onClick)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.GlobalColor.red)
        painter.drawPixmap(event.rect(), self.pixmap)
        numLocation = event.rect().topRight()
        logging.debug(f'topRight: {numLocation}')
        center = event.rect().center()
        logging.debug(f'center: {center}')
        numLocation.setX(numLocation.x() - 11)
        numLocation.setY(numLocation.y() + 12)
        logging.debug(f'text location: {numLocation}')
        painter.drawText(numLocation, f'{self.count}')

    def reset(self, count: int):
        self.start_count = count
        self.count = self.start_count

    # def onClick(self):
    #     if self.count > 0:
    #         self.count -= 1

    def sizeHint(self):
        return self.pixmap.size() / 6

    def mousePressEvent(self, event):
        # override this to handle right clicking
        # want to use right click to increase count in case of misclick
        if event.button() == Qt.MouseButton.LeftButton:
            if self.count > 0:
                self.count -= 1
        elif event.button() == Qt.MouseButton.RightButton:
            self.count += 1
        self.update()

def resetButtons(buttons: List[PicButton], count) -> None:
    for button in buttons:
        button.reset(count)
        button.update()

if __name__ == "__main__":
    p = ArgumentParser(
        description="Runs a graphical card-counting helper for poker.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("-n", "--num_cards", type=int, default=3, help="number of cards to start with")
    args = p.parse_args()

    app = QApplication(sys.argv)
    window = QWidget()
    layout = QGridLayout(window)
    buttons = []

    button1 = PicButton(QPixmap("cards/ace_of_spades.png"))
    button2 = PicButton(QPixmap("cards/2_of_spades.png"))
    button3 = PicButton(QPixmap("cards/3_of_spades.png"))
    button4 = PicButton(QPixmap("cards/4_of_spades.png"))
    button5 = PicButton(QPixmap("cards/5_of_spades.png"))
    button6 = PicButton(QPixmap("cards/6_of_spades.png"))
    button7 = PicButton(QPixmap("cards/7_of_spades.png"))
    button8 = PicButton(QPixmap("cards/8_of_spades.png"))
    button9 = PicButton(QPixmap("cards/9_of_spades.png"))
    button10 = PicButton(QPixmap("cards/10_of_spades.png"))
    button11 = PicButton(QPixmap("cards/jack_of_spades2.png"))
    button12 = PicButton(QPixmap("cards/queen_of_spades2.png"))
    button13 = PicButton(QPixmap("cards/king_of_spades2.png"))
    button14 = PicButton(QPixmap("cards/black_joker.png"))
    button15 = PicButton(QPixmap("cards/red_joker.png"))

    button16 = PicButton(QPixmap("cards/ace_of_hearts.png"))
    button17 = PicButton(QPixmap("cards/ace_of_diamonds.png"), count=9)

    buttons = [
        button1,
        button2,
        button3,
        button4,
        button5,
        button6,
        button7,
        button8,
        button9,
        button10,
        button11,
        button12,
        button13,
        button14,
        button15,
        button16,
        # button17,
    ]

    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
    layout.addWidget(button14, 0, 1)
    layout.addWidget(button15, 0, 0)
    layout.addWidget(button16, 0, 2)
    layout.addWidget(button17, 0, 3)

    layout.addWidget(button1, 1, 0)
    layout.addWidget(button13, 1, 1)
    layout.addWidget(button12, 1, 2)
    layout.addWidget(button11, 1, 3)
    layout.addWidget(button10, 1, 4)
    layout.addWidget(button9, 1, 5)
    layout.addWidget(button8, 1, 6)
    layout.addWidget(button7, 2, 0)
    layout.addWidget(button6, 2, 1)
    layout.addWidget(button5, 2, 2)
    layout.addWidget(button4, 2, 3)
    layout.addWidget(button3, 2, 4)
    layout.addWidget(button2, 2, 5)

    window2 = QWidget()
    layout = QGridLayout(window2)

    aces = [
        QPixmap("cards/red_joker.png"),
        QPixmap("cards/ace_of_spades.png"),
        QPixmap("cards/ace_of_hearts.png"),
        QPixmap("cards/ace_of_diamonds.png"),
        QPixmap("cards/ace_of_clubs.png"),
    ]
    suits1 = SuitButton(pixmaps=aces)
    suits2 = SuitButton(pixmaps=aces)
    suits3 = SuitButton(pixmaps=aces)
    suits4 = SuitButton(pixmaps=aces)
    suits5 = SuitButton(pixmaps=aces)

    buttons.append(suits1)
    buttons.append(suits2)
    buttons.append(suits3)
    buttons.append(suits4)
    buttons.append(suits5)

    layout.addWidget(suits1, 0, 1)
    layout.addWidget(suits2, 1, 0)
    layout.addWidget(suits3, 1, 2)
    layout.addWidget(suits4, 2, 0)
    layout.addWidget(suits5, 2, 2)

    window3 = QWidget()
    layout = QGridLayout(window3)
    a_s = PicButton(QPixmap("cards/ace_of_spades.png"))
    a_h = PicButton(QPixmap("cards/ace_of_hearts.png"))
    a_d = PicButton(QPixmap("cards/ace_of_diamonds.png"))
    a_c = PicButton(QPixmap("cards/ace_of_clubs.png"))
    k_s = PicButton(QPixmap("cards/king_of_spades2.png"))
    k_h = PicButton(QPixmap("cards/king_of_hearts2.png"))
    k_d = PicButton(QPixmap("cards/king_of_diamonds2.png"))
    k_c = PicButton(QPixmap("cards/king_of_clubs2.png"))
    ten_s = PicButton(QPixmap("cards/10_of_spades.png"))
    ten_h = PicButton(QPixmap("cards/10_of_hearts.png"))
    ten_d = PicButton(QPixmap("cards/10_of_diamonds.png"))
    ten_c = PicButton(QPixmap("cards/10_of_clubs.png"))
    buttons.append(a_s)
    buttons.append(a_h)
    buttons.append(a_d)
    buttons.append(a_c)
    buttons.append(k_s)
    buttons.append(k_h)
    buttons.append(k_d)
    buttons.append(k_c)
    buttons.append(ten_s)
    buttons.append(ten_h)
    buttons.append(ten_d)
    buttons.append(ten_c)
    layout.addWidget(a_s, 0, 0)
    layout.addWidget(a_h, 0, 1)
    layout.addWidget(a_d, 0, 2)
    layout.addWidget(a_c, 0, 3)
    layout.addWidget(k_s, 1, 0)
    layout.addWidget(k_h, 1, 1)
    layout.addWidget(k_d, 1, 2)
    layout.addWidget(k_c, 1, 3)
    layout.addWidget(ten_s, 2, 0)
    layout.addWidget(ten_h, 2, 1)
    layout.addWidget(ten_d, 2, 2)
    layout.addWidget(ten_c, 2, 3)

    # text entry line for user-defined count
    entry = QLineEdit(window)
    def handleEntry():
        logging.debug(f"handling entry with input: {entry.text()}")
        count = int(entry.text())
        for button in buttons:  # set all button counts according to to user input
            button.count = count
            button.update()
            button17.count = count * 3
            button17.update()

    entry.returnPressed.connect(handleEntry)  # optionally press enter to process input number
    layout.addWidget(entry, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)

    def handleReset(buttons, count=3):
        resetButtons(buttons, count)
        button17.reset(count * 3)
        button17.update()

    resetButton = QPushButton("Reset")
    # hook up line edit field to reset button for a more intuitive user experience
    resetButton.clicked.connect(
        lambda _: handleReset(buttons, int(entry.text()) if entry.text() else 3)
    )
    layout.addWidget(resetButton, 0, 4)

    window.show()
    window2.show()
    window3.show()
    sys.exit(app.exec())

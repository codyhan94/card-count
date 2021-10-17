import logging
import sys

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

# maybe implement with an on-map and off-map
class SuitButton(QAbstractButton):
    def __init__(self, pixmaps=[], parent=None):
        super(SuitButton, self).__init__(parent)
        self.pixmaps = pixmaps
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

        # self.pressed.connect(self.onClick)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.GlobalColor.red)
        painter.drawPixmap(event.rect(), self.pixmap)
        numLocation = event.rect().topRight()
        logging.debug(f'topRight: {numLocation}')
        center = event.rect().center()
        logging.debug(f'center: {center}')
        numLocation.setX(numLocation.x() - 9)
        numLocation.setY(numLocation.y() + 12)
        logging.debug(f'text location: {numLocation}')
        painter.drawText(numLocation, f'{self.count}')

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

app = QApplication(sys.argv)
window = QWidget()
layout = QGridLayout(window)

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

button16 = PicButton(QPixmap("cards/ace_of_hearts.png"), count=0)
button17 = PicButton(QPixmap("cards/ace_of_diamonds.png"), count=0)

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

layout.addWidget(suits1, 0, 1)
layout.addWidget(suits2, 1, 0)
layout.addWidget(suits3, 1, 2)
layout.addWidget(suits4, 2, 0)
layout.addWidget(suits5, 2, 2)
# layout.addWidget(button1, 2, 6)
# def on_click():
#     alert = QMessageBox()
#     alert.setText('clicked')
#     alert.exec()

# button.clicked.connect(on_click)

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
layout.addWidget(a_s, 0, 0)
layout.addWidget(a_h, 0, 1)
layout.addWidget(a_d, 0, 2)
layout.addWidget(a_c, 0, 3)
layout.addWidget(k_s, 1, 0)
layout.addWidget(k_h, 1, 1)
layout.addWidget(k_d, 1, 2)
layout.addWidget(k_c, 1, 3)

window.show()
window2.show()
window3.show()
sys.exit(app.exec())

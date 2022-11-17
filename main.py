import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.bt.clicked.connect(self.run)

    def run(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))

        side = randint(0, 255)
        qp.drawEllipse(QRect(randint(0, 500), randint(0, 500), side, side))
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

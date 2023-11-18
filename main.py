import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
        self.do_paint = False

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = randint(1, 120)
        qp.drawEllipse(170, 170, 200 + r, 200 + r)

    def paint(self):
        self.do_paint = True
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
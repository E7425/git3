import sys
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication
from UI import Ui_MainWindow


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
        self.do_paint = False

    def draw_circles(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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
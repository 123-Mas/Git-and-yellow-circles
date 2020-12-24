import sys
import random


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Circles(QWidget):
    def __init__(self):
        super(Circles, self).__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.clicked)

    def clicked(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = random.choice(range(20, 100))
        x = random.choice(range(30, 450))
        y = random.choice(range(30, 510))
        qp.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)


if __name__ == "__main__":
    app = QApplication([])
    widget = Circles()
    widget.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QImage, QBrush, QColor
from PyQt5 import uic
from PyQt5.QtCore import QPointF


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('rect.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.is_draw = False

    def paintEvent(self, event):
        if self.is_draw:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        try:
            self.side = int(self.lineEdit.text())
            self.coeff = float(self.lineEdit_2.text())
            self.n = int(self.lineEdit_3.text())

            x, y = self.side // 2, self.side // 2
            for i in range(self.n):
                qp.drawRect(x, y, self.side, self.side)
                x += (self.side - self.side * self.coeff) // 2
                y += (self.side - self.side * self.coeff) // 2
                self.side *= self.coeff

        except Exception:
            print('Ошибка')

    def paint(self):
        self.is_draw = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec())

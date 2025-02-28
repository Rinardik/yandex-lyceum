import sys
import random
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtCore import Qt
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.circles = []
        self.button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        radius = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for circle in self.circles:
            x, y, radius, color = circle
            painter.setBrush(QBrush(color, Qt.BrushStyle.SolidPattern))
            painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
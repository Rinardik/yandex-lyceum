from PyQt6.QtWidgets import QPushButton


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Random Circles")
        MainWindow.setGeometry(100, 100, 800, 600)

        # Создаем кнопку
        self.button = QPushButton("Draw Circle", MainWindow)
        self.button.setGeometry(350, 350, 100, 30)
import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_coffee_data()

    def load_coffee_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зернах', 'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
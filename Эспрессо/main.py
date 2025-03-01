import sys
import sqlite3
from PyQt6 import QtWidgets, uic

# Подключение к базе данных
conn = sqlite3.connect('coffee.sqlite')
cursor = conn.cursor()

# Загрузка UI-файлов
form_main, base_main = uic.loadUiType("main.ui")
form_add_edit, _ = uic.loadUiType("addEditCoffeeForm.ui")

class AddEditCoffeeForm(QtWidgets.QDialog, form_add_edit):
    def __init__(self, coffee_id=None):
        super().__init__()
        self.setupUi(self)
        self.coffee_id = coffee_id

        # Установка значений по умолчанию для ComboBox
        self.roastComboBox.addItems(["Легкая", "Средняя", "Темная"])
        self.typeComboBox.addItems(["молотый", "в зернах"])

        # Если передан coffee_id, загружаем данные для редактирования
        if coffee_id:
            cursor.execute("SELECT * FROM coffee WHERE id=?", (coffee_id,))
            data = cursor.fetchone()
            self.nameLineEdit.setText(data[1])
            self.roastComboBox.setCurrentText(data[2])
            self.typeComboBox.setCurrentText(data[3])
            self.descriptionTextEdit.setPlainText(data[4])
            self.priceSpinBox.setValue(data[5])
            self.volumeSpinBox.setValue(data[6])

        # Сохранение данных
        self.saveButton.clicked.connect(self.save_data)

    def save_data(self):
        name = self.nameLineEdit.text()
        roast = self.roastComboBox.currentText()
        type_ = self.typeComboBox.currentText()
        description = self.descriptionTextEdit.toPlainText()
        price = self.priceSpinBox.value()
        volume = self.volumeSpinBox.value()

        if self.coffee_id:  # Редактирование существующей записи
            cursor.execute(
                "UPDATE coffee SET name=?, roast=?, type=?, description=?, price=?, volume=? WHERE id=?",
                (name, roast, type_, description, price, volume, self.coffee_id)
            )
        else:  # Добавление новой записи
            cursor.execute(
                "INSERT INTO coffee (name, roast, type, description, price, volume) VALUES (?, ?, ?, ?, ?, ?)",
                (name, roast, type_, description, price, volume)
            )
        conn.commit()
        self.accept()


class MainWindow(QtWidgets.QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.refreshButton.clicked.connect(self.load_data)
        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)

    def load_data(self):
        self.tableWidget.setRowCount(0)
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        for row_number, row_data in enumerate(rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def add_coffee(self):
        dialog = AddEditCoffeeForm()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_data()

    def edit_coffee(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row != -1:
            coffee_id = int(self.tableWidget.item(selected_row, 0).text())
            dialog = AddEditCoffeeForm(coffee_id)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.load_data()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
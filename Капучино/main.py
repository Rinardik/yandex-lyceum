import sys
import sqlite3
from PyQt6 import QtWidgets, uic


class AddEditCoffeeForm(QtWidgets.QDialog):
    def __init__(self, coffee_id=None):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        
        self.coffee_id = coffee_id
        
        if coffee_id:
            self.load_coffee_data()
        
        self.pushButtonSave.clicked.connect(self.save_coffee)
        self.pushButtonCancel.clicked.connect(self.reject)

    def load_coffee_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee WHERE ID=?", (self.coffee_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            self.lineEditSortName.setText(row[1])
            self.lineEditRoastLevel.setText(row[2])
            self.lineEditGroundOrBeans.setText(row[3])
            self.lineEditTasteDescription.setText(row[4])
            self.lineEditPrice.setText(str(row[5]))
            self.lineEditVolume.setText(str(row[6]))

    def save_coffee(self):
        sort_name = self.lineEditSortName.text()
        roast_level = self.lineEditRoastLevel.text()
        ground_or_beans = self.lineEditGroundOrBeans.text()
        taste_description = self.lineEditTasteDescription.text()
        price = self.lineEditPrice.text()
        volume = self.lineEditVolume.text()

        if not all([sort_name, roast_level, ground_or_beans, taste_description, price, volume]):
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
            return

        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        if self.coffee_id:
            cursor.execute("""
                UPDATE coffee SET 
                sort_name=?, roast_level=?, ground_or_beans=?, taste_description=?, price=?, volume=?
                WHERE ID=?
            """, (sort_name, roast_level, ground_or_beans, taste_description, price, volume, self.coffee_id))
        else:
            cursor.execute("""
                INSERT INTO coffee (sort_name, roast_level, ground_or_beans, taste_description, price, volume)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (sort_name, roast_level, ground_or_beans, taste_description, price, volume))
        
        conn.commit()
        conn.close()
        self.accept()


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.load_data()
        
        self.pushButtonAdd.clicked.connect(self.add_coffee)
        self.pushButtonEdit.clicked.connect(self.edit_coffee)

    def load_data(self):
        conn = sqlite3.connect('coffee.sqlite')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        conn.close()
        
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

    def add_coffee(self):
        dialog = AddEditCoffeeForm()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_data()

    def edit_coffee(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите запись для редактирования!")
            return
        
        coffee_id = int(self.tableWidget.item(selected_row, 0).text())
        dialog = AddEditCoffeeForm(coffee_id)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_data()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
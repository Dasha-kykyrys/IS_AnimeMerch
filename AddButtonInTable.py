import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QTableView, QPushButton, QLabel, QHBoxLayout, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class ItemDelegate(QWidget):
    def __init__(self, text, parent=None):
        super(ItemDelegate, self).__init__(parent)

        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.label = QLabel(text)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.label)

        self.setLayout(layout)

        # Подключите обработчики событий для кнопок
        self.button1.clicked.connect(lambda: print(f'Button 1 clicked for: {text}'))
        self.button2.clicked.connect(lambda: print(f'Button 2 clicked for: {text}'))

class TableView(QWidget):
    def __init__(self):
        super().__init__()

        self.table_view = QTableView(self)
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderLabels(['Name', 'Actions'])

        # Подключение к СУБД PostgreSQL и загрузка данных
        self.load_data_from_db()

        self.table_view.setModel(self.model)

        # Настройка делегата
        for row in range(self.model.rowCount()):
            item = self.model.item(row, 1)
            item.setData(ItemDelegate(item.text()), Qt.UserRole)

            # Присвоение делегатов для каждой строки в таблице
            self.table_view.setIndexWidget(self.model.index(row, 1), ItemDelegate(self.model.item(row, 0).text()))

        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        self.setLayout(layout)

        self.setWindowTitle('QTableView Example')
        self.resize(600, 400)

    def load_data_from_db(self):
        try:
            # Подключитесь к вашей базе данных
            connection = psycopg2.connect(
                dbname='ваша_база_данных',
                user='ваш_пользователь',
                password='ваш_пароль',
                host='localhost',  # или IP вашей базы
                port='5432'        # порт по умолчанию
            )
            cursor = connection.cursor()

            # Выполните SQL запрос
            cursor.execute("SELECT name FROM your_table_name;")
            rows = cursor.fetchall()

            # Добавьте данные в модель
            for row in rows:
                self.model.appendRow([
                    QStandardItem(row[0]),
                    QStandardItem()
                ])

            cursor.close()
            connection.close()
        except Exception as e:
            print(f'Ошибка при подключении к базе данных: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableView()
    main.show()
    sys.exit(app.exec_())




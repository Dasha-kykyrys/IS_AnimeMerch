from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
from GUI import Ui_MainWindow, Ui_CreateEditAnime_form, Ui_CreateEditProduct_form, Ui_preview_form, ItemDelegateData, ItemDelegateCheck
from database import load_data_from_db, add_to_database_product, add_to_database_anime, delete_anime_by_name, \
    delete_product, update_anime, update_product, save_database
import re


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main_window = Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        #смена вкладок
        self.ui_main_window.catalog_button.clicked.connect(lambda: self.change_widget(0))
        self.ui_main_window.sales_button.clicked.connect(lambda: self.change_widget(1))
        self.ui_main_window.management_button.clicked.connect(lambda: self.change_widget(2))

        #Таблицы во вкладке управления
        self.ui_main_window.animetable_button.clicked.connect(self.open_anime_table)
        self.ui_main_window.productstable_button.clicked.connect(self.open_product_table)

        #открытие окон
        self.ui_main_window.print_sales_button.clicked.connect(self.open_preview)
        self.ui_main_window.print_button.clicked.connect(self.open_preview)
        self.ui_main_window.creat_button.clicked.connect(self.open_create)

        #Модель таблицы Каталог
        self.catalog_model = QStandardItemModel(0, 4, self)
        load_data_from_db(self.catalog_model, 'product_table')
        self.catalog_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во'])
        self.ui_main_window.catalog_table.setModel(self.catalog_model)
        for column in range(self.catalog_model.columnCount()): # Адаптирующиеся под данные столбцы
            self.ui_main_window.catalog_table.resizeColumnToContents(column)

        # Модель таблицы Чек
        self.check_model = QStandardItemModel(0, 3, self)
        self.check_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Кол-во'])
        self.ui_main_window.chek_table.setModel(self.check_model)
        for column in range(self.check_model.columnCount()): # Адаптирующиеся под данные столбцы
            self.ui_main_window.chek_table.resizeColumnToContents(column)

        # Модель таблицы Продажа
        self.sale_model = QStandardItemModel(0, 5, self)

        # Модель таблицы Товар
        self.product_model = QStandardItemModel(0, 5, self)

        # Модель таблицы Аниме
        self.anime_model = QStandardItemModel(0, 2, self)

        self.create_edit_product = CreateEditProduct( self.ui_main_window, self.product_model,self.add_delegate_managment)
        self.create_edit_anime = CreateEditAnime(self.ui_main_window, self.anime_model, self.add_delegate_managment)

        # Подключение обработчика кнопки добавления
        self.ui_main_window.add_button.clicked.connect(self.add_item_to_check)

    def add_item_to_check(self):
        # Получаем выделенные индексы в таблице каталога
        selected_indexes = self.ui_main_window.catalog_table.selectedIndexes()

        if not selected_indexes:
            return  # Если ничего не выбрано, выходим

        # Получаем индекс строки, выбранной пользователем
        selected_row = selected_indexes[0].row()

        # Получаем данные из выбранной строки
        item_number = self.catalog_model.item(selected_row, 0).text()  # №
        item_name = self.catalog_model.item(selected_row, 1).text()  # Наименование
        item_anime = self.catalog_model.item(selected_row, 2).text()  # Аниме
        item_price = self.catalog_model.item(selected_row, 3).text()  # Цена
        item_quantity = int(self.catalog_model.item(selected_row, 4).text())  # Кол-во

        # Проверяем, достаточно ли товара для добавления
        if item_quantity <= 0:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Недостаточно товара для добавления в чек!")
            return

        # Уменьшаем количество в каталоге
        new_quantity = item_quantity - 1  # Уменьшаем на 1 для добавления в чек
        self.catalog_model.setItem(selected_row, 4, QStandardItem(str(new_quantity)))  # Обновляем количество

        # Добавляем элемент в чек
        new_row = self.check_model.rowCount()
        self.check_model.insertRow(new_row)
        self.check_model.setItem(new_row, 0, QStandardItem(item_number))  # №
        self.check_model.setItem(new_row, 1, QStandardItem(item_name))  # Наименование
        self.check_model.setItem(new_row, 2, QStandardItem(item_anime))  # Аниме
        self.check_model.setItem(new_row, 3, QStandardItem("1"))  # Кол-во, добавляем 1

        # Удаляем строку из каталога
        self.catalog_model.removeRow(selected_row)


    def update_create_edit_anime(self, press_edit, current_name):
        self.create_edit_anime.press_edit = press_edit
        self.create_edit_anime.current_name = current_name

    def update_create_edit_product(self, press_edit, current_name, current_anime, current_price, current_count):
        self.create_edit_product.press_edit = press_edit
        self.create_edit_product.current_name = current_name
        self.create_edit_product.current_anime = current_anime
        self.create_edit_product.current_price = current_price
        self.create_edit_product.current_count = current_count

    def change_widget(self, index):
        if index == 0: # Открытие Каталога
            self.ui_main_window.catalog_button.setEnabled(False)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(True)

        if index == 1: # Открытие Продажи
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(False)
            self.ui_main_window.management_button.setEnabled(True)

            self.sale_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Дата'])
            self.ui_main_window.sales_table.setModel(self.sale_model)
            for column in range(self.sale_model.columnCount()): # Адаптирующиеся под данные столбцы
                self.ui_main_window.sales_table.resizeColumnToContents(column)

        if index == 2: # Открытие Управление
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(False)

            self.open_product_table()

        self.ui_main_window.stacked_widget.setCurrentIndex(index)

    def open_anime_table(self):
        self.ui_main_window.print_button.hide()
        self.ui_main_window.productstable_button.setEnabled(True)
        self.ui_main_window.animetable_button.setEnabled(False)

        load_data_from_db(self.anime_model, 'anime_table')
        self.anime_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Действие'])
        self.ui_main_window.management_table.setModel(self.anime_model)
        self.add_delegate_managment(self.anime_model, self.ui_main_window.management_table, 2)
        for column in range(self.anime_model.columnCount()): # Адаптирующиеся под данные столбцы
            self.ui_main_window.management_table.resizeColumnToContents(column)

    def open_product_table(self):
        self.ui_main_window.print_button.show()
        self.ui_main_window.animetable_button.setEnabled(True)
        self.ui_main_window.productstable_button.setEnabled(False)

        load_data_from_db(self.product_model, 'product_table')
        self.product_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Действие'])
        self.ui_main_window.management_table.setModel(self.product_model)
        self.add_delegate_managment(self.product_model, self.ui_main_window.management_table, 5)
        for column in range(self.product_model.columnCount()): # Адаптирующиеся под данные столбцы
            self.ui_main_window.management_table.resizeColumnToContents(column)

    def open_create(self):
        if self.ui_main_window.productstable_button.isEnabled(): # Если активна кнопка "Товары", то открыта таблица Аниме
            self.create_edit_anime.ui_create_edit_anime.name_textedit.clear()
            self.create_edit_anime.setWindowModality(Qt.ApplicationModal)
            self.create_edit_anime.show()
        else:
            self.create_edit_product.clear_text()
            self.create_edit_product.setWindowModality(Qt.ApplicationModal)
            self.create_edit_product.show()

    def open_preview(self):
        preview.setWindowModality(Qt.ApplicationModal)
        preview.show()

    def add_delegate_managment(self, model, table, number):
        for row in range(model.rowCount()):
            item = model.item(row, 1)

            if item is not None:
                item_delegate = ItemDelegateData(row)
                table.setIndexWidget(model.index(row, number), item_delegate)  # Установка кнопок редактирования и удаления в таблицу

                item_delegate.button_clicked.connect(self.handle_button_click)

    def handle_button_click(self, button_type, row_number):
        type_button = button_type # Определение кнопки
        number_row = row_number # Определение в какой она строке

        if type_button == "edit":
            if self.ui_main_window.productstable_button.isEnabled():
                index_name = self.ui_main_window.management_table.model().index(number_row, 1)

                # Извлечение текста из ячеек
                self.create_edit_anime.ui_create_edit_anime.name_textedit.setText(index_name.data())

                current_name = index_name.data()  #Запоминание текста из ячеек

                self.create_edit_anime.show()

                press_edit = True
                self.update_create_edit_anime(press_edit, current_name)
            else:
                # Получение индекса
                index_name = self.ui_main_window.management_table.model().index(number_row, 1)
                index_anime = self.ui_main_window.management_table.model().index(number_row, 2)
                index_price = self.ui_main_window.management_table.model().index(number_row, 3)
                index_count = self.ui_main_window.management_table.model().index(number_row, 4)

                # Извлечение текста из ячеек
                self.create_edit_product.ui_create_edit_product.name_textedit.setText(index_name.data())
                self.create_edit_product.ui_create_edit_product.anime_textedit.setText(index_anime.data())
                self.create_edit_product.ui_create_edit_product.price_textedit.setText(index_price.data())
                self.create_edit_product.ui_create_edit_product.count_textedit.setText(index_count.data())

                current_name = index_name.data() #Запоминание текста из ячеек
                current_anime = index_anime.data()
                current_price = index_price.data()
                current_count = index_count.data()

                self.create_edit_product.show()

                press_edit = True
                self.update_create_edit_product(press_edit, current_name, current_anime, current_price,
                                                current_count)
        else:
            if self.ui_main_window.productstable_button.isEnabled():
                index_name = self.ui_main_window.management_table.model().index(number_row, 1)

                anime_name = index_name.data()
                delete_anime_by_name(anime_name)

                # Загрузка данных из базы данных
                load_data_from_db(self.anime_model, 'anime_table')
                self.anime_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Действие'])
                self.add_delegate_managment(self.anime_model, self.ui_main_window.management_table, 2)
            else:
                index_name = self.ui_main_window.management_table.model().index(number_row, 1)
                index_anime = self.ui_main_window.management_table.model().index(number_row, 2)
                index_price = self.ui_main_window.management_table.model().index(number_row, 3)
                index_count = self.ui_main_window.management_table.model().index(number_row, 4)

                # Извлечение текста из ячеек
                name = index_name.data()
                anime = index_anime.data()
                price = index_price.data()
                count = index_count.data()
                delete_product(name, anime, price, count)

                load_data_from_db(self.product_model, 'product_table')
                self.product_model.setHorizontalHeaderLabels(
                    ['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Действие'])
                self.add_delegate_managment(self.product_model, self.ui_main_window.management_table, 5)

    def closeEvent(self, event):
        save_database()
        event.accept()

class CreateEditProduct(QtWidgets.QWidget):
    def __init__(self, main_window, product_model, add_delegate):
        super(CreateEditProduct, self).__init__()
        self.ui_create_edit_product = Ui_CreateEditProduct_form()
        self.ui_create_edit_product.setupUi(self)

        self.product_model = product_model
        self.main_window = main_window
        self.add_delegate = add_delegate

        self.press_edit = False
        self.current_name = None
        self.current_anime = None
        self.current_price = None
        self.current_count = None

        self.ui_create_edit_product.ok_button.clicked.connect(self.save_product) # Кнопка подтверждения
        self.ui_create_edit_product.cancel_button.clicked.connect(self.close_create_edit_product) # Кнопка отмены

    def save_product(self):
        name = self.ui_create_edit_product.name_textedit.toPlainText().strip()  # Наименование
        anime = self.ui_create_edit_product.anime_textedit.toPlainText().strip()  # Аниме
        price = self.ui_create_edit_product.price_textedit.toPlainText().strip()  # Цена
        count = self.ui_create_edit_product.count_textedit.toPlainText().strip()  # Количество

        def is_valid_input(value):
            # Проверка, что строка состоит только из букв и цифр
            return bool(re.match(r'^[\w\s]+$', value))  # \w соответствует буквам и цифрам, \s соответствует пробелам

        def is_valid_number(number):
            # Проверка, что count состоит только из цифр
            return number.isdigit()

        if self.press_edit:
            # Проверка входных данных
            input_valid = (
                    is_valid_input(name) and
                    is_valid_input(anime) and
                    is_valid_number(price) and
                    is_valid_number(count)
            )

            if not input_valid:
                # Очистка полей, если входные данные недействительны
                if not is_valid_number(price):
                    self.ui_create_edit_product.price_textedit.setText(self.current_price) # Ввод текущей цены
                if not is_valid_number(count):
                    self.ui_create_edit_product.count_textedit.setText(self.current_count)
                if not is_valid_input(anime):
                    self.ui_create_edit_product.anime_textedit.setText(self.current_anime)
                if not is_valid_input(name):
                    self.ui_create_edit_product.name_textedit.setText(self.current_name)
                return

            # Если входные данные валидны, обновляем продукт
            if update_product(self.current_name, self.current_anime, self.current_price, self.current_count, name,
                              anime, price, count):
                self.close()
                self.press_edit = False

        else:
            print('New')
            # Проверка входных данных и добавление новой записи
            if not is_valid_input(name) or not is_valid_input(anime) or not is_valid_number(price) or not is_valid_number(
                    count) or not add_to_database_product(name, anime, price, count):
                # Очистка полей и уведомление пользователя об ошибке
                if not is_valid_input(name):
                    self.ui_create_edit_product.name_textedit.clear()
                if not is_valid_number(price):
                    self.ui_create_edit_product.price_textedit.clear()  # Очистка поля цены
                if not is_valid_number(count):
                    self.ui_create_edit_product.count_textedit.clear()  # Очистка поля количества
                if not is_valid_input(anime) or not add_to_database_product(name, anime, price, count):
                    self.ui_create_edit_product.anime_textedit.clear()  # Очистка поля аниме
                return

        self.clear_text()# Очистка полей

        # Загрузка данных из базы данных
        load_data_from_db(self.product_model, 'product_table')
        self.product_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Действие'])
        self.add_delegate(self.product_model, self.main_window.management_table, 5)

    def close_create_edit_product(self):
        self.clear_text()
        self.close()

    def clear_text(self):
        self.ui_create_edit_product.name_textedit.clear()
        self.ui_create_edit_product.anime_textedit.clear()
        self.ui_create_edit_product.price_textedit.clear()
        self.ui_create_edit_product.count_textedit.clear()


class CreateEditAnime(QtWidgets.QWidget):
    def __init__(self, main_window, anime_model, add_delegate):
        super(CreateEditAnime, self).__init__()
        self.ui_create_edit_anime = Ui_CreateEditAnime_form()
        self.ui_create_edit_anime.setupUi(self)

        self.main_window = main_window
        self.anime_model = anime_model
        self.add_delegate = add_delegate

        self.press_edit = False
        self.current_name = None

        self.ui_create_edit_anime.ok_button.clicked.connect(self.save_anime) # Кнопка подтверждения
        self.ui_create_edit_anime.cancel_button.clicked.connect(self.close_create_edit_anime) # Кнопка отмены

    def save_anime(self):
        name = self.ui_create_edit_anime.name_textedit.toPlainText().strip()  # Наименование

        def is_valid_input(value):
            # Проверка, что строка состоит только из букв и цифр
            return bool(re.match(r'^[\w\s]+$', value))

        # Проверка входных данных
        if not is_valid_input(name) :
            self.ui_create_edit_anime.name_textedit.clear()
            return

        if self.press_edit:
            update_anime(self.current_name, name)
            self.close()
            self.press_edit = False
        else:
            add_to_database_anime(name) # Добавление новой записи

        self.ui_create_edit_anime.name_textedit.clear()   # Очистка поля

        # Загрузка данных из базы данных
        load_data_from_db(self.anime_model, 'anime_table')
        self.anime_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Действие'])
        self.add_delegate(self.anime_model, self.main_window.management_table, 2)

    def close_create_edit_anime(self):
        self.ui_create_edit_anime.name_textedit.clear() # Очистка поля
        self.close()

class Preview(QtWidgets.QWidget):
    def __init__(self):
        super(Preview, self).__init__()
        self.ui_preview =  Ui_preview_form()
        self.ui_preview.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()


    preview = Preview()

    sys.exit(app.exec())
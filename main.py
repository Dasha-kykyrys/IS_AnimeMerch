from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
import sys
from GUI import Ui_MainWindow, Ui_CreateEditAnime_form, Ui_CreateEditProduct_form, Ui_preview_form, ItemDelegateData, ItemDelegateCheck
from database import load_data_from_db, add_to_database_product,  add_to_database_anime, delete_anime_by_name, delete_product

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
        self.ui_main_window.creat_button.clicked.connect(self.open_create_edit)

        self.catalog_model = QStandardItemModel(0, 4, self)
        load_data_from_db(self.catalog_model, 'product_table')
        self.catalog_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во'])
        self.ui_main_window.catalog_table.setModel(self.catalog_model)

        self.check_model = QStandardItemModel(0, 3, self)
        self.check_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Кол-во'])
        self.ui_main_window.chek_table.setModel(self.check_model)

        self.sale_model = QStandardItemModel(0, 5, self)

        self.product_model = QStandardItemModel(0, 5, self)

        self.anime_model = QStandardItemModel(0, 2, self)


    def change_widget(self, index):
        if index == 0:
            self.ui_main_window.catalog_button.setEnabled(False)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(True)

        if index == 1:
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(False)
            self.ui_main_window.management_button.setEnabled(True)

            self.sale_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Дата'])

            self.ui_main_window.sales_table.setModel(self.sale_model)

        if index == 2:
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

    def open_product_table(self):
        self.ui_main_window.print_button.show()
        self.ui_main_window.animetable_button.setEnabled(True)
        self.ui_main_window.productstable_button.setEnabled(False)

        load_data_from_db(self.product_model, 'product_table')
        self.product_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Действие'])
        self.ui_main_window.management_table.setModel(self.product_model)
        self.add_delegate_managment(self.product_model, self.ui_main_window.management_table, 5)

    def open_create_edit(self):
        if self.ui_main_window.productstable_button.isEnabled():
            create_edit_anime.setWindowModality(Qt.ApplicationModal)
            create_edit_anime.show()
        else:
            create_edit_product.setWindowModality(Qt.ApplicationModal)
            create_edit_product.show()

    def open_preview(self):
        preview.setWindowModality(Qt.ApplicationModal)
        preview.show()

    def add_delegate_managment(self, model, table, number):
        for row in range(model.rowCount()):
            item = model.item(row, 1)  # Получаем элемент, который будет отображаться

            if item is not None:  # Убедитесь, что item существует
                item_delegate = ItemDelegateData(item.text(), row)  # Создаем экземпляр ItemDelegateData
                table.setIndexWidget(model.index(row, number), item_delegate)  # Устанавливаем делегат в таблицу

                # Подключаем сигнал нажатия кнопки удаления к обработчику
                item_delegate.delete_requested.connect(lambda r=row: self.handle_delete_request(row))

    def handle_delete_request(self, row):
        is_product = not self.ui_main_window.productstable_button.isChecked()  # Проверяем состояние кнопки в момент вызова

        if is_product:
            # Получаем данные о продукте из модели на основе номера строки
            product_name = self.product_model.item(row, 1).text()
            anime_name = self.product_model.item(row, 2).text()
            product_price = self.product_model.item(row, 3).text()
            product_count = self.product_model.item(row, 4).text()

            delete_product(product_name, anime_name, product_price, product_count)
            load_data_from_db(self.product_model, 'product_table')
            self.add_delegate_managment(self.product_model, self.ui_main_window.management_table, 5)

        else:
            anime_name = self.anime_model.item(row, 1).text()
            delete_anime_by_name(anime_name)
            load_data_from_db(self.anime_model, 'anime_table')
            self.add_delegate_managment(self.anime_model, self.ui_main_window.management_table, 2)


class CreateEditProduct(QtWidgets.QWidget):
    def __init__(self, main_window, product_model, add_delegate):
        super(CreateEditProduct, self).__init__()
        self.ui_create_edit_product = Ui_CreateEditProduct_form()
        self.ui_create_edit_product.setupUi(self)

        self.product_model = product_model
        self.main_window = main_window
        self.add_delegate = add_delegate


        self.ui_create_edit_product.ok_button.clicked.connect(self.save_product)
        self.ui_create_edit_product.cancel_button.clicked.connect(self.close_create_edit_product)

    def save_product(self):
        name = self.ui_create_edit_product.name_textedit.toPlainText().strip()  # Наименование
        anime = self.ui_create_edit_product.anime_textedit.toPlainText().strip()  # Аниме
        price = self.ui_create_edit_product.price_textedit.toPlainText().strip()  # Цена
        count = self.ui_create_edit_product.count_textedit.toPlainText().strip()  # Количество

        if not price.replace('.', '', 1).isdigit() or not count.isdigit() or not add_to_database_product(name, anime, price, count):
            # Очистка полей и уведомление пользователя об ошибке
            if not price.replace('.', '', 1).isdigit():
                self.ui_create_edit_product.price_textedit.clear()  # Очистка поля цены
            if not count.isdigit():
                self.ui_create_edit_product.count_textedit.clear()  # Очистка поля количества
            if not add_to_database_product(name, anime, price, count):
                self.ui_create_edit_product.anime_textedit.clear()  # Очистка поля аниме
            return

        # Очистка полей
        self.ui_create_edit_product.name_textedit.clear()
        self.ui_create_edit_product.anime_textedit.clear()
        self.ui_create_edit_product.price_textedit.clear()
        self.ui_create_edit_product.count_textedit.clear()

        # Загрузка данных из базы данных
        load_data_from_db(self.product_model, 'product_table')
        self.product_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Действие'])
        self.add_delegate(self.product_model, self.main_window.ui_main_window.management_table, 5)

    def close_create_edit_product(self):
        self.ui_create_edit_product.name_textedit.clear()
        self.ui_create_edit_product.anime_textedit.clear()
        self.ui_create_edit_product.price_textedit.clear()
        self.ui_create_edit_product.count_textedit.clear()
        self.close()


class CreateEditAnime(QtWidgets.QWidget):
    def __init__(self, main_window, anime_model, add_delegate):
        super(CreateEditAnime, self).__init__()
        self.ui_create_edit_anime = Ui_CreateEditAnime_form()
        self.ui_create_edit_anime.setupUi(self)

        self.main_window = main_window
        self.anime_model = anime_model
        self.add_delegate = add_delegate

        self.ui_create_edit_anime.ok_button.clicked.connect(self.save_anime)
        self.ui_create_edit_anime.cancel_button.clicked.connect(self.close_create_edit_anime)

    def save_anime(self):
        name = self.ui_create_edit_anime.name_textedit.toPlainText().strip()  # Наименование

        add_to_database_anime(name)

        # Очистка полей
        self.ui_create_edit_anime.name_textedit.clear()

        # Загрузка данных из базы данных
        load_data_from_db(self.anime_model, 'anime_table')
        self.anime_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Действие'])
        self.add_delegate(self.anime_model, self.main_window.ui_main_window.management_table, 2)

    def close_create_edit_anime(self):
        self.ui_create_edit_anime.name_textedit.clear()
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

    create_edit_product = CreateEditProduct(application, application.product_model, application.add_delegate_managment)
    create_edit_anime = CreateEditAnime(application, application.anime_model, application.add_delegate_managment)  # Передаем main_window
    preview = Preview()

    sys.exit(app.exec())
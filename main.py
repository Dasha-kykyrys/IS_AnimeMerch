from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
import sys
from GUI import Ui_MainWindow, Ui_CreateEditAnime_form, Ui_CreateEditProduct_form, Ui_preview_form, ItemDelegateData, ItemDelegateCheck
from database import load_data_from_db, add_to_database

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
        self.catalog_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во'])
        load_data_from_db(self.catalog_model, 'product_table')
        self.ui_main_window.catalog_table.setModel(self.catalog_model)

        self.check_model = QStandardItemModel(0, 3, self)
        self.check_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Кол-во'])
        self.ui_main_window.chek_table.setModel(self.check_model)
        self.add_delegate(self.check_model, self.ui_main_window.chek_table, ItemDelegateCheck, 3)


    def change_widget(self, index):
        if index == 0:
            self.ui_main_window.catalog_button.setEnabled(False)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(True)

        if index == 1:
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(False)
            self.ui_main_window.management_button.setEnabled(True)

            self.sale_model = QStandardItemModel(0, 5, self)
            self.sale_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Дата'])

            self.ui_main_window.sales_table.setModel(self.sale_model)

        if index == 2:
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(False)

            self.product_model = QStandardItemModel(0, 5, self)
            self.product_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Аниме', 'Цена', 'Кол-во', 'Действие'])

            load_data_from_db(self.product_model, 'product_table')

            self.ui_main_window.management_table.setModel(self.product_model)

            self.add_delegate(self.product_model, self.ui_main_window.management_table, ItemDelegateData, 5)

        self.ui_main_window.stacked_widget.setCurrentIndex(index)

    def open_anime_table(self):
        self.ui_main_window.print_button.hide()
        self.ui_main_window.productstable_button.setEnabled(True)
        self.ui_main_window.animetable_button.setEnabled(False)

        self.anime_model = QStandardItemModel(0, 2, self)
        self.anime_model.setHorizontalHeaderLabels(['№', 'Наименование', 'Действие'])

        load_data_from_db(self.anime_model, 'anime_table')

        self.ui_main_window.management_table.setModel(self.anime_model)
        self.add_delegate(self.anime_model,self.ui_main_window.management_table, ItemDelegateData, 2)

    def open_product_table(self):
        self.ui_main_window.print_button.show()
        self.ui_main_window.animetable_button.setEnabled(True)
        self.ui_main_window.productstable_button.setEnabled(False)

        self.ui_main_window.management_table.setModel(self.product_model)
        self.add_delegate(self.product_model, self.ui_main_window.management_table, ItemDelegateData, 5)

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

    def add_delegate(self, model, table, delegate, number):
        for row in range(model.rowCount()):
            item = model.item(row, 1)
            item.setData(delegate(item.text()), Qt.UserRole)
            # Присвоение делегатов для каждой строки в таблице
            table.setIndexWidget(model.index(row, number), delegate(model.item(row, 0).text()))

class CreateEditProduct(QtWidgets.QWidget):
    def __init__(self):
        super(CreateEditProduct, self).__init__()
        self.ui_create_edit_product = Ui_CreateEditProduct_form()
        self.ui_create_edit_product.setupUi(self)

        self.ui_create_edit_product.ok_button.clicked.connect(self.save_product)
        self.ui_create_edit_product.cancel_button.clicked.connect(self.close_create_edit_product)

    def save_product(self):
        add_to_database(self.ui_create_edit_product.name_label,self.ui_create_edit_product.anime_lable,self.ui_create_edit_product.price_lable, self.ui_create_edit_product.count_label)

    def close_create_edit_product(self):
        create_edit_product.close()

class CreateEditAnime(QtWidgets.QWidget):
    def __init__(self):
        super(CreateEditAnime, self).__init__()
        self.ui_create_edit_anime = Ui_CreateEditAnime_form()
        self.ui_create_edit_anime.setupUi(self)

class Preview(QtWidgets.QWidget):
    def __init__(self):
        super(Preview, self).__init__()
        self.ui_preview =  Ui_preview_form()
        self.ui_preview.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    create_edit_product = CreateEditProduct()
    create_edit_anime = CreateEditAnime()
    preview = Preview()

    sys.exit(app.exec())
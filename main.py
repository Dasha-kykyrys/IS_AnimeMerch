from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from GUI import Ui_MainWindow, Ui_CreateEditAnime_form, Ui_CreateEditProduct_form, Ui_preview_form # импорт интерфейса
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main_window = Ui_MainWindow()
        self.ui_main_window.setupUi(self)

        self.ui_main_window.catalog_button.clicked.connect(lambda: self.change_widget(0))
        self.ui_main_window.sales_button.clicked.connect(lambda: self.change_widget(1))
        self.ui_main_window.management_button.clicked.connect(lambda: self.change_widget(2))

        self.ui_main_window.print_sales_button.clicked.connect(self.open_preview)      

        self.ui_main_window.animetable_button.clicked.connect(self.open_anime_table)
        self.ui_main_window.productstable_button.clicked.connect(self.open_product_table)
        self.ui_main_window.print_button.clicked.connect(self.open_preview)
        self.ui_main_window.creat_button.clicked.connect(self.open_create_edit_product)

    def change_widget(self, index):
        if index == 0:
            self.ui_main_window.catalog_button.setEnabled(False)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(True)
        if index == 1:
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(False)
            self.ui_main_window.management_button.setEnabled(True)
        if index == 2:
            self.ui_main_window.catalog_button.setEnabled(True)
            self.ui_main_window.sales_button.setEnabled(True)
            self.ui_main_window.management_button.setEnabled(False)

        self.ui_main_window.stacked_widget.setCurrentIndex(index)

    def open_anime_table(self):
        self.ui_main_window.print_button.hide()
        self.ui_main_window.productstable_button.setEnabled(True)
        self.ui_main_window.animetable_button.setEnabled(False)

    def open_product_table(self):
        self.ui_main_window.print_button.show()
        self.ui_main_window.animetable_button.setEnabled(True)
        self.ui_main_window.productstable_button.setEnabled(False)

    def open_create_edit_product(self):
        create_edit_product.setWindowModality(Qt.ApplicationModal)
        create_edit_product.show()

    def open_preview(self):
        preview.setWindowModality(Qt.ApplicationModal)
        preview.show()

class CreateEditProduct(QtWidgets.QWidget):
    def __init__(self):
        super(CreateEditProduct, self).__init__()
        self.ui_create_edit_product = Ui_CreateEditProduct_form()
        self.ui_create_edit_product.setupUi(self)

        self.ui_create_edit_product.cancel_button.clicked.connect(self.close_create_edit_product)

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
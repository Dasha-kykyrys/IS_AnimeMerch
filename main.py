from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from GUI import Ui_MainWindow, Ui_CreateEditAnime_form, Ui_CreateEditProduct_form, Ui_preview_form # импорт интерфейса
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.catalog_button.clicked.connect(lambda: self.change_widget(0))
        self.ui.sales_button.clicked.connect(lambda: self.change_widget(1))
        self.ui.management_button.clicked.connect(lambda: self.change_widget(2))
        self.ui.creat_button.clicked.connect(self.open_create_edit_product)

    def change_widget(self, index):
        if index == 0:
            self.ui.catalog_button.setEnabled(False)
            self.ui.sales_button.setEnabled(True)
            self.ui.management_button.setEnabled(True)
        if index == 1:
            self.ui.catalog_button.setEnabled(True)
            self.ui.sales_button.setEnabled(False)
            self.ui.management_button.setEnabled(True)
        if index == 2:
            self.ui.catalog_button.setEnabled(True)
            self.ui.sales_button.setEnabled(True)
            self.ui.management_button.setEnabled(False)

        self.ui.stacked_widget.setCurrentIndex(index)

    def open_create_edit_product(self):
        create_edit_product.setWindowModality(Qt.ApplicationModal)
        create_edit_product.show()  # Open the dialog and freeze the main window


class CreateEditProduct(QtWidgets.QWidget):
    def __init__(self):
        super(CreateEditProduct, self).__init__()
        self.ui = Ui_CreateEditProduct_form()
        self.ui.setupUi(self)

class CreateEditAnime(QtWidgets.QWidget):
    def __init__(self):
        super(CreateEditAnime, self).__init__()
        self.ui = Ui_CreateEditAnime_form()
        self.ui.setupUi(self)

class Preview(QtWidgets.QWidget):
    def __init__(self):
        super(Preview, self).__init__()
        self.ui =  Ui_preview_form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    create_edit_product = CreateEditProduct()
    create_edit_anime = CreateEditAnime()


    sys.exit(app.exec())
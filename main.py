from PyQt5 import QtWidgets
from GUI import Ui_MainWindow  # импорт интерфейса
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.catalog_button.clicked.connect(lambda: self.change_widget(0))
        self.ui.sales_button.clicked.connect(lambda: self.change_widget(1))
        self.ui.management_button.clicked.connect(lambda: self.change_widget(2))

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


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
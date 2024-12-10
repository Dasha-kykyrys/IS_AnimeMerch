# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'management.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1311, 858)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgba(255, 234, 210, 1);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: 2px solid #6E491E;\n"
"    background:  #E7C49C;\n"
"       height: 20px;\n"
"    margin: 0px 20px 0 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #7F5525;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 2px solid #6E491E;\n"
"   background:  #E7C49C;\n"
"    width: 20px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"    border: 2px solid #6E491E;\n"
"   background:  #E7C49C;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-image: url(:/image/scrollbar_left.png);\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal  {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-image: url(:/image/scrollbar_right.png);\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: 2px solid #6E491E;\n"
"    background:  #E7C49C;\n"
"    width: 20px;\n"
"    margin: 20px 0px 20 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #7F5525;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    border: 2px solid #6E491E;\n"
"   background:  #E7C49C;\n"
"    height:  20px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    border: 2px solid #6E491E;\n"
"   background:  #E7C49C;\n"
"    height: 20px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-image: url(:/image/scrollbar_up.png);\n"
"}\n"
"\n"
"QScrollBar::down-arrow:vertical  {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    border-image: url(:/image/scrollbar_down.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralwidget_layout.setContentsMargins(0, 0, 0, -1)
        self.centralwidget_layout.setObjectName("centralwidget_layout")

        self.centralwidget_layout.addLayout(self.work_area_layout, 2, 0, 1, 1)
        self.tabs = QtWidgets.QFrame(self.centralwidget)
        self.tabs.setStyleSheet("background-color: #7F5525;")
        self.tabs.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tabs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabs.setObjectName("tabs")
        self.tabs_layout = QtWidgets.QHBoxLayout(self.tabs)
        self.tabs_layout.setContentsMargins(30, 27, 30, 0)
        self.tabs_layout.setSpacing(22)
        self.tabs_layout.setObjectName("tabs_layout")
        self.catalog_button = QtWidgets.QPushButton(self.tabs)
        self.catalog_button.setEnabled(False)
        self.catalog_button.setMinimumSize(QtCore.QSize(192, 55))
        self.catalog_button.setToolTip("")
        self.catalog_button.setAutoFillBackground(False)
        self.catalog_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/catalog_button.png);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    border-image: url(:/image/catalog_pressbutton.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/image/catalog_hoverbutton.png);\n"
"}")
        self.catalog_button.setText("")
        self.catalog_button.setObjectName("catalog_button")
        self.tabs_layout.addWidget(self.catalog_button)
        self.sales_button = QtWidgets.QPushButton(self.tabs)
        self.sales_button.setMinimumSize(QtCore.QSize(192, 55))
        self.sales_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/sales_button.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/image/sales_hoverbutton.png);\n"
"}")
        self.sales_button.setText("")
        self.sales_button.setObjectName("sales_button")
        self.tabs_layout.addWidget(self.sales_button)
        self.management_button = QtWidgets.QPushButton(self.tabs)
        self.management_button.setEnabled(True)
        self.management_button.setMinimumSize(QtCore.QSize(192, 55))
        self.management_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/managment_button.png);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    border-image: url(:/image/managment_pressbutton.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/image/managment_hoverbutton.png);\n"
"}")
        self.management_button.setText("")
        self.management_button.setObjectName("management_button")
        self.tabs_layout.addWidget(self.management_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tabs_layout.addItem(spacerItem1)
        self.centralwidget_layout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.productstable_button.setToolTip(_translate("MainWindow", "Таблица товаров"))
        self.animetable_button.setToolTip(_translate("MainWindow", "Таблица аниме"))
        self.creat_button.setToolTip(_translate("MainWindow", "Добавить"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
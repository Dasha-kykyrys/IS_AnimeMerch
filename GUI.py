from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QStackedWidget, QWidget
import images_rc

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1311, 858)
        MainWindow.setWindowTitle("АнимеТорговля")
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


        # Кнопки перехода по страницам
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
"QPushButton:disabled{\n"
	" border-image: url(:/image/sales_pressbutton.png);\n"
"}\n"
                                      
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.tabs_layout.addItem(spacerItem2)
        self.centralwidget_layout.addWidget(self.tabs, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # создание стека со всеми страницами
        self.stacked_widget = QStackedWidget()
        self.centralwidget_layout.addWidget(self.stacked_widget)

        self.stacked_widget.addWidget(self.catalog_page())
        self.stacked_widget.addWidget(self.sales_page())
        self.stacked_widget.addWidget(self.management_page())


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def catalog_page(self):
        page = QWidget()
        self.work_area_layout = QtWidgets.QHBoxLayout()
        self.work_area_layout.setContentsMargins(30, -1, 30, -1)
        self.work_area_layout.setSpacing(7)
        self.work_area_layout.setObjectName("work_area_layout")

        # таблица каталога и поиск
        self.catalog_layout = QtWidgets.QVBoxLayout()
        self.catalog_layout.setContentsMargins(-1, 12, -1, 12)
        self.catalog_layout.setSpacing(23)
        self.catalog_layout.setObjectName("catalog_layout")

        self.catalog_label = QtWidgets.QLabel(self.centralwidget)
        self.catalog_label.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.catalog_label.setFont(font)
        self.catalog_label.setStyleSheet("color: #6E491E;")
        self.catalog_label.setObjectName("catalog_label")
        self.catalog_layout.addWidget(self.catalog_label)
        self.catalog_table = QtWidgets.QTableView(self.centralwidget)
        self.catalog_table.setStyleSheet("QTableView {\n"
                                             "    border:none;\n"
                                             "    border-top:2px solid #6E491E; \n"
                                             "      border-left: 2px solid #6E491E; \n"
                                             "    border-radius: 5px;\n"
                                             "    gridline-color: #6E491E; \n"
                                             "    color: #563916;    \n"
                                             "    font: 14pt \"Times New Roman\";\n"
                                             "  }\n"
                                             "\n"
                                             "QTableView::item {\n"
                                             "    border-bottom:1px solid #6E491E; \n"
                                             "      border-left: 0.4px solid #6E491E; \n"
                                             "    border-right: 0.5px solid #6E491E; \n"
                                             "}\n"
                                             " \n"
                                             "QTableView::item:selected {\n"
                                             "    background-color: rgb(218, 218, 218);\n"
                                             " }\n"
                                             "\n"
                                             "QHeaderView::section {\n"
                                             "    border: none;\n"
                                             "     border-bottom: 2px solid #6E491E; \n"
                                             "      border-left: 0.4px solid #6E491E; \n"
                                             "    border-right: 2px solid #6E491E; ; \n"
                                             "    background-color: #E7C49C; \n"
                                             "    color: #563916;\n"
                                             "    font: 14pt \"Times New Roman\";\n"
                                             "    padding: 3px;\n"
                                             "}\n"
                                             "\n"
                                             "QHeaderView::down-arrow {\n"
                                             "    width: 26px; \n"
                                             "    height:18px; \n"
                                             "    subcontrol-position: bottom right; \n"
                                             "}\n"
                                             "")
        self.catalog_table.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.catalog_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.catalog_table.setLineWidth(0)
        self.catalog_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.catalog_table.setTabKeyNavigation(False)
        self.catalog_table.setProperty("showDropIndicator", False)
        self.catalog_table.setDragDropOverwriteMode(False)
        self.catalog_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.catalog_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.catalog_table.setSortingEnabled(True)
        self.catalog_table.setObjectName("catalog_table")
        self.catalog_table.horizontalHeader().setCascadingSectionResizes(False)
        self.catalog_table.horizontalHeader().setHighlightSections(False)
        self.catalog_table.horizontalHeader().setSortIndicatorShown(True)
        self.catalog_table.horizontalHeader().setStretchLastSection(True)
        self.catalog_table.verticalHeader().setVisible(False)
        self.catalog_table.verticalHeader().setStretchLastSection(True)

        self.catalog_layout.addWidget(self.catalog_table)

        self.search_layout = QtWidgets.QHBoxLayout()
        self.search_layout.setObjectName("search_layout")
        self.search_field = QtWidgets.QTextEdit(self.centralwidget)
        self.search_field.setMinimumSize(QtCore.QSize(416, 53))
        self.search_field.setMaximumSize(QtCore.QSize(16777215, 53))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.search_field.setFont(font)
        self.search_field.setStyleSheet("QTextEdit{\n"
                                            "    border: 2px solid #6E491E;\n"
                                            "    color: #563916;\n"
                                            "    font: 18pt \"Times New Roman\";\n"
                                            "}")
        self.search_field.setObjectName("search_field")
        self.search_layout.addWidget(self.search_field)
        self.find_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_button.setMinimumSize(QtCore.QSize(155, 53))
        self.find_button.setMaximumSize(QtCore.QSize(155, 53))
        self.find_button.setToolTip("")
        self.find_button.setWhatsThis("")
        self.find_button.setStyleSheet("QPushButton{\n"
                                           "    border-image: url(:/image/find_button.png);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    border-image: url(:/image/find_pressbutton.png);\n"
                                           "}\n"
                                           "")
        self.find_button.setText("")
        self.find_button.setObjectName("find_button")
        self.search_layout.addWidget(self.find_button)
        self.catalog_layout.addLayout(self.search_layout)

        self.work_area_layout.addLayout(self.catalog_layout)

        # Кнопки добавления удаления товаров из чека
        self.filling_layout = QtWidgets.QVBoxLayout()
        self.filling_layout.setContentsMargins(20, -1, 20, -1)
        self.filling_layout.setSpacing(50)
        self.filling_layout.setObjectName("filling_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.filling_layout.addItem(spacerItem)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMinimumSize(QtCore.QSize(59, 53))
        self.add_button.setStyleSheet("QPushButton{\n"
                                          "    border-image: url(:/image/add_button.png);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    border-image: url(:/image/add_pressbutton.png);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:disabled {\n"
                                          "    border-image: url(:/image/add_disablebutton.png);\n"
                                          "}")
        self.add_button.setText("")
        self.add_button.setObjectName("add_button")
        self.filling_layout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_button.sizePolicy().hasHeightForWidth())
        self.remove_button.setSizePolicy(sizePolicy)
        self.remove_button.setMinimumSize(QtCore.QSize(59, 53))
        self.remove_button.setStyleSheet("QPushButton{\n"
                                             "    border-image: url(:/image/remove_button.png);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    border-image: url(:/image/remove_pressbutton.png);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:disabled {\n"
                                             "    border-image: url(:/image/remove_disablebutton.png);\n"
                                             "}")
        self.remove_button.setText("")
        self.remove_button.setObjectName("remove_button")
        self.filling_layout.addWidget(self.remove_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.filling_layout.addItem(spacerItem1)

        self.work_area_layout.addLayout(self.filling_layout)

        # таблица чека
        self.check_layout = QtWidgets.QVBoxLayout()
        self.check_layout.setContentsMargins(-1, 12, -1, 12)
        self.check_layout.setSpacing(23)
        self.check_layout.setObjectName("check_layout")
        self.chek_label = QtWidgets.QLabel(self.centralwidget)
        self.chek_label.setMinimumSize(QtCore.QSize(101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.chek_label.setFont(font)
        self.chek_label.setStyleSheet("color: #6E491E;")
        self.chek_label.setObjectName("chek_label")
        self.check_layout.addWidget(self.chek_label)
        self.chek_table = QtWidgets.QTableView(self.centralwidget)
        self.chek_table.setStyleSheet("QTableView {\n"
                                          "    border:none;\n"
                                          "    border-top:2px solid #6E491E; \n"
                                          "      border-left: 2px solid #6E491E; \n"
                                          "    border-radius: 5px;\n"
                                          "    gridline-color: #6E491E; \n"
                                          "    color: #563916;    \n"
                                          "    font: 14pt \"Times New Roman\";\n"
                                          "  }\n"
                                          "\n"
                                          "QTableView::item {\n"
                                          "    border-bottom:1px solid #6E491E; \n"
                                          "      border-left: 0.4px solid #6E491E; \n"
                                          "    border-right: 0.5px solid #6E491E; \n"
                                          "}\n"
                                          " \n"
                                          "QTableView::item:selected {\n"
                                          "    background-color: rgb(218, 218, 218);\n"
                                          " }\n"
                                          "\n"
                                          "QHeaderView::section {\n"
                                          "    border: none;\n"
                                          "     border-bottom: 2px solid #6E491E; \n"
                                          "      border-left: 0.4px solid #6E491E; \n"
                                          "    border-right: 2px solid #6E491E; ; \n"
                                          "    background-color: #E7C49C; \n"
                                          "    color: #563916;\n"
                                          "    font: 14pt \"Times New Roman\";\n"
                                          "    padding: 3px;\n"
                                          "}\n"
                                          "\n"
                                          "QHeaderView::down-arrow {\n"
                                          "    width: 26px; \n"
                                          "    height:18px; \n"
                                          "    subcontrol-position: bottom right; \n"
                                          "}\n"
                                          "")
        self.chek_table.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.chek_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chek_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.chek_table.setTabKeyNavigation(False)
        self.chek_table.setProperty("showDropIndicator", False)
        self.chek_table.setDragDropOverwriteMode(False)
        self.chek_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.chek_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.chek_table.setSortingEnabled(True)
        self.chek_table.setObjectName("chek_table")
        self.chek_table.horizontalHeader().setCascadingSectionResizes(False)
        self.chek_table.horizontalHeader().setHighlightSections(False)
        self.chek_table.horizontalHeader().setSortIndicatorShown(True)
        self.chek_table.horizontalHeader().setStretchLastSection(True)
        self.chek_table.verticalHeader().setVisible(False)
        self.chek_table.verticalHeader().setCascadingSectionResizes(False)
        self.chek_table.verticalHeader().setStretchLastSection(True)
        self.check_layout.addWidget(self.chek_table)
        self.result_layout = QtWidgets.QHBoxLayout()
        self.result_layout.setObjectName("result_layout")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setMinimumSize(QtCore.QSize(101, 37))
        self.result_label.setMaximumSize(QtCore.QSize(101, 37))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setStyleSheet("color: #6E491E;")
        self.result_label.setObjectName("result_label")
        self.result_layout.addWidget(self.result_label)
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setMinimumSize(QtCore.QSize(146, 37))
        self.total_label.setMaximumSize(QtCore.QSize(16777215, 37))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.total_label.setFont(font)
        self.total_label.setStyleSheet("color: #C66B00;")
        self.total_label.setObjectName("total_label")
        self.result_layout.addWidget(self.total_label)
        self.confirm_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_button.setEnabled(False)
        self.confirm_button.setMinimumSize(QtCore.QSize(195, 53))
        self.confirm_button.setMaximumSize(QtCore.QSize(195, 53))
        self.confirm_button.setStyleSheet("QPushButton{\n"
                                              "    border-image: url(:/image/confirm_button.png);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    border-image: url(:/image/confirm_pressbutton.png);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:disabled {\n"
                                              "    border-image: url(:/image/confirm_disablebutton.png);\n"
                                              "}")
        self.confirm_button.setText("")
        self.confirm_button.setObjectName("confirm_button")
        self.result_layout.addWidget(self.confirm_button)
        self.check_layout.addLayout(self.result_layout)

        self.work_area_layout.addLayout(self.check_layout)


        self.catalog_label.setText("Каталог")
        self.add_button.setToolTip("Добавить товар")
        self.remove_button.setToolTip("Убрать товар")
        self.chek_label.setText("Чек")
        self.result_label.setText("Итого:")
        self.confirm_button.setToolTip("Создать чек")

        page.setLayout(self.work_area_layout)

        return page

    def sales_page(self):
        page = QWidget()
        self.work_area_layout = QtWidgets.QVBoxLayout()
        self.work_area_layout.setContentsMargins(30, 30, 30, 30)
        self.work_area_layout.setSpacing(20)
        self.work_area_layout.setObjectName("work_area_layout")
        self.header_layout = QtWidgets.QHBoxLayout()
        self.header_layout.setContentsMargins(-1, -1, -1, 0)
        self.header_layout.setSpacing(13)
        self.header_layout.setObjectName("header_layout")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setStyleSheet("color: #6E491E;")
        self.header_label.setObjectName("header_label")
        self.header_layout.addWidget(self.header_label)
        self.begin_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.begin_dateEdit.setMinimumSize(QtCore.QSize(139, 43))
        self.begin_dateEdit.setStyleSheet("QDateEdit {\n"
                                          "    font: 75 14pt \"Times New Roman\";\n"
                                          "    color: #6E491E;\n"
                                          "    border: 2px solid #6E491E;\n"
                                          "    padding-left : 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QDateEdit::drop-down {\n"
                                          "    subcontrol-origin: margin;\n"
                                          "    margin-right: 5px;\n"
                                          "    subcontrol-position: right center;\n"
                                          "       width: 10px;\n"
                                          "    height: 10px;\n"
                                          "    border-image: url(:/image/scrollbar_down.png);\n"
                                          "\n"
                                          "}")
        self.begin_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.begin_dateEdit.setCalendarPopup(True)
        self.begin_dateEdit.setObjectName("begin_dateEdit")
        self.header_layout.addWidget(self.begin_dateEdit)
        self.header_label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.header_label2.setFont(font)
        self.header_label2.setStyleSheet("color: #6E491E;")
        self.header_label2.setObjectName("header_label2")
        self.header_layout.addWidget(self.header_label2)
        self.end_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.end_dateEdit.setMinimumSize(QtCore.QSize(139, 43))
        self.end_dateEdit.setStyleSheet("QDateEdit {\n"
                                        "    font: 75 14pt \"Times New Roman\";\n"
                                        "    color: #6E491E;\n"
                                        "    border: 2px solid #6E491E;\n"
                                        "    padding-left : 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QDateEdit::drop-down {\n"
                                        "    subcontrol-origin: margin;\n"
                                        "    margin-right: 5px;\n"
                                        "    subcontrol-position: right center;\n"
                                        "       width: 10px;\n"
                                        "    height: 10px;\n"
                                        "    border-image: url(:/image/scrollbar_down.png);\n"
                                        "}")
        self.end_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.end_dateEdit.setCalendarPopup(True)
        self.end_dateEdit.setObjectName("end_dateEdit")
        self.header_layout.addWidget(self.end_dateEdit)
        self.confirmdate_button = QtWidgets.QPushButton(self.centralwidget)
        self.confirmdate_button.setEnabled(True)
        self.confirmdate_button.setMinimumSize(QtCore.QSize(50, 43))
        self.confirmdate_button.setStyleSheet("QPushButton{\n"
                                              "    border-image: url(:/image/confirmdate_button.png);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    border-image: url(:/image/confirmdate_pressbutton.png);\n"
                                              "}")
        self.confirmdate_button.setText("")
        self.confirmdate_button.setObjectName("confirmdate_button")
        self.header_layout.addWidget(self.confirmdate_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header_layout.addItem(spacerItem)
        self.print_sales_button = QtWidgets.QPushButton(self.centralwidget)
        self.print_sales_button.setEnabled(True)
        self.print_sales_button.setMinimumSize(QtCore.QSize(195, 53))
        self.print_sales_button.setStyleSheet("QPushButton{\n"
                                              "    border-image: url(:/image/print_button.png);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    border-image: url(:/image/print_pressbutton.png);\n"
                                              "}")
        self.print_sales_button.setText("")
        self.print_sales_button.setObjectName("print_sales_button")
        self.header_layout.addWidget(self.print_sales_button)
        self.work_area_layout.addLayout(self.header_layout)
        self.sales_table = QtWidgets.QTableView(self.centralwidget)
        self.sales_table.setStyleSheet("QTableView {\n"
                                       "    border:none;\n"
                                       "    border-top:2px solid #6E491E; \n"
                                       "      border-left: 2px solid #6E491E; \n"
                                       "    border-radius: 5px;\n"
                                       "    gridline-color: #6E491E; \n"
                                       "    color: #563916;    \n"
                                       "    font: 14pt \"Times New Roman\";\n"
                                       "  }\n"
                                       "\n"
                                       "QTableView::item {\n"
                                       "    border-bottom:1px solid #6E491E; \n"
                                       "      border-left: 0.4px solid #6E491E; \n"
                                       "    border-right: 0.5px solid #6E491E; \n"
                                       "}\n"
                                       " \n"
                                       "QTableView::item:selected {\n"
                                       "    background-color: rgb(218, 218, 218);\n"
                                       " }\n"
                                       "\n"
                                       "QHeaderView::section {\n"
                                       "    border: none;\n"
                                       "     border-bottom: 2px solid #6E491E; \n"
                                       "      border-left: 0.4px solid #6E491E; \n"
                                       "    border-right: 2px solid #6E491E; ; \n"
                                       "    background-color: #E7C49C; \n"
                                       "    color: #563916;\n"
                                       "    font: 14pt \"Times New Roman\";\n"
                                       "    padding: 3px;\n"
                                       "}\n"
                                       "\n"
                                       "QHeaderView::down-arrow {\n"
                                       "    width: 26px; \n"
                                       "    height:18px; \n"
                                       "    subcontrol-position: bottom right; \n"
                                       "}\n"
                                       "")
        self.sales_table.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.sales_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sales_table.setLineWidth(0)
        self.sales_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_table.setTabKeyNavigation(False)
        self.sales_table.setProperty("showDropIndicator", False)
        self.sales_table.setDragDropOverwriteMode(False)
        self.sales_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sales_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sales_table.setSortingEnabled(True)
        self.sales_table.setObjectName("sales_table")
        self.sales_table.horizontalHeader().setCascadingSectionResizes(False)
        self.sales_table.horizontalHeader().setHighlightSections(False)
        self.sales_table.horizontalHeader().setSortIndicatorShown(True)
        self.sales_table.horizontalHeader().setStretchLastSection(True)
        self.sales_table.verticalHeader().setVisible(False)
        self.sales_table.verticalHeader().setStretchLastSection(True)
        self.work_area_layout.addWidget(self.sales_table)

        self.header_label.setText("с")
        self.header_label2.setText("по")
        self.confirmdate_button.setToolTip("Отфильтровать")

        page.setLayout(self.work_area_layout)
        return page

    def management_page(self):
            page = QWidget()
            self.work_area_layout = QtWidgets.QVBoxLayout()
            self.work_area_layout.setContentsMargins(30, 28, 30, 30)
            self.work_area_layout.setSpacing(15)
            self.work_area_layout.setObjectName("work_area_layout")
            self.header_layout = QtWidgets.QHBoxLayout()
            self.header_layout.setObjectName("header_layout")
            self.productstable_button = QtWidgets.QPushButton(self.centralwidget)
            self.productstable_button.setEnabled(False)
            self.productstable_button.setMinimumSize(QtCore.QSize(145, 53))
            self.productstable_button.setStyleSheet("QPushButton{\n"
                                                    "    border-image: url(:/image/productstable_button.png);\n"
                                                    "}\n"
                                                    "\n"
                                                    "QPushButton:disabled {\n"
                                                    "    border-image: url(:/image/productstable_pressbutton.png);\n"
                                                    "}")
            self.productstable_button.setText("")
            self.productstable_button.setObjectName("productstable_button")
            self.header_layout.addWidget(self.productstable_button)
            self.animetable_button = QtWidgets.QPushButton(self.centralwidget)
            self.animetable_button.setEnabled(True)
            self.animetable_button.setMinimumSize(QtCore.QSize(145, 53))
            self.animetable_button.setStyleSheet("QPushButton{\n"
                                                 "    border-image: url(:/image/animetable_button.png);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:disabled {\n"
                                                 "    border-image: url(:/image/animetable_pressbutton.png);\n"
                                                 "}")
            self.animetable_button.setText("")
            self.animetable_button.setObjectName("animetable_button")
            self.header_layout.addWidget(self.animetable_button)
            spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.header_layout.addItem(spacerItem)
            self.print_button = QtWidgets.QPushButton(self.centralwidget)
            self.print_button.setMinimumSize(QtCore.QSize(195, 53))
            self.print_button.setStyleSheet("QPushButton{\n"
                                                  "    border-image: url(:/image/print_button.png);\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed {\n"
                                                  "    border-image: url(:/image/print_pressbutton.png);\n"
                                                  "}")
            self.print_button.setText("")
            self.print_button.setObjectName("print_button")
            self.header_layout.addWidget(self.print_button)
            self.creat_button = QtWidgets.QPushButton(self.centralwidget)
            self.creat_button.setMinimumSize(QtCore.QSize(60, 60))
            self.creat_button.setStyleSheet("QPushButton{\n"
                                            "    border-image: url(:/image/creat_button.png);\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "    border-image: url(:/image/creat_pressbutton.png);\n"
                                            "}")
            self.creat_button.setText("")
            self.creat_button.setObjectName("creat_button")
            self.header_layout.addWidget(self.creat_button)
            self.work_area_layout.addLayout(self.header_layout)
            self.management_table = QtWidgets.QTableView(self.centralwidget)
            self.management_table.setStyleSheet("QTableView {\n"
                                                "    border:none;\n"
                                                "    border-top:2px solid #6E491E; \n"
                                                "      border-left: 2px solid #6E491E; \n"
                                                "    border-radius: 5px;\n"
                                                "    gridline-color: #6E491E; \n"
                                                "    color: #563916;    \n"
                                                "    font: 14pt \"Times New Roman\";\n"
                                                "  }\n"
                                                "\n"
                                                "QTableView::item {\n"
                                                "    border-bottom:1px solid #6E491E; \n"
                                                "      border-left: 0.4px solid #6E491E; \n"
                                                "    border-right: 0.5px solid #6E491E; \n"
                                                "}\n"
                                                " \n"
                                                "QTableView::item:selected {\n"
                                                "    background-color: rgb(218, 218, 218);\n"
                                                " }\n"
                                                "\n"
                                                "QHeaderView::section {\n"
                                                "    border: none;\n"
                                                "     border-bottom: 2px solid #6E491E; \n"
                                                "      border-left: 0.4px solid #6E491E; \n"
                                                "    border-right: 2px solid #6E491E; ; \n"
                                                "    background-color: #E7C49C; \n"
                                                "    color: #563916;\n"
                                                "    font: 14pt \"Times New Roman\";\n"
                                                "    padding: 3px;\n"
                                                "}\n"
                                                "\n"
                                                "QHeaderView::down-arrow {\n"
                                                "    width: 26px; \n"
                                                "    height:18px; \n"
                                                "    subcontrol-position: bottom right; \n"
                                                "}\n"
                                                "")
            self.management_table.setFrameShape(QtWidgets.QFrame.WinPanel)
            self.management_table.setFrameShadow(QtWidgets.QFrame.Plain)
            self.management_table.setLineWidth(0)
            self.management_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.management_table.setTabKeyNavigation(False)
            self.management_table.setProperty("showDropIndicator", False)
            self.management_table.setDragDropOverwriteMode(False)
            self.management_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.management_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.management_table.setSortingEnabled(True)
            self.management_table.setObjectName("management_table")
            self.management_table.horizontalHeader().setCascadingSectionResizes(False)
            self.management_table.horizontalHeader().setHighlightSections(False)
            self.management_table.horizontalHeader().setSortIndicatorShown(True)
            self.management_table.horizontalHeader().setStretchLastSection(True)
            self.management_table.verticalHeader().setVisible(False)
            self.management_table.verticalHeader().setStretchLastSection(True)
            self.work_area_layout.addWidget(self.management_table)

            self.productstable_button.setToolTip("Таблица товаров")
            self.animetable_button.setToolTip("Таблица аниме")
            self.creat_button.setToolTip("Добавить")

            page.setLayout(self.work_area_layout)
            return page

class RowButton(QtWidgets.QPushButton):
    def __init__(self, row_number, *args, **kwargs):
        super(RowButton, self).__init__(*args, **kwargs)
        self.row_number = row_number

    def get_row_number(self):
        return self.row_number

class ItemDelegateCheck(QWidget):
    button_clicked = QtCore.pyqtSignal(str, int)  # Создаем сигнал для передачи типа кнопки и номера строки

    def __init__(self, row_number, parent=None):
        super(ItemDelegateCheck, self).__init__(parent)

        self.row_number = row_number  # Номер строки

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.addCount_button = RowButton(row_number, self.horizontalLayoutWidget)
        self.addCount_button.setMinimumSize(QtCore.QSize(32, 32))
        self.addCount_button.setMaximumSize(QtCore.QSize(32, 32))
        self.addCount_button.setStyleSheet("QPushButton{\n"
                                           "    color: #6E491E;\n"
                                           "    border: none;\n"
                                           "    font: 75 20pt \"Times New Roman\";\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    color: #B57F3E;\n"
                                           "}\n"
                                           )
        self.addCount_button.setObjectName("addCount_button")
        self.addCount_button.setText("+")
        self.addCount_button.clicked.connect(lambda: self.on_button_clicked("add", row_number))  # Передаем тип кнопки
        self.horizontalLayout.addWidget(self.addCount_button)

        self.count_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.count_label.setStyleSheet("color: #6E491E;\n"
                                       "font: 75 14pt \"Times New Roman\";\n"
                                       )
        self.count_label.setObjectName("count_label")
        self.count_label.setText("1")
        self.horizontalLayout.addWidget(self.count_label)

        self.delCount_button = RowButton(row_number, self.horizontalLayoutWidget)
        self.delCount_button.setMinimumSize(QtCore.QSize(32, 32))
        self.delCount_button.setMaximumSize(QtCore.QSize(32, 32))
        self.delCount_button.setStyleSheet("QPushButton{\n"
                                           "    color: #6E491E;\n"
                                           "    border: none;\n"
                                           "    font: 75 20pt \"Times New Roman\";\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed {\n"
                                           "    color: #B57F3E;\n"
                                           "}\n"
                                           )
        self.delCount_button.setObjectName("delCount_button")
        self.delCount_button.setText("–")
        self.delCount_button.clicked.connect(lambda: self.on_button_clicked("delete", row_number))  # Передаем тип кнопки
        self.horizontalLayout.addWidget(self.delCount_button)

        # Установка компоновки для виджета
        self.setLayout(self.horizontalLayout)

    def on_button_clicked(self, button_type, row_number):
        self.button_clicked.emit(button_type, row_number)

    def update_count_label(self, count):
        self.count_label.setText(str(count))

    def get_count(self):
        return int(self.count_label.text())

class ItemDelegateData(QWidget):
    button_clicked = QtCore.pyqtSignal(str, int)  # Создаем сигнал для передачи типа кнопки и номера строки

    def __init__(self, row_number, parent=None):
        super(ItemDelegateData, self).__init__(parent)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.edit_button = RowButton(row_number, self.horizontalLayoutWidget)
        self.edit_button.setMinimumSize(QtCore.QSize(32, 32))
        self.edit_button.setMaximumSize(QtCore.QSize(32, 32))
        self.edit_button.setStyleSheet("QPushButton{\n"
                                        "  border-image: url(:/image/edit_button.png);\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "  border-image: url(:/image/edit_pressbutton.png);\n"
                                        "}\n"
                                        )
        self.edit_button.setObjectName("edit_button")
        self.edit_button.clicked.connect(lambda: self.on_button_clicked("edit", row_number))  # Передаем тип кнопки
        self.horizontalLayout.addWidget(self.edit_button)

        self.delet_button = RowButton(row_number, self.horizontalLayoutWidget)
        self.delet_button.setMinimumSize(QtCore.QSize(32, 32))
        self.delet_button.setMaximumSize(QtCore.QSize(32, 32))
        self.delet_button.setStyleSheet("QPushButton{\n"
                                         "  border-image: url(:/image/delet_button.png);\n"
                                         "}\n"
                                         "QPushButton:pressed {\n"
                                         "  border-image: url(:/image/delet_pressbutton.png);\n"
                                         "}\n"
                                        )
        self.delet_button.setObjectName("delet_button")
        self.delet_button.clicked.connect(lambda: self.on_button_clicked("delete", row_number))  # Передаем тип кнопки
        self.horizontalLayout.addWidget(self.delet_button)

        # Установка компоновки для виджета
        self.setLayout(self.horizontalLayout)

    def on_button_clicked(self, button_type, row_number):
        self.button_clicked.emit(button_type, row_number)

class Ui_CreateEditAnime_form(object):
    def setupUi(self, CreateEditAnime_form):
        CreateEditAnime_form.setObjectName("CreateEditAnime_form")
        CreateEditAnime_form.resize(657, 348)
        CreateEditAnime_form.setMinimumSize(QtCore.QSize(657, 348))
        CreateEditAnime_form.setMaximumSize(QtCore.QSize(657, 348))
        CreateEditAnime_form.setWindowTitle("")
        CreateEditAnime_form.setStyleSheet("QWidget {\n"
"background-color: #FFEAD2;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CreateEditAnime_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, 20, 20, 10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(CreateEditAnime_form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.name_textedit = QtWidgets.QLineEdit(CreateEditAnime_form)
        self.name_textedit.setMinimumSize(QtCore.QSize(0, 53))
        self.name_textedit.setMaximumSize(QtCore.QSize(16777215, 53))
        self.name_textedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid #6E491E;\n"
"    color: #563916;\n"
"    font: 18pt \"Times New Roman\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.name_textedit.setObjectName("name_textedit")
        self.verticalLayout.addWidget(self.name_textedit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(CreateEditAnime_form)
        self.cancel_button.setMinimumSize(QtCore.QSize(172, 42))
        self.cancel_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/cancel_button.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/image/cancel_pressbutton.png);\n"
"}\n"
"")
        self.cancel_button.setText("")
        self.cancel_button.setObjectName("cancel_button")
        self.buttons_layout.addWidget(self.cancel_button)
        self.ok_button = QtWidgets.QPushButton(CreateEditAnime_form)
        self.ok_button.setMinimumSize(QtCore.QSize(172, 42))
        self.ok_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/ok_button.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/image/ok_pressbutton.png);\n"
"}\n"
"")
        self.ok_button.setText("")
        self.ok_button.setObjectName("ok_button")
        self.buttons_layout.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.buttons_layout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        QtCore.QMetaObject.connectSlotsByName(CreateEditAnime_form)

        self.name_label.setText("Наименование")

class Ui_CreateEditProduct_form(object):
    def setupUi(self, CreateEditProduct_form):
        CreateEditProduct_form.setObjectName("CreateEditProduct_form")
        CreateEditProduct_form.resize(657, 525)
        CreateEditProduct_form.setMinimumSize(QtCore.QSize(657, 525))
        CreateEditProduct_form.setMaximumSize(QtCore.QSize(657, 525))
        CreateEditProduct_form.setWindowTitle("")
        CreateEditProduct_form.setStyleSheet("QWidget {\n"
"background-color: #FFEAD2;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(CreateEditProduct_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.work_area_layout = QtWidgets.QVBoxLayout()
        self.work_area_layout.setContentsMargins(20, 15, 20, 10)
        self.work_area_layout.setSpacing(20)
        self.work_area_layout.setObjectName("work_area_layout")
        self.name_label = QtWidgets.QLabel(CreateEditProduct_form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.work_area_layout.addWidget(self.name_label)
        self.name_textedit = QtWidgets.QLineEdit(CreateEditProduct_form)
        self.name_textedit.setMinimumSize(QtCore.QSize(0, 53))
        self.name_textedit.setMaximumSize(QtCore.QSize(16777215, 53))
        self.name_textedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid #6E491E;\n"
"    color: #563916;\n"
"    font: 18pt \"Times New Roman\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.name_textedit.setObjectName("name_textedit")
        self.work_area_layout.addWidget(self.name_textedit)
        self.anime_lable = QtWidgets.QLabel(CreateEditProduct_form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.anime_lable.setFont(font)
        self.anime_lable.setObjectName("anime_lable")
        self.work_area_layout.addWidget(self.anime_lable)
        self.anime_textedit = QtWidgets.QLineEdit(CreateEditProduct_form)
        self.anime_textedit.setMinimumSize(QtCore.QSize(0, 53))
        self.anime_textedit.setMaximumSize(QtCore.QSize(16777215, 53))
        self.anime_textedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid #6E491E;\n"
"    color: #563916;\n"
"    font: 18pt \"Times New Roman\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.anime_textedit.setObjectName("anime_textedit")
        self.work_area_layout.addWidget(self.anime_textedit)
        self.wa_horizontal_layout = QtWidgets.QHBoxLayout()
        self.wa_horizontal_layout.setContentsMargins(-1, 14, -1, -1)
        self.wa_horizontal_layout.setSpacing(30)
        self.wa_horizontal_layout.setObjectName("wa_horizontal_layout")
        self.price_layout = QtWidgets.QVBoxLayout()
        self.price_layout.setSpacing(10)
        self.price_layout.setObjectName("price_layout")
        self.price_lable = QtWidgets.QLabel(CreateEditProduct_form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.price_lable.setFont(font)
        self.price_lable.setObjectName("price_lable")
        self.price_layout.addWidget(self.price_lable)
        self.price_textedit = QtWidgets.QLineEdit(CreateEditProduct_form)
        self.price_textedit.setMinimumSize(QtCore.QSize(266, 53))
        self.price_textedit.setMaximumSize(QtCore.QSize(16777215, 53))
        self.price_textedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid #6E491E;\n"
"    color: #563916;\n"
"    font: 18pt \"Times New Roman\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.price_textedit.setObjectName("price_textedit")
        self.price_layout.addWidget(self.price_textedit)
        self.wa_horizontal_layout.addLayout(self.price_layout)
        self.count_layout = QtWidgets.QVBoxLayout()
        self.count_layout.setSpacing(10)
        self.count_layout.setObjectName("count_layout")
        self.count_label = QtWidgets.QLabel(CreateEditProduct_form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.count_label.setFont(font)
        self.count_label.setObjectName("count_label")
        self.count_layout.addWidget(self.count_label)
        self.count_textedit = QtWidgets.QLineEdit(CreateEditProduct_form)
        self.count_textedit.setMinimumSize(QtCore.QSize(266, 53))
        self.count_textedit.setMaximumSize(QtCore.QSize(16777215, 53))
        self.count_textedit.setStyleSheet("QLineEdit{\n"
"    border: 2px solid #6E491E;\n"
"    color: #563916;\n"
"    font: 18pt \"Times New Roman\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.count_textedit.setObjectName("count_textedit")
        self.count_layout.addWidget(self.count_textedit)
        self.wa_horizontal_layout.addLayout(self.count_layout)
        self.work_area_layout.addLayout(self.wa_horizontal_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.work_area_layout.addItem(spacerItem)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem1)
        self.cancel_button = QtWidgets.QPushButton(CreateEditProduct_form)
        self.cancel_button.setMinimumSize(QtCore.QSize(172, 42))
        self.cancel_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/cancel_button.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/image/cancel_pressbutton.png);\n"
"}\n")
        self.cancel_button.setText("")
        self.cancel_button.setObjectName("cancel_button")
        self.buttons_layout.addWidget(self.cancel_button)
        self.ok_button = QtWidgets.QPushButton(CreateEditProduct_form)
        self.ok_button.setMinimumSize(QtCore.QSize(172, 42))
        self.ok_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/ok_button.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/image/ok_pressbutton.png);\n"
"}\n")
        self.ok_button.setText("")
        self.ok_button.setObjectName("ok_button")
        self.buttons_layout.addWidget(self.ok_button)
        self.work_area_layout.addLayout(self.buttons_layout)
        self.verticalLayout_2.addLayout(self.work_area_layout)

        QtCore.QMetaObject.connectSlotsByName(CreateEditProduct_form)

        self.name_label.setText("Наименование")
        self.anime_lable.setText("Аниме")
        self.price_lable.setText("Цена")
        self.count_label.setText("Количество")

class Ui_preview_form(object):
    def setupUi(self, preview_form):
        preview_form.setObjectName("preview_form")
        preview_form.resize(657, 348)
        preview_form.setMinimumSize(QtCore.QSize(657, 348))

        preview_form.setWindowTitle("")
        preview_form.setStyleSheet("QWidget {\n"
"background-color: #FFEAD2;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(preview_form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.work_area_layout = QtWidgets.QVBoxLayout()
        self.work_area_layout.setContentsMargins(20, 20, 20, 10)
        self.work_area_layout.setSpacing(20)
        self.work_area_layout.setObjectName("work_area_layout")

        self.viewer = QtWebEngineWidgets.QWebEngineView()
        self.viewer.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.viewer.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem)
        self.sendtoprint_button = QtWidgets.QPushButton(preview_form)
        self.sendtoprint_button.setMinimumSize(QtCore.QSize(172, 42))
        self.sendtoprint_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/sendtoprint_button.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/image/sendtoprint_pressbutton.png);\n"
"}\n")
        self.sendtoprint_button.setText("")
        self.sendtoprint_button.setObjectName("sendtoprint_button")
        self.buttons_layout.addWidget(self.sendtoprint_button)
        self.save_button = QtWidgets.QPushButton(preview_form)
        self.save_button.setMinimumSize(QtCore.QSize(172, 42))
        self.save_button.setStyleSheet("QPushButton{\n"
"    border-image: url(:/image/save_button.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/image/save_pressbutton.png);\n"
"}\n")
        self.save_button.setText("")
        self.save_button.setObjectName("save_button")
        self.buttons_layout.addWidget(self.save_button)

        self.work_area_layout.addWidget(self.viewer)
        self.work_area_layout.addLayout(self.buttons_layout)
        self.verticalLayout_2.addLayout(self.work_area_layout)

        QtCore.QMetaObject.connectSlotsByName(preview_form)



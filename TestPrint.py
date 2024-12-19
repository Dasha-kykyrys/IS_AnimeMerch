from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtPrintSupport, QtWebEngineWidgets


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.viewer = QtWebEngineWidgets.QWebEngineView(self)
        self.viewer.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.viewer.settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)

        self.buttonOpen = QtWidgets.QPushButton('Open', self)
        self.buttonOpen.clicked.connect(self.handleOpen)
        self.buttonPrint = QtWidgets.QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QtWidgets.QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.viewer, 0, 0, 1, 3)
        layout.addWidget(self.buttonOpen, 1, 0)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.printer = Printer(self.viewer.page(), self)

    def handleOpen(self):
        if path := QtWidgets.QFileDialog.getOpenFileName(self)[0]:
            self.viewer.load(QtCore.QUrl.fromLocalFile(path))

    def handlePrint(self):
        if self.viewer.url().isValid():
            self.printer.print()

    def handlePreview(self):
        if self.viewer.url().isValid():
            self.printer.preview()


class Printer(QtCore.QObject):
    def __init__(self, page, parent=None):
        super().__init__(parent)
        self._page = page
        self._printing = False

    def render(self, printer):
        loop = QtCore.QEventLoop()
        failed = False
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        def callback(result):
            nonlocal failed
            failed = not result
            QtWidgets.QApplication.restoreOverrideCursor()
            loop.quit()
        self._page.print(printer, callback)
        loop.exec()
        if failed:
            painter = QtGui.QPainter()
            if painter.begin(printer):
                font = painter.font()
                font.setPixelSize(20)
                painter.setFont(font)
                painter.drawText(QtCore.QPointF(10, 25),
                    'Could not generate print preview')
                painter.end()

    def preview(self):
        if not self._printing:
            self._printing = True
            printer = QtPrintSupport.QPrinter()
            printer.setResolution(300)
            dialog = QtPrintSupport.QPrintPreviewDialog(
                printer, self._page.view())
            dialog.paintRequested.connect(self.render)
            dialog.exec()
            dialog.deleteLater()
            self._printing = False

    def print(self):
        printer = QtPrintSupport.QPrinter(
            QtPrintSupport.QPrinter.HighResolution)
        dialog = QtPrintSupport.QPrintDialog(printer, self._page.view())
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            self.render(printer)
        dialog.deleteLater()


if __name__ == '__main__':

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(['Printing Demo'])
    window = Window()
    window.setGeometry(600, 100, 800, 600)
    window.show()
    app.exec()
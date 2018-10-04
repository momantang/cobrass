import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)
        self.status = self.statusBar()
        self.status.showMessage('this is status bar', 5000)
        self.setWindowTitle('MainWindows demo')


        layout=QHBoxLayout()
        layout

        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/cartoon1.ico'))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

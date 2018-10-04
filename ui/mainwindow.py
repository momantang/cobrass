import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('cobrass 智能量化实验室')
        self.init_menu()

    def init_menu(self):
        self.menu = self.menuBar()
        self.menu.setNativeMenuBar(False)
        file_menu = self.menu.addMenu('&文件')
        tool_menu = self.menu.addMenu('&工具')
        about_menu = self.menu.addMenu('&关于')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    app.exec_()

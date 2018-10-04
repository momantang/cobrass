from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys


class lineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont('Arial', 20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        flo = QFormLayout()
        flo.addRow('integer validator', e1)
        flo.addRow('double validator', e2)

        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')
        flo.addRow('Input Mask', e3)

        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)
        flo.addRow('text change', e4)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        flo.addRow('Password', e5)

        e6 = QLineEdit('Hello PyQt5')
        e6.setReadOnly(True)
        flo.addRow('Read only', e6)

        e5.editingFinished.connect(self.enterPress)
        self.setLayout(flo)
        self.setWindowTitle('qline edit')

    def textchanged(self, text):
        print('input content is ' + text)

    def enterPress(self):
        print('input finish')


if __name__ == '__main__':
    ap = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(ap.exec_())

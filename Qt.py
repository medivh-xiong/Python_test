import sys
import random
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtQuick import QQuickView

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("霸王茶姬")

        self.tokenLabel = QtWidgets.QLabel("token:")
        self.tokenEdit = QtWidgets.QLineEdit("输入token")
        self.pushButton = QtWidgets.QPushButton("添加")

        layout = QtWidgets.lay
        layout.addWidget(self.tokenLabel)
        layout.addWidget(self.tokenEdit)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

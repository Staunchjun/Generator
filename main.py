import sys

from PyQt5 import QtWidgets

from input_data import Ui_MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
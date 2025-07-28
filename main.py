import sys
from controlador.main_controlador import MainController
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
import time

from window.basic import LoginWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
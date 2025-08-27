import sys
from PyQt6.QtWidgets import QApplication, QDialog 
from PyQt6 import uic

class testWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('0821_test.ui', self)
        self.buttonBox.clicked.connect(self.click_btn)

    def click_btn(self):
        print('클릭')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = testWindow()
    window.show()
    sys.exit(app.exec())
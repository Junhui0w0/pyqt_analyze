from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLabel
from PyQt6.QtGui import QPixmap

import ui.ui_mainhomeForm

class mainhomepage(QMainWindow, ui.ui_mainhomeForm.Ui_MainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.setupUi(self)
        self.login_window = login_window

        # #- 기본 프로필 설정
        # basic_profile = QPixmap('img/profile.png')
        # self.lbl_profile.setPixmap(basic_profile)

        # self.lbl_profile.clicked.connect(self.change_profile)


    def change_profile(self):
        print('change profile')

        ch_profile = QPixmap('img/bg_black.png')
        self.lbl_profile.setPixmap(ch_profile)
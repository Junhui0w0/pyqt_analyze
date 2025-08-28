from PyQt6.QtWidgets import QMainWindow, QMessageBox, QLabel
from PyQt6.QtGui import QPixmap

import ui.ui_mainhomeForm

class mainhomepage(QMainWindow, ui.ui_mainhomeForm.Ui_MainWindow):
    def __init__(self, user_id, login_window):

        #1. 상속
        super().__init__()
        self.setupUi(self)
        self.login_window = login_window

        #2. player_id 변경
        self.lbl_playerid.setText(user_id)

        #3. 기능 연결
        self.lbl_profile.clicked.connect(self.func_change_profile)
        self.btn_logout.clicked.connect(self.func_logout)


    def func_change_profile(self):
        print('change profile')

        ch_profile = QPixmap('0826/img/bg_black.png')
        self.lbl_profile.setPixmap(ch_profile)

    def func_logout(self):
        print('logout')
        self.hide()
        self.login_window.show()
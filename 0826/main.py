from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
import time

from ui_loginForm import loginForm
from ui_registerForm import registerForm
from MongoDB_userinfo import Basic_Login, Basic_Register

class LoginWindow(QMainWindow, loginForm):
    def __init__(self):

        #1. 상속 작업
        super().__init__()
        self.setupUi(self)
        
        #2. 버튼 - 함수 연결 작업
        self.btn_basic_login.clicked.connect(self.func_btn_click_basicLogin)
        self.btn_google_login.clicked.connect(self.func_btn_click_googleLogin)

        #3. 인스턴스 변수 생성
        self.register_window = None

    def func_btn_click_basicLogin(self):
        user_id = self.txt_id.toPlainText()
        user_pw = self.txt_pw.toPlainText()

        print(f'입력 ID: {user_id} , PW: {user_pw} - Basic_Login으로 데이터 전송 중...')
        # time.sleep(1)

        ret_basic_login = Basic_Login(user_id, user_pw)

        if ret_basic_login == 'Do Register?': #회원가입 하실?
            question_register_box = QMessageBox()
            question_register_box.setWindowTitle('DO REGISTER?')
            question_register_box.setText('사용자가 입력한 ID 정보가 없습니다.')

            register_btn = question_register_box.addButton("회원가입", QMessageBox.ButtonRole.AcceptRole)
            login_btn = question_register_box.addButton("로그인", QMessageBox.ButtonRole.AcceptRole)

            question_register_box.exec()

            if question_register_box.clickedButton() == register_btn:
                print('회원가입 수행 - 회원가입 Form 출력')

                self.register_window = RegisterWindow(self)
                self.register_window.show() #회원가입 창 출력

                self.hide() #현재 window 숨기기

                return True
            
            elif question_register_box.clickedButton() == login_btn:
                print('재 로그인 수행 - 로그인 Form 재 출력')
                self.txt_id.setText('')
                self.txt_pw.setText('')
                return True
            
        elif ret_basic_login == 'Success To Login':
            print('[debug] 로그인 성공')

    def func_btn_click_googleLogin(self):
        print(f'Google 계정으로 로그인 수행')

class RegisterWindow(QMainWindow, registerForm):
    def __init__(self, login_window):
        super().__init__()
        self.setupUi(self)
        self.login_window = login_window

        self.btn_register.clicked.connect(self.func_btn_click_register)

    def func_btn_click_register(self):
        user_id = self.edit_id.text()
        user_pw = self.edit_pw.text()

        ret_basic_register = Basic_Register(user_id, user_pw)
        if ret_basic_register == 'length error':
            print(f'[debug] {user_id} 의 아이디 길이 부적합')
            self.edit_id.setText('')
            self.edit_pw.setText('')

        elif ret_basic_register == 'alphabet or num only included':
            print(f'[debug] 영문자 또는 숫자만 포함되어야 함')
            self.edit_id.setText('')
            self.edit_pw.setText('')

        elif ret_basic_register == 'db connect error':
            print(f'[debug] mongodb 연결 오류')
            self.edit_id.setText('')
            self.edit_pw.setText('')

        elif ret_basic_register == 'success to login':
            print(f'[debug] 회원가입 성공')
            
            self.login_window.show()
            self.hide()


        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
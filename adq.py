import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel
#
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# ||||||||||||||||||||||||||||||||||||||||||||||
# ? ?????? ????? ???? ??????? ??????????? ? ??????
#

class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 100, 300, 100)
        self.setWindowTitle('??????? ?????')

        self.btn = QPushButton('?????', self)
        self.btn.resize(100, 50)
        self.btn.move(50, 25)

        self.btn1 = QPushButton('????', self)
        self.btn1.resize(100, 50)
        self.btn1.move(150, 25)
        #
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
        # ||||||||||||||||||||||||||||||||||||||||||||||
        # ? ?????? ????? ???? ?? ??????? ?????? ????? ? ????
        # ? ?????? ?????? ??? ??????
        #

        self.btn.clicked.connect(self.open_second_form)
        self.btn1.clicked.connect(self.open_second_form1)

    def open_second_form(self):
        self.second_form = SecondForm(self, "?????? ??? ?????? ?????")
        self.second_form.show()

    def open_second_form1(self):
        self.second_form1 = SecondForm1(self, "?????? ??? ?????? ?????")
        self.second_form1.show()

class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('?????? ?????')
        print(webbrowser.open("ttt.py"))

class SecondForm1(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)


    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('?????? ?????1')
        print(os.startfile(r"C:\Users\BARCA\Desktop\??????\data\my_calendar.py"))
#
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# ||||||||||||||||||||||||||||||||||||||||||||||
# ? ?????? ????? ???? ?? ??????? ??????
# ??? ??????? ????? pyqt5
#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())


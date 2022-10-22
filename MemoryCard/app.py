from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
import sys


app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 400)
window.setWindowTitle('Memo Card')

btn_ok = QPushButton('Ответить')
lbl_question = QLabel('Вопрос?')
grpbox_answers = QGroupBox('Варианты ответов')
radio_group = QButtonGroup()
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

def show_question():
    grpbox_answers.show()
    grpbox_result.hide()
    btn_ok.setText('Ответить')
    btn_ok.clicked.connect(show_result)
    radio_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True)

def show_result():
    grpbox_answers.hide()
    grpbox_result.show()
    btn_ok.setText('Следующий вопрос')
    btn_ok.clicked.connect(show_question)

btn_ok.clicked.connect(show_result)

grpbox_result = QGroupBox('Результат теста')
lbl_right_answer = QLabel('Правильный ответ: 2313')
v_line_result = QVBoxLayout()

v_line_result.addWidget(lbl_right_answer, alignment=Qt.AlignCenter)
grpbox_result.setLayout(v_line_result)

h_line_ans = QHBoxLayout()
v_line_ans_1 = QVBoxLayout()
v_line_ans_2 = QVBoxLayout()

v_line_ans_1.addWidget(rbtn_1)
v_line_ans_1.addWidget(rbtn_2)
v_line_ans_2.addWidget(rbtn_3)
v_line_ans_2.addWidget(rbtn_4)
h_line_ans.addLayout(v_line_ans_1)
h_line_ans.addLayout(v_line_ans_2)

grpbox_answers.setLayout(h_line_ans)

v_line_main = QVBoxLayout()
h_line_main_1 = QHBoxLayout()
h_line_main_2 = QHBoxLayout()
h_line_main_3 = QHBoxLayout()

h_line_main_1.addWidget(lbl_question, alignment=Qt.AlignCenter)
h_line_main_2.addWidget(grpbox_answers)
h_line_main_2.addWidget(grpbox_result)
h_line_main_3.addStretch(1)
h_line_main_3.addWidget(btn_ok, stretch=2)
h_line_main_3.addStretch(1)

v_line_main.addLayout(h_line_main_1, stretch=2)
v_line_main.addLayout(h_line_main_2, stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line_main_3, stretch=1)
v_line_main.addStretch(1)

#
grpbox_result.hide()
#

window.setLayout(v_line_main)

window.show()
app.exec()

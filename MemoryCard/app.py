from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
import sys
from random import shuffle


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
    check_answer()
    grpbox_answers.hide()
    grpbox_result.show()
    btn_ok.setText('Следующий вопрос')
    btn_ok.clicked.connect(show_question)


btn_ok.setStyleSheet('''
background-color: #1F3641;
color: #F0F0F0;
border-radius: 5%;
padding: 10% 3% 10% 3%;
''')

window.setStyleSheet('''
    font-size: 16px;
''')

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

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = [
    Question('Вопрос №1', 'правильный', 'неправильный', 'неправильный', 'правильный'),
    Question('Вопрос №2', '1', '2', '4', '1024'),
    Question('Вопрос №3', '12', '21321321', '21321312', '12321312')
]

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q):
    lbl_question.setText(q.question)
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

def check_answer():
    if answers[0].isChecked():
        lbl_right_answer.setText('Поздравляем! Вы выбрали правильный ответ!')
        grpbox_result.setStyleSheet('QGroupBox { border: 2px solid #69f369; border-radius: 8%; }')
    else:
        lbl_right_answer.setText('Неверный ответ\nПравильный ответ: ' + answers[0].text())
        grpbox_result.setStyleSheet('QGroupBox { border: 2px solid #ee4433; border-radius: 8%; }')

ask(question_list[0])

#
grpbox_result.hide()
#

window.setLayout(v_line_main)

window.show()
app.exec()

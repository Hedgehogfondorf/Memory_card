from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                            QLabel, QVBoxLayout, QHBoxLayout, 
                            QGroupBox, QRadioButton, QButtonGroup)
import random


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 


#Функции
#Start - проверка, какую функцию запускать
def click_ok():
    if but_ok.text() == 'Ответить':
        check_answer()
    elif but_ok.text() == 'Следующий вопрос':
        next_question()

#Показывает результат ответа
def show_result():
    answer_group.hide()
    result_group.show()
    but_ok.setText('Следующий вопрос')

#Показывает список вопросов
def show_question():
    result_group.hide()
    answer_group.show()
    but_ok.setText('Ответить')
    button_group.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    button_group.setExclusive(True)

#Функция, задающая правильный ответ
def ask(q: Question):
    main_question.setText(q.question)
    random.shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    right_answer_label.setText(q.right_answer)
    show_question()

# Проверка ответа
def check_answer():
    main_win.count += 1
    if answers[0].isChecked():
        answer.setText('Правильно')
        main_win.right_answer += 1
    else:
        answer.setText('Неправильно')
    print(f'Правильных ответов {main_win.right_answer} из {main_win.count}')
    show_result()

#Выводит следующий вопрос
def next_question():
    main_win.cur_question = random.randint(0, len(question_list) - 1)
    q = question_list[main_win.cur_question]
    ask(q)

#создание элементов интерфейса
app = QApplication([])
main_win = QWidget()
main_win.resize(600, 400)
main_win.setWindowTitle('Викторина')
main_question = QLabel(' ')
main_win.count = 0
main_win.right_answer = 0
but_ok = QPushButton('Ответить')

#Создание группы c вопросaми
answer_group = QGroupBox('Варианты ответов')
rbt1 = QRadioButton(' ')
rbt2 = QRadioButton(' ')
rbt3 = QRadioButton(' ')
rbt4 = QRadioButton(' ')
radio_button_group_v_line = QVBoxLayout()
answers = [rbt1, rbt2, rbt3, rbt4]
radio_button_group_v_line.addWidget(rbt1)
radio_button_group_v_line.addWidget(rbt2)
radio_button_group_v_line.addWidget(rbt3)
radio_button_group_v_line.addWidget(rbt4)
answer_group.setLayout(radio_button_group_v_line)

#Привязка на сброс всех переключателей
button_group = QButtonGroup()
button_group.addButton(rbt1)
button_group.addButton(rbt2)
button_group.addButton(rbt3)
button_group.addButton(rbt4)

#Создание группы с результатами
result_group = QGroupBox('Результат теста')
answer = QLabel(' ')
right_answer_label = QLabel(' ')
result_line = QVBoxLayout()
result_line.addWidget(right_answer_label)
result_line.addWidget(answer)
result_group.setLayout(result_line)

#привязка элементов к вертикальной линии
main_line = QVBoxLayout()
main_line.addWidget(main_question, alignment = Qt.AlignCenter)
main_line.addWidget(answer_group)
main_line.addWidget(result_group)
result_group.hide()
main_line.addWidget(but_ok)
main_win.setLayout(main_line)

#обработка событий
but_ok.clicked.connect(click_ok)
question_list = []
question_list.append(Question('Какое время было при Иване IV Грозном?', 'Опричнина', 'Аракчеевщина', 'Пугачёвщина', 'Польская интервенция'))
question_list.append(Question('Как изначально назывался рассказ Солженицына "Один день Ивана Денисовича"?', 'Щ-854', 'Один день в лагере', "День в ГУЛАГ'е", 'Тяжелый труд'))
question_list.append(Question('Год восстания декабристов', '1825', '1914', '1812', '1853'))
question_list.append(Question('Чем является "дир" в слове "Раздирать"?', 'Корень', 'Приставка', 'Суффикс', 'Окончание'))
question_list.append(Question('Формула нахождения дискриминанта', 'b^2-4*a*c', 'a^3-2*a', 'a*b^2', '(-b-a+c)/2'))
question_list.append(Question('Чему равно значение логарифм 3 по основанию 3?', '1', '8', '10', '4'))
question_list.append(Question('В каком году началась вторая мировая война?', '1939', '1941', '1933', '1940'))
question_list.append(Question('В каком году произошёл распад СССР?', '1991', '1990', '1989', '1992'))
question_list.append(Question('Площадь прямоугольного треугольника вычисляется по формуле', '1/2*a*b', 'a*b', '1/3*Sabc*h', 'a*b*c'))
question_list.append(Question('Кто написал "Капитанская дочка"?', 'Пушкин', 'Карамзин', 'Лермонтов', 'Толстой'))
next_question()

#запуск приложения
main_win.show()
app.exec_()
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QMessageBox

app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс від Craze Peaple')
win.resize(400, 200)

text = QLabel(win)
text.setText('Як звали першого ютуб-блогера, який набрав 100000000 підписників')
text.move(30,10)

button1 = QRadioButton(win)
button1.setText('PewDiePie')
button1.move(50,60)

button2 = QRadioButton(win)
button2.setText('Рет і Лінк')
button2.move(290,60)

button3 = QRadioButton(win)
button3.setText('SlivkiShow')
button3.move(50,120)

button4 = QRadioButton(win)
button4.setText('TheBrianMaps')
button4.move(290,120)

button5 = QRadioButton(win)
button5.setText('Mister Max')
button5.move(170,60)

button6 = QRadioButton(win)
button6.setText('EeOneGuy')
button6.move(170,120)

def show_information1():
    box1 = QMessageBox(win)
    box1.setText('Ви виграли зустріч з творцями каналу!')
    box1.exec_()
def show_information2():
    box2 = QMessageBox(win)
    box2.setText('Пощастить іншим разом')
    box2.exec_()

button1.clicked.connect(show_information1)
button2.clicked.connect(show_information2)
button3.clicked.connect(show_information2)
button4.clicked.connect(show_information2)
button5.clicked.connect(show_information2)
button6.clicked.connect(show_information2)

win.show()
app.exec_()

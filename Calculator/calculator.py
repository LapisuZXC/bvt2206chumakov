import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QHBoxLayout,QVBoxLayout,QPushButton, QGridLayout
class Calculator(QWidget):


    def __init__(self):
        super(Calculator,self).__init__()
        self.vbox=QVBoxLayout(self)
        self.hbox_input = QGridLayout()
        self.hbox_first = QGridLayout()
        self.hbox_result = QGridLayout()


        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1, 0, 0)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2, 0, 1)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3,0,2)

        self.b_4 = QPushButton("4", self)
        self.hbox_first.addWidget(self.b_4, 1, 0)

        self.b_5 = QPushButton("5", self)
        self.hbox_first.addWidget(self.b_5,1,1)

        self.b_6 = QPushButton("6", self)
        self.hbox_first.addWidget(self.b_6,1,2)

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7,2,0)

        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8,2,1)

        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9,2,2)

        self.b_0 = QPushButton("0", self)
        self.hbox_first.addWidget(self.b_0,3,1)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus,0,3)
        
        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus,1,3)

        self.b_multiply = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_multiply,2,3)

        self.b_divide = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_divide,3,3)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_del = QPushButton('del',self)
        self.hbox_first.addWidget(self.b_del,3,0)


        self.b_plus.clicked.connect(lambda: self._operation("+"))
        

        self.b_minus.clicked.connect(lambda: self._operation("-"))
        

        self.b_multiply.clicked.connect(lambda: self._operation("*"))

        self.b_divide.clicked.connect(lambda: self._operation("/"))

        self.b_del.clicked.connect(lambda: self._operation_del())

        self.b_result.clicked.connect(self._result)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))




    def _operation_del(self):
        text = self.input.text()
        print(text[:len(text)-1])
        self.input.setText(text[:-1])    


    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)



    def _operation(self, op):
        if self.input.text() != '':

            self.num_1 = int(self.input.text())
            
            self.op = op
            self.input.setText("")



    def _result(self,op):
        if self.input.text() != '':
            self.num_2 = int(self.input.text())
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
            if self.op =="-":
                self.input.setText(str(self.num_1 - self.num_2))
            if self.op =="*":
                self.input.setText(str(self.num_1 * self.num_2))
            if self.op =="/":
                self.input.setText(str(self.num_1 / self.num_2))
        

app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())

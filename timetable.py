import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Расписание группы БВТ2206")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_schedule_o_tab()
        self._create_schedule_e_tab()
        self._create_teacher_tab()


    def _connect_to_db(self):
            self.conn = psycopg2.connect(database="timetable",
                                        user="postgres",
                                        password="Zawarudo112",
                                        host="localhost",
                                        port="5432")

            self.cursor = self.conn.cursor()
    
    def _create_teacher_tab(self):
        self.teacher_table = QWidget()
        self.tabs.addTab(self.teacher_table, "Преподователи")

        self.teach_box = QGroupBox("Преподователи")
        

        self.svbox = QVBoxLayout()
        self.smobox1 = QHBoxLayout()
        self.shobox2 = QHBoxLayout()

        self.svbox.addLayout(self.smobox1)
        
        self.smobox1.addWidget(self.teach_box)

        self._create_teacher_table()

        self.update_schedule_button = QPushButton("Обновить таблицы")
        self.shobox2.addWidget(self.update_schedule_button)
        self.update_schedule_button.clicked.connect(self._update_schedule_o)
        
        self.svbox.addLayout(self.shobox2)
        self.teacher_table.setLayout(self.svbox)

    def _create_teacher_table(self):
        self.teacher_tabs = QTableWidget()
        self.teacher_tabs.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_tabs.setColumnCount(3)
        self.teacher_tabs.setHorizontalHeaderLabels(["Предмет", "Преподователь",""])

        self._update_teacher_table()

        self.teachbox = QVBoxLayout()
        self.teachbox.addWidget(self.teacher_tabs)
        self.teach_box.setLayout(self.teachbox)

    def _create_schedule_o_tab(self):
        self.schedule_tab_o = QWidget()
        self.tabs.addTab(self.schedule_tab_o, "Расписание нечетной недели")

        self.monday_o_gbox = QGroupBox("Понедельник")
        

        self.svbox1 = QVBoxLayout()
        self.svbox2 = QVBoxLayout()
        self.shobox1 = QHBoxLayout()
        self.shobox2 = QHBoxLayout()
        self.shobox3 = QHBoxLayout()
        self.shobox4 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()

        self.svbox1.addLayout(self.shobox1)

        
        self.shobox1.addWidget(self.monday_o_gbox)

        self._create_monday_o_table()

        self.update_schedule_button = QPushButton("Обновить таблицы")
        self.shobox3.addWidget(self.update_schedule_button)
        self.update_schedule_button.clicked.connect(self._update_schedule_o)

        self.tuesday_o_gbox = QGroupBox("Вторник")
        self.svbox1.addLayout(self.shobox1)
        self.shobox1.addWidget(self.tuesday_o_gbox)

        self._create_tuesday_o_table()
        
        self.wednesday_o_gbox = QGroupBox("Среда")
        self.svbox1.addLayout(self.shobox1)
        self.shobox1.addWidget(self.wednesday_o_gbox)

        self._create_wednesday_o_table()

        
        self.thursday_o_gbox = QGroupBox("Четверг")
        self.svbox1.addLayout(self.shobox2)
        self.shobox2.addWidget(self.thursday_o_gbox)

        self._create_thursday_o_table()

        
        self.friday_o_gbox = QGroupBox("Пятница")
        self.svbox1.addLayout(self.shobox2)
        self.shobox2.addWidget(self.friday_o_gbox)

        self._create_friday_o_table()

        
        self.saturday_o_gbox = QGroupBox("Суббота")
        self.svbox1.addLayout(self.shobox2)
        self.shobox2.addWidget(self.saturday_o_gbox)

        self._create_saturday_o_table()

        
        self.svbox1.addLayout(self.shobox3)
        self.schedule_tab_o.setLayout(self.svbox1)

    def _update_teacher_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        records = list(self.cursor.fetchall())

        self.teacher_tabs.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.teacher_tabs.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.teacher_tabs.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.teacher_tabs.setCellWidget(i, 2, joinButton)

            joinButton.clicked.connect(lambda ch, id_n=id, num=i: self._change_teachers(num, id_n))

        self.teacher_tabs.resizeRowsToContents()


    def _create_schedule_e_tab(self):
            self.schedule_tab_e = QWidget()
            self.tabs.addTab(self.schedule_tab_e, "Расписание четной недели")

            self.monday_e_gbox = QGroupBox("Понедельник")
            

            self.svbox = QVBoxLayout()
            self.shebox1 = QHBoxLayout()
            self.shebox2 = QHBoxLayout()
            self.shebox3 = QHBoxLayout()

            self.svbox.addLayout(self.shebox1)
            

            self.shebox1.addWidget(self.monday_e_gbox)

            self._create_monday_e_table()

            self.update_schedule_button = QPushButton("Обновить таблицы")
            self.shebox3.addWidget(self.update_schedule_button)
            self.update_schedule_button.clicked.connect(self._update_schedule_e)

            self.tuesday_e_gbox = QGroupBox("Вторник")
            self.svbox.addLayout(self.shebox1)
            self.shebox1.addWidget(self.tuesday_e_gbox)

            self._create_tuesday_e_table()


            self.wednesday_e_gbox = QGroupBox("Среда")
            self.svbox.addLayout(self.shebox1)
            self.shebox1.addWidget(self.wednesday_e_gbox)

            self._create_wednesday_e_table()

            self.thursday_e_gbox = QGroupBox("Четверг")
            self.svbox.addLayout(self.shebox2)
            self.shebox2.addWidget(self.thursday_e_gbox)

            self._create_thursday_e_table()

            self.friday_e_gbox = QGroupBox("Пятница")
            self.svbox.addLayout(self.shebox2)
            self.shebox2.addWidget(self.friday_e_gbox)

            self._create_friday_e_table()


            self.saturday_e_gbox = QGroupBox("Суббота")
            self.svbox.addLayout(self.shebox2)
            self.shebox2.addWidget(self.saturday_e_gbox)

            self._create_saturday_e_table()


            self.svbox.addLayout(self.shebox3)
            self.schedule_tab_e.setLayout(self.svbox)


    def _create_monday_o_table(self):
        self.monday_o_table = QTableWidget()
        self.monday_o_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_o_table.setColumnCount(5                                   )
        self.monday_o_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_monday_o_table()

        self.movbox = QVBoxLayout()
        self.movbox.addWidget(self.monday_o_table)
        self.monday_o_gbox.setLayout(self.movbox)

    def _create_tuesday_o_table(self):
        self.tuesday_o_table = QTableWidget()
        self.tuesday_o_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_o_table.setColumnCount(4)
        self.tuesday_o_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_tuesday_o_table()

        self.tovbox = QVBoxLayout()
        self.tovbox.addWidget(self.tuesday_o_table)
        self.tuesday_o_gbox.setLayout(self.tovbox)

    def _create_wednesday_o_table(self):
        self.wednesday_o_table = QTableWidget()
        self.wednesday_o_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_o_table.setColumnCount(4)
        self.wednesday_o_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_wednesday_o_table()

        self.wovbox = QVBoxLayout()
        self.wovbox.addWidget(self.wednesday_o_table)
        self.wednesday_o_gbox.setLayout(self.wovbox)

    def _create_thursday_o_table(self):
        self.thursday_o_table = QTableWidget()
        self.thursday_o_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_o_table.setColumnCount(4)
        self.thursday_o_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_thursday_o_table()

        self.thovbox = QVBoxLayout()
        self.thovbox.addWidget(self.thursday_o_table)
        self.thursday_o_gbox.setLayout(self.thovbox)

    def _create_friday_o_table(self):
        self.friday_o_table = QTableWidget()
        self.friday_o_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_o_table.setColumnCount(4)
        self.friday_o_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_friday_o_table()

        self.fovbox = QVBoxLayout()
        self.fovbox.addWidget(self.friday_o_table)
        self.friday_o_gbox.setLayout(self.fovbox)

    def _create_saturday_o_table(self):
        self.saturday_o_table = QTableWidget()
        self.saturday_o_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_o_table.setColumnCount(4)
        self.saturday_o_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_saturday_o_table()

        self.sovbox = QVBoxLayout()
        self.sovbox.addWidget(self.saturday_o_table)
        self.saturday_o_gbox.setLayout(self.sovbox)

    def _create_monday_e_table(self):
        self.monday_e_table = QTableWidget()
        self.monday_e_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_e_table.setColumnCount(4)
        self.monday_e_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_monday_e_table()

        self.mevbox = QVBoxLayout()
        self.mevbox.addWidget(self.monday_e_table)
        self.monday_e_gbox.setLayout(self.mevbox)

    def _create_tuesday_e_table(self):
        self.tuesday_e_table = QTableWidget()
        self.tuesday_e_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_e_table.setColumnCount(4)
        self.tuesday_e_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_tuesday_e_table()

        self.tevbox = QVBoxLayout()
        self.tevbox.addWidget(self.tuesday_e_table)
        self.tuesday_e_gbox.setLayout(self.tevbox)

    def _create_wednesday_e_table(self):
        self.wednesday_e_table = QTableWidget()
        self.wednesday_e_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.wednesday_e_table.setColumnCount(4)
        self.wednesday_e_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_wednesday_e_table()

        self.wevbox = QVBoxLayout()
        self.wevbox.addWidget(self.wednesday_e_table)
        self.wednesday_e_gbox.setLayout(self.wevbox)

    def _create_thursday_e_table(self):
        self.thursday_e_table = QTableWidget()
        self.thursday_e_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_e_table.setColumnCount(5)
        self.thursday_e_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_thursday_e_table()

        self.thevbox = QVBoxLayout()
        self.thevbox.addWidget(self.thursday_e_table)
        self.thursday_e_gbox.setLayout(self.thevbox)

    def _create_friday_e_table(self):
        self.friday_e_table = QTableWidget()
        self.friday_e_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_e_table.setColumnCount(4)
        self.friday_e_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_friday_e_table()

        self.fevbox = QVBoxLayout()
        self.fevbox.addWidget(self.friday_e_table)
        self.friday_e_gbox.setLayout(self.fevbox)

    def _create_saturday_e_table(self):
        self.saturday_e_table = QTableWidget()
        self.saturday_e_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.saturday_e_table.setColumnCount(4)
        self.saturday_e_table.setHorizontalHeaderLabels(["Предмет", "Время", "Кабинет", ""])

        self._update_saturday_e_table()

        self.sevbox = QVBoxLayout()
        self.sevbox.addWidget(self.saturday_e_table)
        self.saturday_e_gbox.setLayout(self.sevbox)




    def _update_monday_o_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Понедельник' AND odd=True")
        records = list(self.cursor.fetchall())

        self.monday_o_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")
            deleteButton = QPushButton("Удалить")

            self.monday_o_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.monday_o_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_o_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_o_table.setCellWidget(i, 3, joinButton)
            self.monday_o_table.setCellWidget(i,4,deleteButton)

            joinButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_o_monday(num,id_n))
            deleteButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_o_monday(num,id_n))
        createButton = QPushButton('create')
        self.monday_o_table.setCellWidget(len(records),3,createButton)
        createButton.clicked.connect((lambda ch, num=len(records)+1:self._insert_into_monday_o_table(num)))


        self.monday_o_table.resizeRowsToContents()

    def _insert_into_monday_o_table(self, num):
        row = list()
        for i in range(self.monday_o_table.columnCount()):
            try:
                row.append(self.monday_o_table.item(num,i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"Insert into timetable (subject,time,room) values ('{row[0]}','{row[1]}','{row[2]}')")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self,"Error","Cannot insert")

    def _set_day_to_o_monday(self, num):        
        row = list()
        for i in range(self.monday_o_table.columnCount()):
            try:
                row.append(self.monday_o_table.item(num, i).text())
            except Exception:
                row.append(None)        
        try:
            self.cursor.execute(f"insert into timetable (subject, time,room) values( '{row[0]}','{row[1]}','{row[2]}'   )")
            self.conn.commit()        
        except Exception:
            QMessageBox.about(self, "Error", "Cant insert row")


    def _change_day_from_o_monday(self, rowNum,id_n):
        row = list()
        for i in range(self.monday_o_table.columnCount()):
            try:
                row.append(self.monday_o_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', time = '{row[1]}',room = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_tuesday_o_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Вторник' AND odd=True")
        records = list(self.cursor.fetchall())

        self.tuesday_o_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.tuesday_o_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_o_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_o_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_o_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, id_n=id,num=i: self._change_day_from_o_tuesday(num,id_n))

        self.tuesday_o_table.resizeRowsToContents()

    def _change_day_from_o_tuesday(self, rowNum,id_n):
        row = list()
        for i in range(self.tuesday_o_table.columnCount()):
            try:
                row.append(self.tuesday_o_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_wednesday_o_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Среда' AND odd=True")
        records = list(self.cursor.fetchall())

        self.wednesday_o_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.wednesday_o_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.wednesday_o_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_o_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_o_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id,num=i: self._change_day_from_o_wednesday(num,id_n))



        self.wednesday_o_table.resizeRowsToContents()

    def _change_day_from_o_wednesday(self, rowNum,id_n):
        row = list()
        for i in range(self.wednesday_o_table.columnCount()):
            try:
                row.append(self.wednesday_o_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_thursday_o_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Четверг' AND odd=True")
        records = list(self.cursor.fetchall())

        self.thursday_o_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.thursday_o_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.thursday_o_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_o_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.thursday_o_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_o_thursday(num,id_n))

        self.thursday_o_table.resizeRowsToContents()

    def _change_day_from_o_thursday(self, rowNum,id_n):
        row = list()
        for i in range(self.thursday_o_table.columnCount()):
            try:
                row.append(self.thursday_o_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")


    def _update_friday_o_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Пятница' AND odd=True")
        records = list(self.cursor.fetchall())

        self.friday_o_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.friday_o_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.friday_o_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.friday_o_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.friday_o_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, id_n,num=i: self._change_day_from_o_friday(num,id_n))

        self.friday_o_table.resizeRowsToContents()

    def _change_day_from_o_friday(self, rowNum,id_n):
        row = list()
        for i in range(self.friday_e_table.columnCount()):
            try:
                row.append(self.friday_o_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_saturday_o_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Суббота' AND odd=True")
        records = list(self.cursor.fetchall())

        self.saturday_o_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.saturday_o_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.saturday_o_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.saturday_o_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.saturday_o_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_o_saturday(num,id_n))

        self.saturday_o_table.resizeRowsToContents()

    def _change_day_from_o_saturday(self, rowNum,id_n):
        row = list()
        for i in range(self.saturday_o_table.columnCount()):
            try:
                row.append(self.saturday_o_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_monday_e_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Понедельник' AND odd=False")
        records = list(self.cursor.fetchall())

        self.monday_e_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.monday_e_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.monday_e_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.monday_e_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_e_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_e_monday(num,id_n))

        self.monday_e_table.resizeRowsToContents()

    def _change_day_from_e_monday(self, rowNum,id_n):
        row = list()
        for i in range(self.monday_e_table.columnCount()):
            try:
                row.append(self.monday_e_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_tuesday_e_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Вторник' AND odd=False")
        records = list(self.cursor.fetchall())

        self.tuesday_e_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.tuesday_e_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_e_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_e_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_e_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_e_tuesday(num,id_n))

        self.tuesday_e_table.resizeRowsToContents()

    def _change_day_from_e_tuesday(self, rowNum,id_n):
        row = list()
        for i in range(self.tuesday_e_table.columnCount()):
            try:
                row.append(self.tuesday_e_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_wednesday_e_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Среда' AND odd=False")
        records = list(self.cursor.fetchall())

        self.wednesday_e_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.wednesday_e_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.wednesday_e_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_e_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_e_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id ,num=i: self._change_day_from_e_wednesday(num,id_n))

        self.wednesday_e_table.resizeRowsToContents()

    def _change_day_from_e_wednesday(self, rowNum,id_n):
        row = list()
        for i in range(self.wednesday_e_table.columnCount()):
            try:
                row.append(self.wednesday_e_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_thursday_e_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Четверг' AND odd=False")
        records = list(self.cursor.fetchall())

        self.thursday_e_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.thursday_e_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.thursday_e_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_e_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.thursday_e_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, id_n=id,num=i: self._change_day_from_e_thursday(num,id_n))

        self.thursday_e_table.resizeRowsToContents()

    def _change_day_from_e_thursday(self, rowNum,id_n):
        row = list()
        for i in range(self.thursday_e_table.columnCount()):
            try:
                row.append(self.thursday_e_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_friday_e_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Пятница' AND odd=False")
        records = list(self.cursor.fetchall())

        self.friday_e_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.friday_e_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.friday_e_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.friday_e_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.friday_e_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch,id_n=id, num=i: self._change_day_from_e_friday(num,id_n))

    def _change_day_from_e_friday(self, rowNum,id_n):
        row = list()
        for i in range(self.friday_e_table.columnCount()):
            try:
                row.append(self.friday_e_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

        self.friday_e_table.resizeRowsToContents()

    def _update_saturday_e_table(self):
        self.cursor.execute("SELECT * FROM timetable WHERE day='Суббота' AND odd=False")
        records = list(self.cursor.fetchall())

        self.saturday_e_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.saturday_e_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[2])))
            self.saturday_e_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[4])))
            self.saturday_e_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.saturday_e_table.setCellWidget(i, 3, joinButton)

            joinButton.clicked.connect(lambda ch, id_n=id, num=i: self._change_day_from_e_saturday(num,id_n))

        self.saturday_e_table.resizeRowsToContents()
    def _change_day_from_e_saturday(self, rowNum,id_n):
        row = list()
        for i in range(self.saturday_e_table.columnCount()):
            try:
                row.append(self.saturday_e_table.item(rowNum, i).text())
            except Exception:
                row.append(None)
        try:
            self.cursor.execute(f"UPDATE timetable SET subject = '{row[0]}', start_time = '{row[1]}',room_nubmer = '{row[2]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_teacher_table(self):
        self.cursor.execute("SELECT * FROM teacher")
        records = list(self.cursor.fetchall())

        self.teacher_tabs.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            id = r[0]
            joinButton = QPushButton("Обновить")

            self.teacher_tabs.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.teacher_tabs.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.teacher_tabs.setCellWidget(i, 2, joinButton)

            joinButton.clicked.connect(lambda ch, id_n=id, num=i: self._change_teachers(num, id_n))

        self.teacher_tabs.resizeRowsToContents()


    def _change_teachers(self, rowNum, id_n):
        row = list()
        for i in range(self.teacher_tabs.columnCount()):
            try:
                row.append(self.teacher_tabs.item(rowNum, i).text())
            except Exception:
                row.append(None)

        try:
            self.cursor.execute(f"UPDATE teacher SET full_name = '{row[0]}', subject = '{row[1]}' WHERE id = {id_n}")
            self.conn.commit()
        except Exception:
            QMessageBox.about(self, "Error", "Введите данные")

    def _update_schedule_o(self):
        self._update_monday_o_table()
        self._update_tuesday_o_table()
        self._update_wednesday_o_table()
        self._update_thursday_o_table()
        self._update_friday_o_table()
        self._update_saturday_o_table()

    def _update_schedule_e(self):
        self._update_monday_e_table()
        self._update_tuesday_e_table()
        self._update_wednesday_e_table()
        self._update_thursday_e_table()
        self._update_friday_e_table()
        self._update_saturday_e_table()

    def _update_teacher(self):
        self._update_teacher_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())

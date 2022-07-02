import datetime
from ntpath import join
import os
import sys
from PyQt5 import uic 
from PyQt5.QtCore import Qt  , QDate  , QPoint 
from PyQt5.QtGui import QColor , QCursor 
from PyQt5.QtWidgets import QApplication , QMainWindow , QTableWidgetItem  ,QHeaderView  , QCalendarWidget , QGraphicsDropShadowEffect , QPushButton

Home = uic.loadUiType(os.path.join(os.getcwd() , "QT.ui"))[0]
Employee = uic.loadUiType(os.path.join(os.getcwd() , "Employee.ui"))[0]
Tasks = uic.loadUiType(os.path.join(os.getcwd() , "Task.ui"))[0]
MileStones = uic.loadUiType(os.path.join(os.getcwd() , "MileStone.ui"))[0]

class MileStone() :
    def __init__(self , name , date):
        self.name = name
        self.date = date

class Person () :
    def __init__(self , name ,ID , sex , age , joinDate , tasks , finishedTasks , unfinishedTasks ) :
        self.name = name
        self.ID = ID
        self.sex = sex
        self.age = age
        self.joinDate = joinDate
        self.tasks = tasks
        self.finishedTasks = finishedTasks
        self.unfinishedTasks = unfinishedTasks

class Task () :
    def __init__(self , name ,startedTime , deadline , importance , milestone  ,persons  ) :
        self.milestone = []
        self.name = name
        self.startedTime = startedTime
        self.deadline = deadline
        self.importance = importance
        self.milestone.append(milestone)
        self.persons = persons

class programData():
    def __init__(self) :
        self.employ = []
        self.task = []

    def addEmployee(self ,name ,ID , sex , age , joinDate , tasks , finishedTasks , unfinishedTasks):
        person = Person(name ,ID , sex , age , joinDate , tasks , finishedTasks , unfinishedTasks)
        self.employ.append(person)

    def addTask(self , name ,startedTime , deadline , importance , milestone  ,persons):
        task = Task(name ,startedTime , deadline , importance , milestone  ,persons)
        self.task.append(task)

class MainWindow (QMainWindow , Home):
    def __init__(self):
        super(MainWindow , self).__init__()
        self.data = programData()
        self.addSignal = "none"
        self.setupUi(self)
        self.backButton.hide()
        self.addbutton.hide()
        self.tableWidget.hide()
        self.emptyText.hide()
        self.emptyText2.hide()
        self.MainText.setStyleSheet("color : red ; border : none")
        self.MainText2.setStyleSheet("color : #2ed3e6 ; border : none")
        effect = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#2ed3e6"))
        effect2 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#2ed3e6"))
        effect3 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=10, color=QColor("#2ed3e6"))
        effect4 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=10, color=QColor("#2ed3e6"))
        self.employeeButton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 20px ")
        self.employeeButton.setGraphicsEffect(effect2)
        self.employeeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.taskButton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 20px")
        self.taskButton.setGraphicsEffect(effect)
        self.taskButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 10px")
        self.backButton.setGraphicsEffect(effect4)
        self.backButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addbutton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 10px")
        self.addbutton.setGraphicsEffect(effect3)
        self.addbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white")
        self.employeeButton.clicked.connect(self.employ)
        self.taskButton.clicked.connect(self.task)
        self.backButton.clicked.connect(self.back)
        self.addbutton.clicked.connect(self.add)
    def employ(self):
        self.addSignal = "employ"
        self.backButton.show()
        self.MainText2.hide()
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.MainText.setText("Employees Section")
        self.MainText.setStyleSheet("color : white ; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
        if (len(self.data.employ) != 0) :
            self.tableWidget.clear()
            self.tableWidget.show()
            self.emptyText.hide()
            self.emptyText2.hide()
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white ; border : none")
            self.tableWidget.setColumnCount(10)
            self.tableWidget.setRowCount(len(self.data.employ))
            self.tableWidget.setHorizontalHeaderItem( 0 , QTableWidgetItem("Name"))
            self.tableWidget.setHorizontalHeaderItem( 1 , QTableWidgetItem("ID"))
            self.tableWidget.setHorizontalHeaderItem( 2 , QTableWidgetItem("Sex"))
            self.tableWidget.setHorizontalHeaderItem( 3 , QTableWidgetItem("Age"))
            self.tableWidget.setHorizontalHeaderItem( 4 , QTableWidgetItem("Join Date"))
            self.tableWidget.setHorizontalHeaderItem( 5 , QTableWidgetItem("Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 6 , QTableWidgetItem("Finished Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 7 , QTableWidgetItem("UnFinished Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 8 , QTableWidgetItem("Delete"))
            self.tableWidget.setHorizontalHeaderItem( 9 , QTableWidgetItem("Edit"))
            self.tableWidget.horizontalHeader().setStyleSheet(" color : black")
            self.tableWidget.verticalHeader().setStyleSheet(" color : black")
            header = self.tableWidget.horizontalHeader()
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            header.setSectionResizeMode(8 , 20)
            header.setSectionResizeMode(9 , 20)
            self.tableWidget.verticalHeader().setDefaultSectionSize(85)
            i = 0
            for emploees in self.data.employ :
                name = QTableWidgetItem(emploees.name)
                name.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 0 ,name )

                id = QTableWidgetItem(str(emploees.ID))
                id.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 1 ,id )

                sex = QTableWidgetItem(emploees.sex)
                sex.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 2 ,sex )

                age = QTableWidgetItem(str(emploees.age))
                age.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 3 ,age )

                joinDate = QTableWidgetItem(emploees.joinDate.toString("MMMM dd yyyy"))
                joinDate.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 4 ,joinDate )

                tasks = QTableWidgetItem(emploees.tasks)
                tasks.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 5 ,tasks )
                if (emploees.finishedTasks == ""):
                    finishedTasks = QTableWidgetItem("none")
                    finishedTasks.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i , 6 , finishedTasks )
                else :
                    finishedTasks = QTableWidgetItem(emploees.finishedTasks)
                    finishedTasks.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i , 6 , finishedTasks )
                
                if (emploees.unfinishedTasks == ""):
                    finishedTasks = QTableWidgetItem("none")
                    finishedTasks.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i , 7 , finishedTasks )
                else :
                    finishedTasks = QTableWidgetItem(emploees.unfinishedTasks)
                    finishedTasks.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(i , 7 , finishedTasks )
    
                button = QPushButton("❌")
                button.setStyleSheet("font : 20px ; color :red")
                button.setCursor(QCursor(Qt.PointingHandCursor))
                button.clicked.connect(lambda: self.deleteEmployee(i))
                self.tableWidget.setCellWidget(i , 8 , button )

                button2 = QPushButton("🖊️")
                button2.setStyleSheet("font : 20px ; color :green")
                button2.setCursor(QCursor(Qt.PointingHandCursor))
                button2.clicked.connect(lambda: self.editEmployee(i))
                self.tableWidget.setCellWidget(i , 9 , button2 )

                i = i + 1
        else :
            self.tableWidget.hide()
            self.emptyText.show()
            self.emptyText2.show()
            self.emptyText2.setStyleSheet("color : white ; border : none")
            self.emptyText.setText("Sorry There is No Employee :(")
            self.emptyText.setStyleSheet("color : white ; border : none")
            self.emptyText.setAlignment(Qt.AlignCenter)
    def task(self) :
        self.addSignal = "task"
        self.backButton.show()
        self.MainText2.hide()
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.MainText.setText("Tasks Section")
        self.MainText.setStyleSheet("color : white; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
        if (len(self.data.task) != 0) :
            self.tableWidget.clear()
            self.tableWidget.show()
            self.emptyText.hide()
            self.emptyText2.hide()
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white ;border : none ; ")
            self.tableWidget.setColumnCount(9 )
            self.tableWidget.setRowCount(len(self.data.task))
            self.tableWidget.setHorizontalHeaderItem( 0 , QTableWidgetItem("Name"))
            self.tableWidget.setHorizontalHeaderItem( 1 , QTableWidgetItem("Started Time"))
            self.tableWidget.setHorizontalHeaderItem( 2 , QTableWidgetItem("Deadline"))
            self.tableWidget.setHorizontalHeaderItem( 3 , QTableWidgetItem("Importance"))
            self.tableWidget.setHorizontalHeaderItem( 4 , QTableWidgetItem("Persons"))
            self.tableWidget.setHorizontalHeaderItem( 5 , QTableWidgetItem("Milestone"))
            self.tableWidget.setHorizontalHeaderItem( 6 , QTableWidgetItem("Add M.S"))
            self.tableWidget.setHorizontalHeaderItem( 7 , QTableWidgetItem("Delete"))
            self.tableWidget.setHorizontalHeaderItem( 8 , QTableWidgetItem("Edit"))
            self.tableWidget.horizontalHeader().setStyleSheet(" color : black")
            self.tableWidget.verticalHeader().setStyleSheet(" color : black")
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(6 , 20)
            header.setSectionResizeMode(7 , 20)
            header.setSectionResizeMode(8 , 20)
            self.tableWidget.verticalHeader().setDefaultSectionSize(85)
            i = 0
            for tasks in self.data.task :
                name = QTableWidgetItem(tasks.name)
                name.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 0 ,name )

                id = QTableWidgetItem(str(tasks.startedTime.toString("MMMM dd yyyy")))
                id.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 1 ,id )

                sex = QTableWidgetItem(tasks.deadline.toString("MMMM dd yyyy"))
                sex.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 2 ,sex )

                age = QTableWidgetItem(str(tasks.importance))
                age.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 3 ,age )

                person = QTableWidgetItem(tasks.persons)
                person.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 4 ,person )

                text = ""                
                for mile  in tasks.milestone :
                    x = datetime.datetime.now()
                    y = QDate(x.year , x.month , x.day)
                    days = y.daysTo(mile.date)
                    if (days < 1) :
                        text  = text + mile.name + "  --> with Deadline Passed "
                    else :
                        text  = text + mile.name + "  --> with Remaining Days: " + str(days) 
                    if (mile != tasks.milestone[len(tasks.milestone) - 1]):
                        text = text + "\n"

                joinDate = QTableWidgetItem(text)
                joinDate.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 5 ,joinDate )



                button = QPushButton("➕")
                button.setStyleSheet("font : 20px")
                button.setCursor(QCursor(Qt.PointingHandCursor))
                button.clicked.connect(lambda: self.addMileStone(i))
                self.tableWidget.setCellWidget(i , 6 , button )

                button = QPushButton("❌")
                button.setStyleSheet("font : 20px ")
                button.setCursor(QCursor(Qt.PointingHandCursor))
                button.clicked.connect(lambda: self.deleteTask(i))
                self.tableWidget.setCellWidget(i , 7 , button )

                button2 = QPushButton("🖊️")
                button2.setStyleSheet("font : 20px ; color :green")
                button2.setCursor(QCursor(Qt.PointingHandCursor))
                button2.clicked.connect(lambda: self.editTask(i))
                self.tableWidget.setCellWidget(i , 8 , button2 )

        else :
            self.emptyText.show()
            self.emptyText2.show()
            self.tableWidget.hide()
            self.emptyText2.setStyleSheet("color : white ; border : none")
            self.emptyText.setText("Sorry There is No Tasks :(")
            self.emptyText.setStyleSheet("color : white ; border : none")
            self.emptyText.setAlignment(Qt.AlignCenter)
    def back(self):
        self.addSignal = "none"
        self.emptyText.hide()
        self.MainText2.show()
        self.emptyText2.hide()
        self.addbutton.hide()
        self.backButton.hide()
        self.taskButton.show()
        self.employeeButton.show()
        self.tableWidget.hide()
        self.MainText.setText("Main Menu")
        self.MainText.setStyleSheet("color : white; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
    def add(self) :
        if (self.addSignal == "employ"):
            self.w = EmployeeWindow(self , "none")
            self.w.show()
        elif(self.addSignal == "task"):
            self.w = TaskWindow(self , "none")
            self.w.show()
        else :
            return
    def deleteTask(self , index) :
        self.data.task.pop(index -1)
        self.task()
    def deleteEmployee(self , index) :
        print(index)
        self.data.employ.pop(index - 1)
        self.employ()
    def editTask(self , index) :
        self.w = TaskWindow(self , index - 1)
        self.w.show()
    def editEmployee(self , index) :
        self.w = EmployeeWindow(self , index - 1)
        self.w.show()
    def addMileStone(self , index) :
        self.w  = MileStonePage(self , index - 1)
        self.w.show()
    
class EmployeeWindow (QMainWindow , Employee):
    def __init__(self , MainWindow , inde):
        super(EmployeeWindow, self).__init__()
        self.setupUi(self)
        self.inde = inde
        self.MainWindow = MainWindow
        ####################################################################################################
        self.MainText.setStyleSheet("color : white ; border : none")
        self.NameText.setStyleSheet("color : white ; border : none")
        self.IDText.setStyleSheet("color : white ; border : none")
        self.SexText.setStyleSheet("color : white ; border : none")
        self.AgeText.setStyleSheet("color : white ; border : none")
        self.JointDateText.setStyleSheet("color : white ; border : none")
        self.TasksText.setStyleSheet("color : white ; border : none")
        self.FinishedTasksText.setStyleSheet("color : white ; border : none")
        self.UnfinishedTasksText.setStyleSheet("color : white ; border : none")
        self.MaleradioButton.setStyleSheet("color : white")
        self.FemaleradioButton.setStyleSheet("color : white")
        self.AlertText_1.setStyleSheet("border : none ; color : red")
        self.AlertText_2.setStyleSheet("border : none ; color : red")
        self.AlertText_3.setStyleSheet("border : none ; color : red")
        self.AlertText_4.setStyleSheet("border : none ; color : red")
        self.AlertText_5.setStyleSheet("border : none ; color : red")
        self.AlertText_6.setStyleSheet("border : none ; color : red")
        ####################################################################################################
        self.NameEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.IDspinBox.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.AgespinBox.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.dateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.TasksEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.FinishedTasksEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.UnfinishedTasksEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        ####################################################################################################
        self.AlertText_1.hide()
        self.AlertText_2.hide()
        self.AlertText_3.hide()
        self.AlertText_4.hide()
        self.AlertText_5.hide()
        self.AlertText_6.hide()
        ####################################################################################################
        self.IDspinBox.setMinimum(10000000)
        self.IDspinBox.setMaximum(99999999)
        self.AgespinBox.setMaximum(100)
        self.AgespinBox.setMinimum(15)
        self.dateEdit.setDisplayFormat("MMMM dd yyyy")  
        x = datetime.datetime.now()
        self.dateEdit.setDate(QDate(x.year , x.month , x.day))
        self.dateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none")
        self.dateEdit.setCalendarWidget(y)
        self.CanclepushButton.clicked.connect(self.close)
        self.SubmitpushButton.clicked.connect(self.submit)
        effect1 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#111"))
        effect2 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#111"))
        self.SubmitpushButton.setStyleSheet("background-color : #034a21 ; color : white ; border-radius : 10px")
        self.SubmitpushButton.setGraphicsEffect(effect1)
        self.CanclepushButton.setStyleSheet("background-color : #91070f ; color : white ; border-radius : 10px")
        self.CanclepushButton.setGraphicsEffect(effect2)

        if (inde != "none") :  
            self.MainText.setText("Edit Person")
            self.MainText.setStyleSheet("color : white ; border : none")
            self.MainText.setAlignment(Qt.AlignCenter)
            self.NameEdit.setText(MainWindow.data.employ[self.inde].name)
            self.IDspinBox.setValue(MainWindow.data.employ[self.inde].ID)
            self.AgespinBox.setValue(MainWindow.data.employ[self.inde].age)
            self.dateEdit.setDate(QDate(MainWindow.data.employ[self.inde].joinDate))
            self.TasksEdit.setText(MainWindow.data.employ[self.inde].tasks)
            self.FinishedTasksEdit.setText(MainWindow.data.employ[self.inde].finishedTasks)
            self.UnfinishedTasksEdit.setText(MainWindow.data.employ[self.inde].unfinishedTasks)
            if (MainWindow.data.employ[self.inde].sex == "Male") :
                self.MaleradioButton.setChecked(1)
            else :
                self.FemaleradioButton.setChecked(1)

    def submit(self) :
        flag = 0
        if(self.NameEdit.text() == "") :
            self.AlertText_1.show()
            flag = 1
        if(self.IDspinBox.text() == "") :
            self.AlertText_2.show()
            flag = 1
        if(self.AgespinBox.text() == "") :
            self.AlertText_4.show()
            flag = 1
        if(self.dateEdit.text() == "") :
            self.AlertText_5.show()
            flag = 1
        if(self.TasksEdit.text() == "") :
            self.AlertText_6.show()
            flag = 1
        if((self.MaleradioButton.isChecked() == False and self.FemaleradioButton.isChecked() == False)) :
            self.AlertText_3.show()
            flag = 1
        if (flag == 0):
            if self.MaleradioButton.isChecked():
                self.sex = "Male"
            elif self.FemaleradioButton.isChecked():
                self.sex = "Female"
            if (self.inde != "none") :
                self.MainWindow.data.employ[self.inde] = Person(self.NameEdit.text() , self.IDspinBox.value() , self.sex , self.AgespinBox.value() , self.dateEdit.date() , self.TasksEdit.text() , self.FinishedTasksEdit.text() , self.UnfinishedTasksEdit.text())
            else :
                self.MainWindow.data.addEmployee(self.NameEdit.text() , self.IDspinBox.value() , self.sex , self.AgespinBox.value() , self.dateEdit.date() , self.TasksEdit.text() , self.FinishedTasksEdit.text() , self.UnfinishedTasksEdit.text())
            self.MainWindow.employ()
            self.close()

class TaskWindow (QMainWindow , Tasks):
    def __init__(self , MainWindow , inde):
        super(TaskWindow, self).__init__()
        self.setupUi(self)
        self.inde = inde
        self.MainWindow = MainWindow
        ####################################################################################################
        self.MainText.setStyleSheet("color : white ; border : none")
        self.NameText.setStyleSheet("color : white ; border : none")
        self.StartedTimeText.setStyleSheet("color : white ; border : none")
        self.DeadLineText.setStyleSheet("color : white ; border : none")
        self.ImportanceText.setStyleSheet("color : white ; border : none")
        self.MilestoneText.setStyleSheet("color : white ; border : none")
        self.PersonsText.setStyleSheet("color : white ; border : none")
        self.CanclepushButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.SubmitpushButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.AlertText_1.setStyleSheet("border : none ; color : red")
        self.AlertText_2.setStyleSheet("border : none ; color : red")
        self.AlertText_3.setStyleSheet("border : none ; color : red")
        self.AlertText_4.setStyleSheet("border : none ; color : red")
        self.AlertText_5.setStyleSheet("border : none ; color : red")
        self.AlertText_6.setStyleSheet("border : none ; color : red")
        ####################################################################################################
        self.NameEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ;border-radius : 5px ; padding-left : 10px")
        self.StartedTimedateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.DeadLinedateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.ImportanceEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.MilestoneEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        self.MileStoneDate.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 5px")
        self.PersonsEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        ####################################################################################################
        self.AlertText_1.hide()
        self.AlertText_2.hide()
        self.AlertText_3.hide()
        self.AlertText_4.hide()
        self.AlertText_5.hide()
        self.AlertText_6.hide()
        ####################################################################################################
        self.CanclepushButton.clicked.connect(self.close)
        #self.SubmitpushButton.clicked.connect(self.send_data)
        ####################################################################################################
        self.StartedTimedateEdit.setDisplayFormat("MMMM dd yyyy") 
        x = datetime.datetime.now()
        self.StartedTimedateEdit.setDate(QDate(x.year , x.month , x.day))
        self.StartedTimedateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none")
        self.StartedTimedateEdit.setCalendarWidget(y)

        effect1 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#111"))
        effect2 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#111"))
        self.SubmitpushButton.setStyleSheet("background-color : #034a21 ; color : white ; border-radius : 10px")
        self.CanclepushButton.setStyleSheet("background-color : #91070f ; color : white ; border-radius : 10px")
        self.SubmitpushButton.setGraphicsEffect(effect1)
        self.CanclepushButton.setGraphicsEffect(effect2)

        self.DeadLinedateEdit.setDisplayFormat("MMMM dd yyyy") 
        x = datetime.datetime.now()
        self.DeadLinedateEdit.setDate(QDate(x.year , x.month , x.day))
        self.DeadLinedateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none ")
        self.DeadLinedateEdit.setCalendarWidget(y)

        self.MileStoneDate.setDisplayFormat("MMMM dd yyyy")
        x = datetime.datetime.now()
        self.MileStoneDate.setDate(QDate(x.year , x.month , x.day))
        self.MileStoneDate.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none ")
        self.MileStoneDate.setCalendarWidget(y)

        self.CanclepushButton.clicked.connect(self.close)
        self.SubmitpushButton.clicked.connect(self.submit)

        if (inde != "none") :  
            self.MainText.setText("Edit Task")
            self.MainText.setStyleSheet("color : white ; border : none")
            self.MainText.setAlignment(Qt.AlignCenter)
            self.NameEdit.setText(MainWindow.data.task[inde].name)
            self.StartedTimedateEdit.setDate(MainWindow.data.task[inde].startedTime)
            self.DeadLinedateEdit.setDate(MainWindow.data.task[inde].deadline)
            self.ImportanceEdit.setText(MainWindow.data.task[inde].importance)
            self.MilestoneEdit.setText(MainWindow.data.task[inde].milestone[0].name)
            self.MileStoneDate.setDate(MainWindow.data.task[inde].milestone[0].date)
            self.PersonsEdit.setText(MainWindow.data.task[inde].persons)

    def submit(self) :
        flag = 0
        if(self.NameEdit.text() == "") :
            self.AlertText_1.show()
            flag = 1
        if(self.StartedTimedateEdit.text() == "") :
            self.AlertText_2.show()
            flag = 1
        if(self.DeadLinedateEdit.text() == "") :
            self.AlertText_3.show()
            flag = 1
        if(self.ImportanceEdit.text() == "") :
            self.AlertText_4.show()
            flag = 1
        if(self.MilestoneEdit.text() == "") :
            self.AlertText_5.show()
            flag = 1
        if(self.PersonsEdit.text() == "") :
            self.AlertText_6.show()
            flag = 1
        if (flag == 0):
            if (self.inde != "none") :
                self.MainWindow.data.task[self.inde].name  = self.NameEdit.text()
                self.MainWindow.data.task[self.inde].startedTime  = self.StartedTimedateEdit.date()
                self.MainWindow.data.task[self.inde].deadline  = self.DeadLinedateEdit.date()
                self.MainWindow.data.task[self.inde].importance  = self.ImportanceEdit.text()
                self.MainWindow.data.task[self.inde].milestone[0].name  = self.MilestoneEdit.text() 
                self.MainWindow.data.task[self.inde].milestone[0].date  = self.MileStoneDate.date()
                self.MainWindow.data.task[self.inde].persons  = self.PersonsEdit.text()
            else :
                self.MainWindow.data.addTask(self.NameEdit.text() , self.StartedTimedateEdit.date(), self.DeadLinedateEdit.date() , self.ImportanceEdit.text() , MileStone(self.MilestoneEdit.text() ,self.MileStoneDate.date())  , self.PersonsEdit.text())
            self.MainWindow.task()
            self.close()

class MileStonePage (QMainWindow , MileStones):
    def __init__(self , MainWindow , inde):
        super(MileStonePage, self).__init__()
        self.setupUi(self)
        self.inde = inde
        self.MainWindow = MainWindow
        self.MainText.setStyleSheet("color : white ; border : none")
        self.NameText.setStyleSheet("color : white ; border : none")
        self.StartedTimeText.setStyleSheet("color : white ; border : none")
        self.AlertText_1.setStyleSheet("border : none ; color : red")
        self.AlertText_2.setStyleSheet("border : none ; color : red")
        ####################################################################################################
        self.NameEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ;border-radius : 5px ; padding-left : 10px")
        self.StartedTimedateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none ; border-radius : 5px ; padding-left : 10px")
        ####################################################################################################
        self.AlertText_1.hide()
        self.AlertText_2.hide()
        ####################################################################################################
        self.StartedTimedateEdit.setDisplayFormat("MMMM dd yyyy") 
        x = datetime.datetime.now()
        self.StartedTimedateEdit.setDate(QDate(x.year , x.month , x.day))
        self.StartedTimedateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none")
        self.StartedTimedateEdit.setCalendarWidget(y)

        effect1 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#111"))
        effect2 = QGraphicsDropShadowEffect(offset=QPoint(0, 0), blurRadius=25, color=QColor("#111"))
        self.SubmitpushButton.setStyleSheet("background-color : #034a21 ; color : white ; border-radius : 10px")
        self.CanclepushButton.setStyleSheet("background-color : #91070f ; color : white ; border-radius : 10px")
        self.SubmitpushButton.setGraphicsEffect(effect1)
        self.CanclepushButton.setGraphicsEffect(effect2)
        self.CanclepushButton.clicked.connect(self.close)
        self.SubmitpushButton.clicked.connect(self.submit)
    def submit(self):
        flag = 0
        if(self.NameEdit.text() == "") :
            self.AlertText_1.show()
            flag = 1
        if(self.StartedTimedateEdit.text() == "") :
            self.AlertText_2.show()
            flag = 1
        if (flag == 0):
            self.MainWindow.data.task[self.inde].milestone.append(MileStone(self.NameEdit.text() , self.StartedTimedateEdit.date()))
            self.MainWindow.task()
            self.close()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
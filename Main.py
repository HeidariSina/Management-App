from asyncio import tasks
import datetime
import os
import sys
from PyQt5 import uic 
from PyQt5.QtCore import Qt  , QDate  
from PyQt5.QtWidgets import QApplication , QMainWindow , QTableWidgetItem  ,QHeaderView  , QCalendarWidget

Home = uic.loadUiType(os.path.join(os.getcwd() , "QT.ui"))[0]
Employee = uic.loadUiType(os.path.join(os.getcwd() , "Employee.ui"))[0]
Tasks = uic.loadUiType(os.path.join(os.getcwd() , "Task.ui"))[0]

class MileStone() :
    def __init__(self , name , checked):
        self.name = name
        self.checked = checked

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
        self.name = name
        self.startedTime = startedTime
        self.deadline = deadline
        self.importance = importance
        self.milestone = milestone
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
        self.MainText.setStyleSheet("color : white ; border : none")
        self.employeeButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.taskButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.backButton.setStyleSheet("background-color : #1a161c ; color : white")
        self.addbutton.setStyleSheet("background-color : #1a161c ; color : white")
        self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white")
        self.employeeButton.clicked.connect(self.employ)
        self.taskButton.clicked.connect(self.task)
        self.backButton.clicked.connect(self.back)
        self.addbutton.clicked.connect(self.add)
    def employ(self):
        self.addSignal = "employ"
        self.backButton.show()
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.MainText.setText("Employees Section")
        self.MainText.setStyleSheet("color : white ; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
        if (len(self.data.employ) != 0) :
            self.tableWidget.show()
            self.emptyText.hide()
            self.emptyText2.hide()
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white ; border : none")
            self.tableWidget.setColumnCount(8)
            self.tableWidget.setRowCount(len(self.data.employ))
            self.tableWidget.setHorizontalHeaderItem( 0 , QTableWidgetItem("Name"))
            self.tableWidget.setHorizontalHeaderItem( 1 , QTableWidgetItem("ID"))
            self.tableWidget.setHorizontalHeaderItem( 2 , QTableWidgetItem("Sex"))
            self.tableWidget.setHorizontalHeaderItem( 3 , QTableWidgetItem("Age"))
            self.tableWidget.setHorizontalHeaderItem( 4 , QTableWidgetItem("Entrance Time"))
            self.tableWidget.setHorizontalHeaderItem( 5 , QTableWidgetItem("Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 6 , QTableWidgetItem("Finished Tasks"))
            self.tableWidget.setHorizontalHeaderItem( 7 , QTableWidgetItem("UnFinished Tasks"))
            self.tableWidget.horizontalHeader().setStyleSheet(" color : black")
            self.tableWidget.verticalHeader().setStyleSheet(" color : black")
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
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

                joinDate = QTableWidgetItem(emploees.joinDate)
                joinDate.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 4 ,joinDate )

                tasks = QTableWidgetItem(emploees.tasks)
                tasks.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 5 ,tasks )

                finishedTasks = QTableWidgetItem(emploees.finishedTasks)
                finishedTasks.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 6 , finishedTasks )

                unfinishedTasks = QTableWidgetItem(emploees.unfinishedTasks)
                unfinishedTasks.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 7 ,unfinishedTasks )
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
        self.addbutton.show()
        self.taskButton.hide()
        self.employeeButton.hide()
        self.MainText.setText("Tasks Section")
        self.MainText.setStyleSheet("color : white; border : none")
        self.MainText.setAlignment(Qt.AlignCenter)
        if (len(self.data.task) != 0) :
            self.tableWidget.show()
            self.emptyText.hide()
            self.emptyText2.hide()
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : black ;border : none")
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setRowCount(len(self.data.task))
            self.tableWidget.setHorizontalHeaderItem( 0 , QTableWidgetItem("Name"))
            self.tableWidget.setHorizontalHeaderItem( 1 , QTableWidgetItem("Started Time"))
            self.tableWidget.setHorizontalHeaderItem( 2 , QTableWidgetItem("Deadline"))
            self.tableWidget.setHorizontalHeaderItem( 3 , QTableWidgetItem("Importance"))
            self.tableWidget.setHorizontalHeaderItem( 4 , QTableWidgetItem("Milestone"))
            self.tableWidget.setHorizontalHeaderItem( 5 , QTableWidgetItem("Persons"))
            self.tableWidget.horizontalHeader().setStyleSheet(" color : black")
            self.tableWidget.verticalHeader().setStyleSheet(" color : black")
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.verticalHeader().setDefaultSectionSize(85)
            i = 0
            for emploees in self.data.employ :
                name = QTableWidgetItem(emploees.name)
                name.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 0 ,name )

                id = QTableWidgetItem(str(emploees.startedTime))
                id.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 1 ,id )

                sex = QTableWidgetItem(emploees.deadline)
                sex.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 2 ,sex )

                age = QTableWidgetItem(str(emploees.importance))
                age.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 3 ,age )

                joinDate = QTableWidgetItem(emploees.milestone)
                joinDate.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 4 ,joinDate )

                tasks = QTableWidgetItem(emploees.persons)
                tasks.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 5 ,tasks )
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
            self.w = EmployeeWindow(self)
            self.w.show()
        elif(self.addSignal == "task"):
            self.w = TaskWindow(self)
            self.w.show()
        else :
            return

class EmployeeWindow (QMainWindow , Employee):
    def __init__(self , MainWindow):
        super(EmployeeWindow, self).__init__()
        self.setupUi(self)
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
        self.CanclepushButton.setStyleSheet("background-color : #ff0000 ; color : white")
        self.SubmitpushButton.setStyleSheet("background-color : #00ff00 ; color : white")
        self.AlertText_1.setStyleSheet("border : none ; color : red")
        self.AlertText_2.setStyleSheet("border : none ; color : red")
        self.AlertText_3.setStyleSheet("border : none ; color : red")
        self.AlertText_4.setStyleSheet("border : none ; color : red")
        self.AlertText_5.setStyleSheet("border : none ; color : red")
        self.AlertText_6.setStyleSheet("border : none ; color : red")
        ####################################################################################################
        self.NameEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.IDspinBox.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.AgespinBox.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.dateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.TasksEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.FinishedTasksEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.UnfinishedTasksEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
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

        # mehdi injaro bekhon Bara to zadam ino
        #self.MainWindow.data.addEmployee("sina" , 11000000 , "male" , 18 , "kjkdjsd" , "jhjkhd" , "djhfkhf" , "jshkahsjdasd")
        #self.MainWindow.employ()
        ####################################################################################################
        #def send_data(self) :
        #    self.close()

        def close(self) :
            self.close()

class TaskWindow (QMainWindow , Tasks):
    def __init__(self , MainWindow):
        super(TaskWindow, self).__init__()
        self.setupUi(self)
        self.MainWindow = MainWindow
        ####################################################################################################
        self.MainText.setStyleSheet("color : white ; border : none")
        self.NameText.setStyleSheet("color : white ; border : none")
        self.StartedTimeText.setStyleSheet("color : white ; border : none")
        self.DeadLineText.setStyleSheet("color : white ; border : none")
        self.ImportanceText.setStyleSheet("color : white ; border : none")
        self.MilestoneText.setStyleSheet("color : white ; border : none")
        self.PersonsText.setStyleSheet("color : white ; border : none")
        self.CanclepushButton.setStyleSheet("background-color : #ff0000 ; color : white")
        self.SubmitpushButton.setStyleSheet("background-color : #00ff00 ; color : white")
        self.AlertText_1.setStyleSheet("border : none ; color : red")
        self.AlertText_2.setStyleSheet("border : none ; color : red")
        self.AlertText_3.setStyleSheet("border : none ; color : red")
        self.AlertText_4.setStyleSheet("border : none ; color : red")
        self.AlertText_5.setStyleSheet("border : none ; color : red")
        self.AlertText_6.setStyleSheet("border : none ; color : red")
        ####################################################################################################
        self.NameEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.StartedTimedateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.DeadLinedateEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.ImportanceEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.MilestoneEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
        self.PersonsEdit.setStyleSheet("background-color : #54485b ; color : white ; border : none")
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

        self.DeadLinedateEdit.setDisplayFormat("MMMM dd yyyy") 
        x = datetime.datetime.now()
        self.DeadLinedateEdit.setDate(QDate(x.year , x.month , x.day))
        self.DeadLinedateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none")
        self.DeadLinedateEdit.setCalendarWidget(y)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
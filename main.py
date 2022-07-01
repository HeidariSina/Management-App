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
        self.employeeButton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 20px")
        self.taskButton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 20px")
        self.backButton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 10px")
        self.addbutton.setStyleSheet("background-color : #1a161c ; color : white ; border-radius : 10px")
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
            self.tableWidget.setStyleSheet("background-color : #1a161c ; color : white ;border : none ; ")
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
            for tasks in self.data.task :
                name = QTableWidgetItem(tasks.name)
                name.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 0 ,name )

                id = QTableWidgetItem(str(tasks.startedTime))
                id.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 1 ,id )

                sex = QTableWidgetItem(tasks.deadline)
                sex.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 2 ,sex )

                age = QTableWidgetItem(str(tasks.importance))
                age.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 3 ,age )

                joinDate = QTableWidgetItem(tasks.milestone)
                joinDate.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 4 ,joinDate )

                person = QTableWidgetItem(tasks.persons)
                person.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(i , 5 ,person )
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
            self.w = EmployeeWindow(self , "none")
            self.w.show()
        elif(self.addSignal == "task"):
            self.w = TaskWindow(self , "none")
            self.w.show()
        else :
            return
    def deleteTask(self , index) :
        self.data.task.pop(index)
        self.task()
    def deleteEmployee(self , index) :
        self.data.employ.pop(index)
        self.employ()
    def editTask(self , index) :
        self.w = EmployeeWindow(self , index)
        self.w.show()
    def editEmployee(self , index) :
        self.w = TaskWindow(self , index)
        self.w.show()
    
class EmployeeWindow (QMainWindow , Employee):
    def __init__(self , MainWindow , inde):
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
        self.dateEdit.setDisplayFormat("MMMM dd yyyy") 
        x = datetime.datetime.now()
        self.dateEdit.setDate(QDate(x.year , x.month , x.day))
        self.dateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none")
        self.dateEdit.setCalendarWidget(y)
        self.CanclepushButton.clicked.connect(self.close)
        self.SubmitpushButton.clicked.connect(self.submit)
        self.SubmitpushButton.setStyleSheet("background-color : #034a21 ; color : white ; border-radius : 10px")
        self.CanclepushButton.setStyleSheet("background-color : #91070f ; color : white ; border-radius : 10px")
        if (inde != "none") :  
            self.NameEdit.setValue(MainWindow.data.employ[inde].name)
            self.IDspinBox.setValue(MainWindow.data.employ[inde].ID)
            self.AgespinBox.setValue(MainWindow.data.employ[inde].age)
            self.dateEdit.setValue(MainWindow.data.employ[inde].age)
            self.TasksEdit.setValue(MainWindow.data.employ[inde].tasks)
            self.FinishedTasksEdit.setValue(MainWindow.data.employ[inde].finishedTasks)
            self.UnfinishedTasksEdit.setValue(MainWindow.data.employ[inde].unfinishedTasks)
            if (MainWindow.data.employ[inde].sex == "Male") :
                self.MaleradioButton.setChecked()
            else :
                self.FemaleradioButton.setChecked()

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
            self.MainWindow.data.addEmployee(self.NameEdit.text() , self.IDspinBox.value() , self.sex , self.AgespinBox.value() , self.dateEdit.text() , self.TasksEdit.text() , self.FinishedTasksEdit.text() , self.UnfinishedTasksEdit.text())
            self.MainWindow.employ()
            self.close()
    def exi(self):
            self.close()

class TaskWindow (QMainWindow , Tasks):
    def __init__(self , MainWindow , inde):
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
        self.SubmitpushButton.setStyleSheet("background-color : #034a21 ; color : white ; border-radius : 10px")
        self.CanclepushButton.setStyleSheet("background-color : #91070f ; color : white ; border-radius : 10px")

        self.DeadLinedateEdit.setDisplayFormat("MMMM dd yyyy") 
        x = datetime.datetime.now()
        self.DeadLinedateEdit.setDate(QDate(x.year , x.month , x.day))
        self.DeadLinedateEdit.setCalendarPopup(1)
        y = QCalendarWidget()
        y.setStyleSheet("background-color : #54485b ; color : black ; border : none ")
        self.DeadLinedateEdit.setCalendarWidget(y)
        self.CanclepushButton.clicked.connect(self.close)
        self.SubmitpushButton.clicked.connect(self.submit)

        if (inde != "none") :  
            self.NameEdit.setValue(MainWindow.data.task[inde].name)
            self.StartedTimedateEdit.setValue(MainWindow.data.task[inde].startedTime)
            self.DeadLinedateEdit.setValue(MainWindow.data.task[inde].deadline)
            self.ImportanceEdit.setValue(MainWindow.data.task[inde].importance)
            self.MilestoneEdit.setValue(MainWindow.data.task[inde].milestone)
            self.PersonsEdit.setValue(MainWindow.data.task[inde].persons)

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
            self.MainWindow.data.addTask(self.NameEdit.text() , self.StartedTimedateEdit.text(), self.DeadLinedateEdit.text() , self.ImportanceEdit.text() , self.MilestoneEdit.text() , self.PersonsEdit.text())
            self.MainWindow.task()
            self.close()
    def exi(self):
            self.close()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
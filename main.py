import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from mainwindow1 import Ui_mainwindow
from detectdia import Diabetes

class MainWindow(QMainWindow,Ui_mainwindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainwindow()
        self.ui.setupUi(self)
        self.detect=Diabetes()
        self.ui.pushButton.clicked.connect(self.on_click)
        self.ui.label_10.setOpenExternalLinks(True)


    def on_click(self):
        self.age = str(self.ui.lineEdit.text())
        self.bmi= str(self.ui.lineEdit_2.text())
        self.dpf= str(self.ui.lineEdit_3.text())
        self.insulin= str(self.ui.lineEdit_4.text())
        self.st= str(self.ui.lineEdit_5.text())
        self.bp= str(self.ui.lineEdit_6.text())
        self.g= str(self.ui.lineEdit_7.text())
        self.preg= str(self.ui.lineEdit_8.text())
        self.age=int(self.age)
        self.bmi=float(self.bmi)
        self.dpf=float(self.dpf)
        self.insulin=int(self.insulin)
        self.st=int(self.st)
        self.bp=int(self.bp)
        self.g=int(self.g)
        self.preg=int(self.preg)

        flag = self.detect.find(self.age,self.bmi,self.dpf,self.insulin,self.st,self.bp,self.g,self.preg)
        if flag==1:
            self.ui.label_9.setText("Person is Diabetic")
        else:
            self.ui.label_9.setText("Person is not Diabetic")



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

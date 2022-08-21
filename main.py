from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(239, 172)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Api = QtWidgets.QLineEdit(self.centralwidget)
        self.Api.setGeometry(QtCore.QRect(20, 30, 120, 20))
        self.Api.setObjectName("Api")
        self.Phone = QtWidgets.QLineEdit(self.centralwidget)
        self.Phone.setGeometry(QtCore.QRect(20, 80, 120, 20))
        self.Phone.setObjectName("Phone")
        self.Hash = QtWidgets.QLineEdit(self.centralwidget)
        self.Hash.setGeometry(QtCore.QRect(20, 130, 196, 20))
        self.Hash.setObjectName("Hash")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(147, 27, 70, 100))
        self.Login.setObjectName("Login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 15, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 65, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 115, 56, 12))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Login.clicked.connect(MainWindow.loginChk) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Api"))
        self.label_2.setText(_translate("MainWindow", "(+82)Phone"))
        self.label_3.setText(_translate("MainWindow", "Hash"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(694, 599)
        self.time_btn_5m = QtWidgets.QRadioButton(Form)
        self.time_btn_5m.setGeometry(QtCore.QRect(438, 500, 51, 16))
        self.time_btn_5m.setObjectName("time_btn_5m")
        self.time_btn_10m = QtWidgets.QRadioButton(Form)
        self.time_btn_10m.setGeometry(QtCore.QRect(481, 500, 51, 16))
        self.time_btn_10m.setObjectName("time_btn10m")
        self.time_btn_30m = QtWidgets.QRadioButton(Form)
        self.time_btn_30m.setGeometry(QtCore.QRect(530, 500, 51, 16))
        self.time_btn_30m.setObjectName("time_btn_30m")
        self.time_btn_1h = QtWidgets.QRadioButton(Form)
        self.time_btn_1h.setGeometry(QtCore.QRect(584, 498, 51, 20))
        self.time_btn_1h.setObjectName("time_btn_1h")
        self.Start = QtWidgets.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(446, 540, 110, 41))
        self.Start.setObjectName("Start")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(436, 20, 241, 20))
        self.label.setObjectName("label")
        self.Text = QtWidgets.QTextEdit(Form)
        self.Text.setGeometry(QtCore.QRect(437, 50, 241, 410))
        self.Text.setObjectName("Text")
        self.Stop = QtWidgets.QPushButton(Form)
        self.Stop.setGeometry(QtCore.QRect(566, 540, 110, 41))
        self.Stop.setObjectName("Stop")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(436, 465, 241, 16))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(21, 20, 400, 16))
        self.label_5.setObjectName("label_5")
        self.time_btn_3h = QtWidgets.QRadioButton(Form)
        self.time_btn_3h.setGeometry(QtCore.QRect(640, 500, 51, 16))
        self.time_btn_3h.setObjectName("time_btn_3h")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(604, 16, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(15, 50, 411, 541))
        self.listView.setObjectName("listView")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 16, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.time_btn_5m.clicked.connect(Form.setCycle) # type: ignore
        self.time_btn_10m.clicked.connect(Form.setCycle) # type: ignore
        self.time_btn_30m.clicked.connect(Form.setCycle) # type: ignore
        self.time_btn_1h.clicked.connect(Form.setCycle) # type: ignore
        self.time_btn_3h.clicked.connect(Form.setCycle) # type: ignore
        self.Start.clicked.connect(Form.startChk) # type: ignore
        self.Stop.clicked.connect(Form.stopChk) # type: ignore
        self.pushButton.clicked.connect(Form.logoutChk) # type: ignore
        self.pushButton_2.clicked.connect(Form.groupChk) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.time_btn_5m.setText(_translate("Form", "5분"))
        self.time_btn_10m.setText(_translate("Form", "10분"))
        self.time_btn_30m.setText(_translate("Form", "30분"))
        self.time_btn_1h.setText(_translate("Form", "1시간"))
        self.Start.setText(_translate("Form", "홍보시작"))
        self.label.setText(_translate("Form", "                        홍보문구"))
        self.Stop.setText(_translate("Form", "홍보중지"))
        self.label_2.setText(_translate("Form", "                      시간 타이머"))
        self.label_5.setText(_translate("Form", "                                   텔레그램 그룹 상태창"))
        self.time_btn_3h.setText(_translate("Form", "3시간"))
        self.pushButton.setText(_translate("Form", "Logout"))
        self.pushButton_2.setText(_translate("Form", "Group list"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
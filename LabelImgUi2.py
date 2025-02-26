# Form implementation generated from reading ui file 'LabelImg_ui2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 709)
        MainWindow.setMinimumSize(QtCore.QSize(600, 700))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 10, 602, 654))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_image = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QtCore.QSize(600, 600))
        self.label_image.setMaximumSize(QtCore.QSize(600, 600))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("SELECT_DIRECTORY.png"))
        self.label_image.setScaledContents(False)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.label_imageName = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_imageName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_imageName.setObjectName("label_imageName")
        self.verticalLayout.addWidget(self.label_imageName)
        self.pushButton_next = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.verticalLayout.addWidget(self.pushButton_next)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 621, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open_directory = QtGui.QAction(parent=MainWindow)
        self.action_open_directory.setObjectName("action_open_directory")
        self.menu.addAction(self.action_open_directory)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LabelImg"))
        self.label_imageName.setText(_translate("MainWindow", "Image name"))
        self.pushButton_next.setText(_translate("MainWindow", "Next"))
        self.menu.setTitle(_translate("MainWindow", "Directory"))
        self.action_open_directory.setText(_translate("MainWindow", "Open directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

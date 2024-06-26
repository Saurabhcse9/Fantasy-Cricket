# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'no_team.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NO_TEAM(object):
    def setupUi(self, NO_TEAM):
        NO_TEAM.setObjectName("NO_TEAM")
        NO_TEAM.resize(463, 163)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NO_TEAM.setWindowIcon(icon)
        NO_TEAM.setWindowOpacity(0.8)
        self.verticalLayout = QtWidgets.QVBoxLayout(NO_TEAM)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(NO_TEAM)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(150, 0, 351, 149))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Team_Name_Edit = QtWidgets.QLineEdit(self.frame_2)
        self.Team_Name_Edit.setGeometry(QtCore.QRect(40, 40, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.Team_Name_Edit.setFont(font)
        self.Team_Name_Edit.setStyleSheet("color: rgb(85, 170, 255);")
        self.Team_Name_Edit.setText("")
        self.Team_Name_Edit.setObjectName("Team_Name_Edit")
        self.OK_PB = QtWidgets.QPushButton(self.frame_2)
        self.OK_PB.setEnabled(True)
        self.OK_PB.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.OK_PB.setAutoFillBackground(False)
        self.OK_PB.setStyleSheet("font: 75 9pt \"Comic Sans MS\";")
        self.OK_PB.setObjectName("OK_PB")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(0, 20, 201, 121))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("pics/Logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.NO_TEAM_LB = QtWidgets.QLabel(self.frame)
        self.NO_TEAM_LB.setGeometry(QtCore.QRect(100, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.NO_TEAM_LB.setFont(font)
        self.NO_TEAM_LB.setObjectName("NO_TEAM_LB")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NO_TEAM)
        QtCore.QMetaObject.connectSlotsByName(NO_TEAM)

    def retranslateUi(self, NO_TEAM):
        _translate = QtCore.QCoreApplication.translate
        NO_TEAM.setWindowTitle(_translate("NO_TEAM", "CricP"))
        self.OK_PB.setText(_translate("NO_TEAM", "OK"))
        self.NO_TEAM_LB.setText(_translate("NO_TEAM", "Team Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NO_TEAM = QtWidgets.QDialog()
    ui = Ui_NO_TEAM()
    ui.setupUi(NO_TEAM)
    NO_TEAM.show()
    sys.exit(app.exec_())

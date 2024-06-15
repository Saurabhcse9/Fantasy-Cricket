# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'party.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Party(object):
    def setupUi(self, Party):
        Party.setObjectName("Party")
        Party.resize(488, 239)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pics/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Party.setWindowIcon(icon)
        Party.setWindowOpacity(0.8)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Party)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Party)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Tropy = QtWidgets.QLabel(self.frame)
        self.Tropy.setGeometry(QtCore.QRect(20, 20, 201, 181))
        self.Tropy.setText("")
        self.Tropy.setPixmap(QtGui.QPixmap("pics/Won.png"))
        self.Tropy.setScaledContents(True)
        self.Tropy.setObjectName("Tropy")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Party)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 60, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(Party)
        QtCore.QMetaObject.connectSlotsByName(Party)

    def retranslateUi(self, Party):
        _translate = QtCore.QCoreApplication.translate
        Party.setWindowTitle(_translate("Party", "Party!!!"))
        self.label.setText(_translate("Party", " Highest Score"))
        self.label_2.setText(_translate("Party", " Congratulations!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Party = QtWidgets.QDialog()
    ui = Ui_Party()
    ui.setupUi(Party)
    Party.show()
    sys.exit(app.exec_())

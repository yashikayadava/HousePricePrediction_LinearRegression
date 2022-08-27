# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'houseprice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 376)
        Form.setStyleSheet("background-color: rgb(200, 188, 192);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 291, 31))
        self.label.setStyleSheet("font: 75 18pt \"Script MT Bold\";\n"
"text-decoration: underline;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 51, 16))
        self.label_2.setStyleSheet("font: italic 14pt \"Monotype Corsiva\";")
        self.label_2.setObjectName("label_2")
        self.area = QtWidgets.QLineEdit(Form)
        self.area.setGeometry(QtCore.QRect(160, 110, 201, 31))
        self.area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.area.setObjectName("area")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 93, 28))
        self.pushButton.setStyleSheet("font: 81 8pt \"Rockwell Extra Bold\";\n"
"background-color: rgb(255, 193, 185);")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 55, 16))
        self.label_3.setStyleSheet("font: 57 12pt \"Dubai Medium\";")
        self.label_3.setObjectName("label_3")
        self.price = QtWidgets.QLabel(Form)
        self.price.setGeometry(QtCore.QRect(120, 290, 201, 21))
        self.price.setStyleSheet("font: 75 14pt \"MS Serif\";")
        self.price.setText("")
        self.price.setObjectName("price")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "House Price Prediction_Linear Regression"))
        self.label.setText(_translate("Form", "House Price Prediction"))
        self.label_2.setText(_translate("Form", "Area :"))
        self.pushButton.setText(_translate("Form", "Predict"))
        self.label_3.setText(_translate("Form", "Price :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

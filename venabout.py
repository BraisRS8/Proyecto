# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venabout.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venabout(object):
    def setupUi(self, venabout):
        venabout.setObjectName("venabout")
        venabout.resize(300, 200)
        venabout.setMinimumSize(QtCore.QSize(300, 200))
        venabout.setMaximumSize(QtCore.QSize(300, 200))
        venabout.setBaseSize(QtCore.QSize(400, 200))
        self.gridLayout = QtWidgets.QGridLayout(venabout)
        self.gridLayout.setObjectName("gridLayout")
        self.btnBox = QtWidgets.QDialogButtonBox(venabout)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.btnBox.setCenterButtons(True)
        self.btnBox.setObjectName("btnBox")
        self.gridLayout.addWidget(self.btnBox, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblNombre = QtWidgets.QLabel(venabout)
        self.lblNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNombre.setObjectName("lblNombre")
        self.gridLayout_2.addWidget(self.lblNombre, 3, 0, 1, 1)
        self.lblVersion = QtWidgets.QLabel(venabout)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName("lblVersion")
        self.gridLayout_2.addWidget(self.lblVersion, 2, 0, 1, 1)
        self.lblLogo = QtWidgets.QLabel(venabout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLogo.sizePolicy().hasHeightForWidth())
        self.lblLogo.setSizePolicy(sizePolicy)
        self.lblLogo.setMinimumSize(QtCore.QSize(0, 0))
        self.lblLogo.setMaximumSize(QtCore.QSize(100, 100))
        self.lblLogo.setBaseSize(QtCore.QSize(0, 0))
        self.lblLogo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblLogo.setText("")
        self.lblLogo.setTextFormat(QtCore.Qt.AutoText)
        self.lblLogo.setPixmap(QtGui.QPixmap("img/logo.jpg"))
        self.lblLogo.setScaledContents(True)
        self.lblLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLogo.setObjectName("lblLogo")
        self.gridLayout_2.addWidget(self.lblLogo, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(venabout)
        self.btnBox.accepted.connect(venabout.accept)
        self.btnBox.rejected.connect(venabout.reject)
        QtCore.QMetaObject.connectSlotsByName(venabout)

    def retranslateUi(self, venabout):
        _translate = QtCore.QCoreApplication.translate
        venabout.setWindowTitle(_translate("venabout", "About"))
        self.lblNombre.setText(_translate("venabout", "Brais Rodríguez Soliño"))
        self.lblVersion.setText(_translate("venabout", "Versión del programa: 0.0.1"))

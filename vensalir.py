from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venSalir(object):
    def setupUi(self, venSalir):
        venSalir.setObjectName("venSalir")
        venSalir.setWindowModality(QtCore.Qt.WindowModal)
        venSalir.resize(373, 166)
        self.btnBox = QtWidgets.QDialogButtonBox(venSalir)
        self.btnBox.setGeometry(QtCore.QRect(90, 110, 191, 32))
        self.btnBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBox.setCenterButtons(True)
        self.btnBox.setObjectName("btnBox")
        self.lblMensaje = QtWidgets.QLabel(venSalir)
        self.lblMensaje.setGeometry(QtCore.QRect(130, 40, 221, 41))
        self.lblMensaje.setObjectName("lblMensaje")
        self.lblImgSalir = QtWidgets.QLabel(venSalir)
        self.lblImgSalir.setGeometry(QtCore.QRect(50, 30, 61, 61))
        self.lblImgSalir.setText("")
        self.lblImgSalir.setPixmap(QtGui.QPixmap("img/Warning-1.png"))
        self.lblImgSalir.setScaledContents(True)
        self.lblImgSalir.setObjectName("lblImgSalir")

        self.retranslateUi(venSalir)
        self.btnBox.accepted.connect(venSalir.accept)
        self.btnBox.rejected.connect(venSalir.reject)
        QtCore.QMetaObject.connectSlotsByName(venSalir)

    def retranslateUi(self, venSalir):
        _translate = QtCore.QCoreApplication.translate
        venSalir.setWindowTitle(_translate("venSalir", "Desea salir?"))
        self.lblMensaje.setText(_translate("venSalir", "¿Está seguro que desea salir de la aplicación?"))
import avisosalir_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VenPrincipal(object):
    def setupUi(self, VenPrincipal):
        VenPrincipal.setObjectName("VenPrincipal")
        VenPrincipal.resize(1258, 926)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VenPrincipal.sizePolicy().hasHeightForWidth())
        VenPrincipal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        VenPrincipal.setFont(font)
        VenPrincipal.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(VenPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_clientes = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_clientes.sizePolicy().hasHeightForWidth())
        self.lbl_clientes.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(219, 201, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.lbl_clientes.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(28)
        self.lbl_clientes.setFont(font)
        self.lbl_clientes.setStyleSheet("background-color: rgb(219, 201, 255);\n"
"")
        self.lbl_clientes.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_clientes.setObjectName("lbl_clientes")
        self.gridLayout_2.addWidget(self.lbl_clientes, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 754, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(1075, 650))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.panelCli = QtWidgets.QWidget()
        self.panelCli.setObjectName("panelCli")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.panelCli)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridFormuDF = QtWidgets.QGridLayout()
        self.gridFormuDF.setObjectName("gridFormuDF")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridFormuDF.addItem(spacerItem2, 0, 7, 1, 1)
        self.btnCalendar = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCalendar.sizePolicy().hasHeightForWidth())
        self.btnCalendar.setSizePolicy(sizePolicy)
        self.btnCalendar.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(32, 32))
        self.btnCalendar.setObjectName("btnCalendar")
        self.gridFormuDF.addWidget(self.btnCalendar, 0, 10, 1, 1)
        self.lblValidar = QtWidgets.QLabel(self.panelCli)
        self.lblValidar.setMinimumSize(QtCore.QSize(32, 32))
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.gridFormuDF.addWidget(self.lblValidar, 0, 4, 1, 1)
        self.lblFecha = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFecha.sizePolicy().hasHeightForWidth())
        self.lblFecha.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblFecha.setFont(font)
        self.lblFecha.setObjectName("lblFecha")
        self.gridFormuDF.addWidget(self.lblFecha, 0, 8, 1, 1)
        self.lblDNI = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDNI.sizePolicy().hasHeightForWidth())
        self.lblDNI.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.gridFormuDF.addWidget(self.lblDNI, 0, 2, 1, 1)
        self.editDni = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDni.sizePolicy().hasHeightForWidth())
        self.editDni.setSizePolicy(sizePolicy)
        self.editDni.setStyleSheet("background-color: rgb(242, 231, 255);")
        self.editDni.setMaxLength(9)
        self.editDni.setObjectName("editDni")
        self.gridFormuDF.addWidget(self.editDni, 0, 3, 1, 1)
        self.editClialta = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editClialta.sizePolicy().hasHeightForWidth())
        self.editClialta.setSizePolicy(sizePolicy)
        self.editClialta.setStyleSheet("background-color: rgb(242, 231, 255);")
        self.editClialta.setObjectName("editClialta")
        self.gridFormuDF.addWidget(self.editClialta, 0, 9, 1, 1)
        self.lblCodcli = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCodcli.sizePolicy().hasHeightForWidth())
        self.lblCodcli.setSizePolicy(sizePolicy)
        self.lblCodcli.setMinimumSize(QtCore.QSize(60, 0))
        self.lblCodcli.setStyleSheet("background-color: rgb(255, 255, 231);")
        self.lblCodcli.setText("")
        self.lblCodcli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCodcli.setObjectName("lblCodcli")
        self.gridFormuDF.addWidget(self.lblCodcli, 0, 1, 1, 1)
        self.btnSearchCli = QtWidgets.QPushButton(self.panelCli)
        self.btnSearchCli.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearchCli.setIcon(icon1)
        self.btnSearchCli.setIconSize(QtCore.QSize(24, 24))
        self.btnSearchCli.setObjectName("btnSearchCli")
        self.gridFormuDF.addWidget(self.btnSearchCli, 0, 5, 1, 1)
        self.btnReloadCli = QtWidgets.QPushButton(self.panelCli)
        self.btnReloadCli.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/recarga.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnReloadCli.setIcon(icon2)
        self.btnReloadCli.setIconSize(QtCore.QSize(24, 24))
        self.btnReloadCli.setObjectName("btnReloadCli")
        self.gridFormuDF.addWidget(self.btnReloadCli, 0, 6, 1, 1)
        self.gridLayout_7.addLayout(self.gridFormuDF, 0, 0, 1, 1)
        self.gridFormuAN = QtWidgets.QGridLayout()
        self.gridFormuAN.setObjectName("gridFormuAN")
        self.lblApel = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblApel.sizePolicy().hasHeightForWidth())
        self.lblApel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.gridFormuAN.addWidget(self.lblApel, 0, 0, 1, 1)
        self.editNome = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editNome.sizePolicy().hasHeightForWidth())
        self.editNome.setSizePolicy(sizePolicy)
        self.editNome.setStyleSheet("background-color: rgb(220, 255, 255);\n"
"background-color: rgb(242, 231, 255);")
        self.editNome.setMaxLength(20)
        self.editNome.setObjectName("editNome")
        self.gridFormuAN.addWidget(self.editNome, 0, 5, 1, 1)
        self.lblNome = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblNome.sizePolicy().hasHeightForWidth())
        self.lblNome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.gridFormuAN.addWidget(self.lblNome, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormuAN.addItem(spacerItem3, 0, 3, 1, 1)
        self.editApel = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editApel.sizePolicy().hasHeightForWidth())
        self.editApel.setSizePolicy(sizePolicy)
        self.editApel.setStyleSheet("background-color: rgb(242, 231, 255);")
        self.editApel.setObjectName("editApel")
        self.gridFormuAN.addWidget(self.editApel, 0, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridFormuAN, 1, 0, 1, 1)
        self.gridFormuDP = QtWidgets.QGridLayout()
        self.gridFormuDP.setObjectName("gridFormuDP")
        self.cmbProv = QtWidgets.QComboBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setMinimumSize(QtCore.QSize(100, 0))
        self.cmbProv.setObjectName("cmbProv")
        self.gridFormuDP.addWidget(self.cmbProv, 0, 4, 1, 1)
        self.lblDir = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.gridFormuDP.addWidget(self.lblDir, 0, 0, 1, 1)
        self.editDir = QtWidgets.QLineEdit(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDir.sizePolicy().hasHeightForWidth())
        self.editDir.setSizePolicy(sizePolicy)
        self.editDir.setStyleSheet("background-color: rgb(242, 231, 255);")
        self.editDir.setObjectName("editDir")
        self.gridFormuDP.addWidget(self.editDir, 0, 1, 1, 1)
        self.lblProv = QtWidgets.QLabel(self.panelCli)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.gridFormuDP.addWidget(self.lblProv, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormuDP.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridFormuDP, 2, 0, 1, 1)
        self.gridFormuSM = QtWidgets.QGridLayout()
        self.gridFormuSM.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridFormuSM.setObjectName("gridFormuSM")
        self.label = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.gridFormuSM.addWidget(self.label, 0, 3, 1, 1)
        self.chkTrans = QtWidgets.QCheckBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTrans.sizePolicy().hasHeightForWidth())
        self.chkTrans.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chkTrans.setFont(font)
        self.chkTrans.setObjectName("chkTrans")
        self.grpbtnPay = QtWidgets.QButtonGroup(VenPrincipal)
        self.grpbtnPay.setObjectName("grpbtnPay")
        self.grpbtnPay.setExclusive(False)
        self.grpbtnPay.addButton(self.chkTrans)
        self.gridFormuSM.addWidget(self.chkTrans, 0, 9, 1, 1)
        self.chkTar = QtWidgets.QCheckBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTar.sizePolicy().hasHeightForWidth())
        self.chkTar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chkTar.setFont(font)
        self.chkTar.setObjectName("chkTar")
        self.grpbtnPay.addButton(self.chkTar)
        self.gridFormuSM.addWidget(self.chkTar, 0, 8, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridFormuSM.addItem(spacerItem5, 0, 5, 1, 1)
        self.rbtFem = QtWidgets.QRadioButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtFem.sizePolicy().hasHeightForWidth())
        self.rbtFem.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbtFem.setFont(font)
        self.rbtFem.setObjectName("rbtFem")
        self.grpbtnSex = QtWidgets.QButtonGroup(VenPrincipal)
        self.grpbtnSex.setObjectName("grpbtnSex")
        self.grpbtnSex.addButton(self.rbtFem)
        self.gridFormuSM.addWidget(self.rbtFem, 0, 1, 1, 1)
        self.rbtMasc = QtWidgets.QRadioButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbtMasc.sizePolicy().hasHeightForWidth())
        self.rbtMasc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbtMasc.setFont(font)
        self.rbtMasc.setObjectName("rbtMasc")
        self.grpbtnSex.addButton(self.rbtMasc)
        self.gridFormuSM.addWidget(self.rbtMasc, 0, 2, 1, 1)
        self.lblSexo = QtWidgets.QLabel(self.panelCli)
        self.lblSexo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSexo.sizePolicy().hasHeightForWidth())
        self.lblSexo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.gridFormuSM.addWidget(self.lblSexo, 0, 0, 1, 1)
        self.lblPago = QtWidgets.QLabel(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblPago.sizePolicy().hasHeightForWidth())
        self.lblPago.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.gridFormuSM.addWidget(self.lblPago, 0, 6, 1, 1)
        self.chkEfec = QtWidgets.QCheckBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkEfec.sizePolicy().hasHeightForWidth())
        self.chkEfec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.chkEfec.setFont(font)
        self.chkEfec.setObjectName("chkEfec")
        self.grpbtnPay.addButton(self.chkEfec)
        self.gridFormuSM.addWidget(self.chkEfec, 0, 7, 1, 1)
        self.spinEdad = QtWidgets.QSpinBox(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinEdad.sizePolicy().hasHeightForWidth())
        self.spinEdad.setSizePolicy(sizePolicy)
        self.spinEdad.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spinEdad.setFont(font)
        self.spinEdad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinEdad.setObjectName("spinEdad")
        self.gridFormuSM.addWidget(self.spinEdad, 0, 4, 1, 1)
        self.gridLayout_7.addLayout(self.gridFormuSM, 3, 0, 1, 1)
        self.tableCli = QtWidgets.QTableWidget(self.panelCli)
        self.tableCli.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableCli.setAlternatingRowColors(True)
        self.tableCli.setGridStyle(QtCore.Qt.SolidLine)
        self.tableCli.setObjectName("tableCli")
        self.tableCli.setColumnCount(3)
        self.tableCli.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCli.setHorizontalHeaderItem(2, item)
        self.gridLayout_7.addWidget(self.tableCli, 4, 0, 1, 1)
        self.griBoton = QtWidgets.QGridLayout()
        self.griBoton.setContentsMargins(250, -1, 250, -1)
        self.griBoton.setObjectName("griBoton")
        self.btnModifCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnModifCli.sizePolicy().hasHeightForWidth())
        self.btnModifCli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnModifCli.setFont(font)
        self.btnModifCli.setObjectName("btnModifCli")
        self.griBoton.addWidget(self.btnModifCli, 0, 1, 1, 1)
        self.btnBajaCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBajaCli.sizePolicy().hasHeightForWidth())
        self.btnBajaCli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnBajaCli.setFont(font)
        self.btnBajaCli.setObjectName("btnBajaCli")
        self.griBoton.addWidget(self.btnBajaCli, 0, 2, 1, 1)
        self.btnAltaCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAltaCli.sizePolicy().hasHeightForWidth())
        self.btnAltaCli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnAltaCli.setFont(font)
        self.btnAltaCli.setObjectName("btnAltaCli")
        self.griBoton.addWidget(self.btnAltaCli, 0, 0, 1, 1)
        self.btnSalir = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSalir.sizePolicy().hasHeightForWidth())
        self.btnSalir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.griBoton.addWidget(self.btnSalir, 0, 4, 1, 1)
        self.btnLimpiarCli = QtWidgets.QPushButton(self.panelCli)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLimpiarCli.sizePolicy().hasHeightForWidth())
        self.btnLimpiarCli.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnLimpiarCli.setFont(font)
        self.btnLimpiarCli.setObjectName("btnLimpiarCli")
        self.griBoton.addWidget(self.btnLimpiarCli, 0, 3, 1, 1)
        self.gridLayout_7.addLayout(self.griBoton, 5, 0, 1, 1)
        self.tabWidget.addTab(self.panelCli, "")
        self.tabFac = QtWidgets.QWidget()
        self.tabFac.setObjectName("tabFac")
        self.tabWidget.addTab(self.tabFac, "")
        self.tabPro = QtWidgets.QWidget()
        self.tabPro.setObjectName("tabPro")
        self.tabWidget.addTab(self.tabPro, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.lblstatus = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblstatus.sizePolicy().hasHeightForWidth())
        self.lblstatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblstatus.setFont(font)
        self.lblstatus.setStyleSheet("color:rgb(255, 0, 0);\n"
"background-color:rgb(255, 255, 231)")
        self.lblstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblstatus.setObjectName("lblstatus")
        self.gridLayout_2.addWidget(self.lblstatus, 2, 1, 1, 1)
        VenPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VenPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        VenPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VenPrincipal)
        self.statusbar.setObjectName("statusbar")
        VenPrincipal.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(VenPrincipal)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        VenPrincipal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSalir = QtWidgets.QAction(VenPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.actionBackup = QtWidgets.QAction(VenPrincipal)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/backup/backup.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionBackup.setIcon(icon3)
        self.actionBackup.setObjectName("actionBackup")
        self.actionSalirToolbar = QtWidgets.QAction(VenPrincipal)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/salirr.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionSalirToolbar.setIcon(icon4)
        self.actionSalirToolbar.setObjectName("actionSalirToolbar")
        self.toolbarAbrirDir = QtWidgets.QAction(VenPrincipal)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/abrir.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.toolbarAbrirDir.setIcon(icon5)
        self.toolbarAbrirDir.setObjectName("toolbarAbrirDir")
        self.actionAbrir = QtWidgets.QAction(VenPrincipal)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuArchivo.addAction(self.toolbarAbrirDir)
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.toolBar.addAction(self.toolbarAbrirDir)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBackup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSalirToolbar)

        self.retranslateUi(VenPrincipal)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VenPrincipal)

    def retranslateUi(self, VenPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VenPrincipal.setWindowTitle(_translate("VenPrincipal", "MainWindow"))
        self.lbl_clientes.setText(_translate("VenPrincipal", "Xestion de clientes"))
        self.lblFecha.setText(_translate("VenPrincipal", "Fecha alta:"))
        self.lblDNI.setText(_translate("VenPrincipal", "DNI:"))
        self.lblApel.setText(_translate("VenPrincipal", "Apellidos: "))
        self.lblNome.setText(_translate("VenPrincipal", "Nombre:"))
        self.lblDir.setText(_translate("VenPrincipal", "Direccion:"))
        self.lblProv.setText(_translate("VenPrincipal", "Provincia:"))
        self.label.setText(_translate("VenPrincipal", "Edad:"))
        self.chkTrans.setText(_translate("VenPrincipal", "Transferencia"))
        self.chkTar.setText(_translate("VenPrincipal", "Tarjeta"))
        self.rbtFem.setText(_translate("VenPrincipal", "Femenino"))
        self.rbtMasc.setText(_translate("VenPrincipal", "Masculino"))
        self.lblSexo.setText(_translate("VenPrincipal", "Sexo:"))
        self.lblPago.setText(_translate("VenPrincipal", "Metodo de pago:"))
        self.chkEfec.setText(_translate("VenPrincipal", "Efectivo"))
        item = self.tableCli.horizontalHeaderItem(0)
        item.setText(_translate("VenPrincipal", "DNI"))
        item = self.tableCli.horizontalHeaderItem(1)
        item.setText(_translate("VenPrincipal", "Apellidos"))
        item = self.tableCli.horizontalHeaderItem(2)
        item.setText(_translate("VenPrincipal", "Nombre"))
        self.btnModifCli.setText(_translate("VenPrincipal", "Modificar"))
        self.btnBajaCli.setText(_translate("VenPrincipal", "Eliminar"))
        self.btnAltaCli.setText(_translate("VenPrincipal", "Grabar"))
        self.btnSalir.setText(_translate("VenPrincipal", "Salir"))
        self.btnLimpiarCli.setText(_translate("VenPrincipal", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panelCli), _translate("VenPrincipal", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFac), _translate("VenPrincipal", "Facturacion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPro), _translate("VenPrincipal", "Productos"))
        self.lblstatus.setText(_translate("VenPrincipal", "TextLabel"))
        self.menuArchivo.setTitle(_translate("VenPrincipal", "Archivo"))
        self.toolBar.setWindowTitle(_translate("VenPrincipal", "toolBar"))
        self.actionSalir.setText(_translate("VenPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("VenPrincipal", "Ctrl+S"))
        self.actionBackup.setText(_translate("VenPrincipal", "Backup"))
        self.actionBackup.setToolTip(_translate("VenPrincipal", "<html><head/><body><p><img src=\":/backup/backup.png\"/></p></body></html>"))
        self.actionBackup.setShortcut(_translate("VenPrincipal", "Alt+B"))
        self.actionSalirToolbar.setText(_translate("VenPrincipal", "Salir"))
        self.toolbarAbrirDir.setText(_translate("VenPrincipal", "Abrir"))
        self.toolbarAbrirDir.setShortcut(_translate("VenPrincipal", "Ctrl+A"))
        self.actionAbrir.setText(_translate("VenPrincipal", "Abrir"))
import toolbarbackup_rc

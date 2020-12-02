from Ventana import *
from vensalir import *
from vencalendar import *
from venconf import *
from datetime import datetime
import sys, var, events, clients, conexion, locale
from PyQt5.QtPrintSupport import QPrintDialog


locale.setlocale(locale.LC_ALL,'es-ES')

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_venSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        self.setModal(True)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_Calendar()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.calendar.clicked.connect(clients.Clientes.cargarFecha)
        self.setModal(True)

class DialogConf(QtWidgets.QDialog):
    def __init__(self):
        super(DialogConf, self).__init__()
        var.dlgconf = Ui_venconf()
        var.dlgconf.setupUi(self)
        var.dlgconf.btnBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(clients.Clientes.bajaCliente)
        self.setModal(True)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VenPrincipal()
        var.ui.setupUi(self)
        var.dlgsalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.filedlgabrir = FileDialogAbrir()
        var.printdlgabrir = PrintDialogAbrir()
        var.dlgconf = DialogConf()
        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkpago = (var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans)
        '''
        conexion de eventos con los objetos
        estamos conectando el código con la interfaz gráfico
        botones formulario cliente
        '''

        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.editDni.editingFinished.connect(lambda: clients.Clientes.validoDni())
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        var.ui.btnAltaCli.clicked.connect(clients.Clientes.altaCliente)
        var.ui.btnLimpiarCli.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.btnBajaCli.clicked.connect(events.Eventos.Conf)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCliente)
        var.ui.btnReloadCli.clicked.connect(clients.Clientes.reloadCli)
        var.ui.btnSearchCli.clicked.connect(clients.Clientes.searchCli)
        #var.ui.actionBackup.triggered.connect(events.Eventos.backup)
        var.ui.actionSalirToolbar.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarAbrirDir.triggered.connect(events.Eventos.AbrirDir)
        var.ui.toolbarPrint.triggered.connect(events.Eventos.Print)
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)

        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.tableCli.clicked.connect(clients.Clientes.cargarCli)
        var.ui.tableCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        events.Eventos.cargarProv()
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatus, 1)
        var.ui.lblstatus.setText('Bienvenido a 2º DAM    Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))

        '''
        Configuracion del spin de edad
        '''
        var.ui.spinEdad.setMinimum(18)
        var.ui.spinEdad.setMaximum(150)
        var.ui.spinEdad.setValue(18)


        '''
        módulos conexion base datos
        '''

        conexion.Conexion.db_connect(var.filebd)
        # conexion.Conexion()
        conexion.Conexion.mostrarClientes(self)

    def closeEvent(self, event):
        if event:
            events.Eventos.Salir(event)

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
        self.setWindowTitle('Abrir archivo')
        self.setModal(True)

class PrintDialogAbrir(QPrintDialog):
    def __init__(self):
        super(PrintDialogAbrir, self).__init__()
        self.setModal(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


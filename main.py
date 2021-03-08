import printer
from Ventana import *
from venabout import *
from vensalir import *
from vencalendar import *
from venconf import *
from venimp import *
from datetime import datetime
import sys, var, events, clients, conexion, locale, products, bills, backup
from PyQt5.QtPrintSupport import QPrintDialog

#Esto es para que la fecha salga en español
locale.setlocale(locale.LC_ALL,'es-ES')

class DialogSalir(QtWidgets.QDialog):
    """

    Clase que instancia la ventana de aviso salir

    """
    def __init__(self):

        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_venSalir()
        var.dlgsalir.setupUi(self)
        var.dlgsalir.btnBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        self.setModal(True)

class DialogCalendar(QtWidgets.QDialog):
    """

    Clase que instancia la ventana de calendario

    """
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

class DialogCalendar2(QtWidgets.QDialog):
    """

    Clase que instancia la ventana de calendario

    """
    def __init__(self):

        super(DialogCalendar2, self).__init__()
        var.dlgcalendar2 = Ui_Calendar()
        var.dlgcalendar2.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar2.calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar2.calendar.clicked.connect(bills.Facturas.cargarFecha)
        self.setModal(True)

class DialogConf(QtWidgets.QDialog):
    """

    Clase que instancia la ventana avisos

    """
    def __init__(self):

        super(DialogConf, self).__init__()
        var.dlgconf = Ui_venconf()
        var.dlgconf.setupUi(self)
        var.dlgconf.btnBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(clients.Clientes.bajaCliente)
        self.setModal(True)

class DialogImp(QtWidgets.QDialog):
    """

    Clase que instancia la ventana confirmacion de importacion

    """
    def __init__(self):

        super(DialogImp, self).__init__()
        var.dlgimp = Ui_venimp()
        var.dlgimp.setupUi(self)
        var.dlgimp.buttonBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(backup.Backups.cargaDatos)

        self.setModal(True)

class DialogAbout(QtWidgets.QDialog):
    """

    Clase que instancia la ventana de informacion

    """
    def __init__(self):
        super(DialogAbout, self).__init__()
        var.dlgabout = Ui_venabout()
        var.dlgabout.setupUi(self)
        self.setModal(True)

class CmbVenta(QtWidgets.QComboBox):
    def __init__(self):
        super(CmbVenta, self).__init__()
        var.cmbventa = QtWidgets.QComboBox()

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        """

        Clase main. Instancia todas las ventanas del programa.
        Genera y conecta todos los eventos de los botonoes, tablas y otros widgets.
        Cuando se lanza se conecta con la BBDD.
        Cuando se lanza el programa carga todos los articulos, facturas y clientes de
        la BBDD en las tablas correspondientes.

        """
        super(Main, self).__init__()
        """
        
        Instancia de ventanas auxiliares
        
        """
        var.ui = Ui_VenPrincipal()
        var.ui.setupUi(self)
        var.dlgsalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()
        var.filedlgabrir = FileDialogAbrir()
        var.printdlgabrir = PrintDialogAbrir()
        var.dlgconf = DialogConf()
        var.dlgabout = DialogAbout()
        var.dlgcalendar2 = DialogCalendar2()
        var.cmbventa = QtWidgets.QComboBox()
        var.dlgimp = DialogImp()
        '''
        colección de datos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkpago = (var.ui.chkEfec, var.ui.chkTar, var.ui.chkTrans)
        '''
        conexion de eventos con los objetos
        estamos conectando el código con la interfaz gráfico
        botones formulario cliente, productos y facturas
        '''

        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.btnSalirPro.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.editDni.editingFinished.connect(lambda: clients.Clientes.validoDni())
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        var.ui.btnFecha.clicked.connect(bills.Facturas.abrirCalendar)
        var.ui.btnAltaCli.clicked.connect(clients.Clientes.altaCliente)
        var.ui.btnLimpiarCli.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.btnBajaCli.clicked.connect(events.Eventos.Conf)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCliente)
        var.ui.btnReloadCli.clicked.connect(clients.Clientes.reloadCli)
        var.ui.btnSearchCli.clicked.connect(clients.Clientes.searchCli)
        var.ui.actionSalirToolbar.triggered.connect(events.Eventos.Salir)
        var.ui.toolbarAbrirDir.triggered.connect(events.Eventos.AbrirDir)
        var.ui.toolbarPrint.triggered.connect(events.Eventos.Print)
        var.ui.actionAbout.triggered.connect(events.Eventos.About)
        var.ui.actionCrear_Backup.triggered.connect(backup.Backups.crearBackup)
        var.ui.actionBackup.triggered.connect(backup.Backups.restaurarBackup)
        var.ui.actionImportar_datos.triggered.connect(backup.Backups.importarDatos)


        var.ui.btnAltaPro.clicked.connect(products.Productos.altaProducto)
        var.ui.btnModifPro.clicked.connect(products.Productos.modifProducto)
        var.ui.btnBajaPro.clicked.connect(products.Productos.bajaProducto)

        #facturas
        var.ui.btnFactura.clicked.connect(bills.Facturas.altaFactura)
        var.ui.btnBuscar.clicked.connect(conexion.Conexion.mostrarFacturascli)
        var.ui.btnRecarga.clicked.connect(conexion.Conexion.mostrarFacturas)
        var.ui.btnAnular.clicked.connect(bills.Facturas.borrarFactura)
        var.ui.btnAceptarArt.clicked.connect(bills.Facturas.procesoVenta)
        var.ui.btnBorrarArt.clicked.connect(bills.Facturas.anularVenta)

        #informes
        var.ui.actionInforme.triggered.connect(printer.Printer.reportCli)
        var.ui.actionInforme_Productos.triggered.connect(printer.Printer.reportPro)
        var.ui.actionInforme_Facturas.triggered.connect(printer.Printer.reportFac)
        var.ui.actionInforme_Factura_Cliente.triggered.connect(printer.Printer.infFacCli)

        #esto es para hacer las selecciones de checkboxes o radiobuttons y comprobar si hay cambios
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)

        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.tableCli.clicked.connect(clients.Clientes.cargarCli)
        #Esto hace que en vez de seleccionar solo una celda seleccione toda la fila entera
        var.ui.tableCli.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        #Esto carga los valores en el combobox siendo siempre el primero vacio que es la posicion 0 la predeterminada
        events.Eventos.cargarProv(self)
        #Esto sirve para crear el rectangulo de abajo deltodo
        var.ui.statusbar.addPermanentWidget(var.ui.lblstatus, 1)
        var.ui.lblstatus.setText('Bienvenido a 2º DAM           Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        var.ui.tablePro.clicked.connect(products.Productos.cargarPro)
        var.ui.tablePro.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tableFac.clicked.connect(bills.Facturas.cargarFact)
        var.ui.tableFac.clicked.connect(bills.Facturas.mostrarVentasfac)
        var.ui.tableFac.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tableArtFac.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

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
        conexion.Conexion.mostrarProducto(self)
        conexion.Conexion.mostrarFacturas(self)
        var.cmbventa = QtWidgets.QComboBox()

    def closeEvent(self, event):
        if event:
            events.Eventos.Salir(event)

class FileDialogAbrir(QtWidgets.QFileDialog):
    """

    Clase que instancia la ventana de directorio

    """
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
        self.setWindowTitle('Abrir archivo')
        self.setModal(True)

class PrintDialogAbrir(QPrintDialog):
    """

    Clase que instancia la ventana de impresion

    """
    def __init__(self):
        super(PrintDialogAbrir, self).__init__()
        self.setModal(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())


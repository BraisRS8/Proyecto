from Ventana import *
from vensalir import *
from vencalendar import *
from datetime import datetime
import sys, var , events , clients


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisoSalir = Ui_venSalir()
        var.avisoSalir.setupUi(self)
        var.avisoSalir.btnBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_Calendar()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.calendar.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendar.calendar.clicked.connect(clients.Clientes.cargarFecha)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VenPrincipal()
        var.ui.setupUi(self)
        var.avisoSalir = DialogSalir()
        var.dlgcalendar = DialogCalendar()

        QtWidgets.QAction(self).triggered.connect(self.close)

        var.ui.btn_salir.clicked.connect(events.Eventos.Salir)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        var.ui.ent_dni.editingFinished.connect(clients.Clientes.validoDni)

        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)

        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)


        for i in var.rbtsex:
            i.toggled.connect(events.Eventos.selSexo)

        var.chkpago = (var.ui.chkEfec, var.ui.chkTarj, var.ui.chkTrans)

        for i in var.chkpago:
            i.stateChanged.connect(events.Eventos.selPago)

        clients.Clientes.cargarProv()
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)



    def closeEvent(self, event):
        events.Eventos.Salir()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())



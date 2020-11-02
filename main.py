from Ventana import *
from vensalir import *
import sys, var , events , clients

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_VenPrincipal()
        var.ui.setupUi(self)

        var.ui.btn_salir.clicked.connect(events.Eventos.Salir)

        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

        var.ui.ent_dni.editingFinished.connect(clients.Clientes.validoDni)

        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)

        QtWidgets.QAction(self).triggered.connect(self.close)

        for i in var.rbtsex:
            i.toggled.connect(events.Eventos.selSexo)

        var.chkpago = (var.ui.chkEfec, var.ui.chkTarj, var.ui.chkTrans)

        for i in var.chkpago:
            i.stateChanged.connect(events.Eventos.selPago)

        clients.Clientes.cargarProv()
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir,self).__init__()
        var.dialog = Ui_venSalir()
        var.dialog.setupUi(self)
        var.dialog.btnBox.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir())
        var.dialog.btnBox.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
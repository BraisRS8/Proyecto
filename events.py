import var, sys

class Eventos():


        def Salir(event):
            try:
                var.avisoSalir.show()
                if var.avisoSalir.exec_():
                    sys.exit()
                else:
                    var.avisoSalir.close()
                    event.ignore()
            except Exception as error:
                print("Error %s: " % str(error))

        def selSexo():
            try:
                if var.ui.rbtFem.isChecked():
                    var.sex = 'Mujer'
                if var.ui.rbtMasc.isChecked():
                    var.sex = 'Hombre'
            except Exception as error:
                print('Error: %s ' % str(error))

        def selPago():
            try:
                if var.ui.chkEfec.isChecked():
                    var.pay.append("Efectivo")
                if var.ui.chkTarj.isChecked():
                    var.pay.append("Tarjeta")
                if var.ui.chkTrans.isChecked():
                    var.pay.append("Transferencia")
            except Exception as error:
                print('Error: %s ' % str(error))
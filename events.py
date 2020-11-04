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
                    var.ui.lblPrueba.setText('Femenino')
                if var.ui.rbtMasc.isChecked():
                    var.ui.lblPrueba.setText('Masculino')
            except Exception as error:
                print('Error: %s ' % str(error))

        def selPago():
            try:
                if var.ui.chkEfec.isChecked():
                    print('Pagas con efectivo')
                if var.ui.chkTarj.isChecked():
                    print('Pagas con tarjeta')
                if var.ui.chkTrans.isChecked():
                    print('Pagas con transferencia')
            except Exception as error:
                print('Error: %s ' % str(error))
import var
from PyQt5 import QtWidgets

class Clientes():

    def validarDni(dni):

        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni  = dni.replace(dni[0],reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23 ] == dig_control
            return False
        except:
            print('Error módulo validar DNI')
            return None

    def validoDni():

        try:
            dni = var.ui.ent_dni.text()
            print(Clientes.validarDni(dni))
            if Clientes.validarDni(dni):
                var.ui.lblValidar.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValidar.setText('V')
                var.ui.ent_dni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValidar.setText('X')
                var.ui.ent_dni.setText(dni.upper())

        except:
            print('Error módulo escribir valido DNI')
            return None

    def cargarProv():
        try:
            prov = ['','A Coruña','Lugo','Ourense','Pontevedra']
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %s ' & str(error))

    def selProv(prov):
        try:
            global vpro
            vpro = prov
        except Exception as error:
            print('Error: %s ' % str(error))

    def abrirCalendar(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.ent_fecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error: %s ' % str(error))

    def showClients(self):
        try:
            newcli = []
            clitab = []
            client = [var.ui.ent_dni, var.ui.ent_apellidos, var.ui.ent_nombre, var.ui.ent_direccion, var.ui.ent_fecha]
            k = 0
            for i in client:
                newcli.append(i.text())
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)

            var.pay = set(var.pay)
            for j in var.pay:
                newcli.append(j)
            newcli.append(var.sex)
            print(newcli)
            print(clitab)
            row = 0
            column = 0
            var.ui.cliTable.insertRow(row)
            for registro in clitab:
                cell = QtWidgets.QTableWidgetItem(registro)
                var.ui.cliTable.setItem(row,column,cell)
                column += 1
        except Exception as error:
            print('Error: %s ' % str(error))
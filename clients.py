import var

class Clientes():

    def validarDni(dni):

        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'
            dig_ext = 'XYZ'
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni  = dni.replace(dni[0],reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni)%23 ] == dig_control

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
            print('Has seleccionado la provincia de', prov)
            return prov
        except Exception as error:
            print('Error: %s ' % str(error))
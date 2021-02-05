import conexion
import var
from Ventana import *
from datetime import datetime


class Clientes:
    def validarDni(dni):
        """

        Módulo que valida la letra de un dni sea nacional o extranjero

        :param a: dni
        :type: string
        :return: None
        :rtype: bool

        Pone la letra en mayúsculas, comprueba que son nueve caracteres. Toma los ocho primeros,
        si es extrajero cambia la letra por el número, y aplica el algoritmo de comprobación de
        la letra basado en la normativa. Si es correcto devuelve True, si es falso devuelve false.

        """
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
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control

        except:
            print('Error módulo validar DNI')
            return None

    def validoDni():
        """

        Módulo que según este o no verificado el dni, muestra una imagen distinta.

        :return: None

        Si es falso escribe en un label una x roja y si es verdadero una v verde.

        """
        try:
            dni = var.ui.editDni.text()
            if Clientes.validarDni(dni):
                var.ui.lblValidar.setStyleSheet('QLabel {color: green;}')
                var.ui.lblValidar.setText('V')
                var.ui.editDni.setText(dni.upper())
            else:
                var.ui.lblValidar.setStyleSheet('QLabel {color: red;}')
                var.ui.lblValidar.setText('X')
                var.ui.editDni.setText(dni.upper())

        except:
            print('Error módulo escribir valido DNI')
            return None

    def selSexo(self):
        """

        Módulo que segun la opcion checheada en el radioButton Fem o Masc carga el texto
        correspondiente de Mujer o Hombre a la variable var.sex que luego se añade
        a la lista de datos del cliente en la BBDD

        :return: None
        :rtype: None
        """
        try:
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    def selPago():
        """

        Chequea que valores de pago estan seleccionados en el checkbox y los añade
        a una variable lista var.py

        :return: None

        En QtDesigner se debe agrupar los checkbox en un ButtonGroup

        """
        try:
            var.pay = []
            # enumerate sirve para pillar el numero de botones(del grpbtnPay con el .buttons) y luego comprueba si esta marcado y la posicion
            for i, data in enumerate(var.ui.grpbtnPay.buttons()):
                # agrupamos en QtDesigner los checkbox en un ButtonGroup
                if data.isChecked() and i == 0:
                    var.pay.append('Efectivo')
                if data.isChecked() and i == 1:
                    var.pay.append('Tarjeta')
                if data.isChecked() and i == 2:
                    var.pay.append('Transferencia')
            return var.pay
        except Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        """

        Al seleccionar una provincia en el comboBox llama al evento de cmbProv.activated
        que devuelve la provincia seleccionada

        :param a: provincia seleccionada
        :type a: string
        :return: None
        :rtype: None
        """

        try:
            global vpro
            vpro = prov
        except Exception as error:
            print('Error: %s' % str(error))

    def abrirCalendar(self):
        """

        Módulo que abre el widget de Calendario

        :return: None
        :rtype: None
        """
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        """

        Módulo que carga la fecha marcada en el widget Calendar

        :param a: librería python para formateo de fechas
        :return: None
        :rtype: formato de fechas python

        A partir del los eventos Calendar.clicked.connect al clickear en una fecha, captura y la cargar en el widget edit
        en el que almacena la fecha.

        """
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editClialta.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))

    def altaCliente(self):  # SE EJECUTA CON EL BOTÓN ACEPTAR
        """

        Módulo que carga los datos del cliente

        :param a: None
        :param b: None
        :return: None

        Se crea una lista newcli que contendra todos los datos del cliente que se introduzcan en los widgets,
        esta lista se pasa como argumento al módulo altaCli de la clase Conexión.
        El módulo llama a la función mostrarClientes que recarga la tabla con todos los clientes.
        El modulo llama a la función limpiarCli que vacia el contenido de los widgets.

        """

        try:
            newcli = []
            clitab = []
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editClialta, var.ui.editDir]
            k = 0
            for i in client:
                newcli.append(i.text())
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)
            newcli.append(var.sex)
            var.pay2 = Clientes.selPago()
            newcli.append(var.pay2)

            valor = var.ui.spinEdad.value()
            newcli.append(valor)

            if client:
                row = 0
                column = 0
                var.ui.tableCli.insertRow(row)
                for registro in clitab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.tableCli.setItem(row, column, cell)
                    column += 1
                conexion.Conexion.altaCli(newcli)
            else:
                print('Faltan Datos')
            # Clientes.limpiarCli()
        except Exception as error:
            print('Error alta : %s ' % str(error))

    def limpiarCli():
        """

        Modúlo que vacia los widgets de la tabla clientes

        :return: None
        :rtype: None
        """
        try:
            # Coje los editText y con el for hace que se vacie el texto
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editClialta, var.ui.editDir]
            for i in range(len(client)):
                client[i].setText('')
            var.ui.grpbtnSex.setExclusive(False)  # necesario solo para los radiobutton
            for dato in var.rbtsex:
                dato.setChecked(False)
            for data in var.chkpago:
                data.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)  # El index 0 es el vacio que es el predeterminado
            var.ui.lblValidar.setText('')
            var.ui.lblCodcli.setText('')
            var.ui.spinEdad.setValue(18)
        except Exception as error:
            print('Error limpiar widgets: %s ' % str(error))

    def cargarCli():
        """

        Módulo que se activa con el evento clicked.connect y setSelectionBehavior del widget
        tableCli

        :return: None
        :rtype: None

        Al generarse el evento se llama al módulo de Conexión cargarCliente que devuelve los datos
        del cliente seleccionado.

        """
        try:
            fila = var.ui.tableCli.selectedItems()
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome]
            # Esto sirve para guardar en el array de fila cada dato que esta seleccionado en la tabla
            if fila:
                fila = [dato.text() for dato in fila]
            i = 0
            # Esto creo que va poniendo cada valor en su editText
            for i, dato in enumerate(client):
                dato.setText(fila[i])
            conexion.Conexion.cargarCliente()
        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def bajaCliente(self):
        """

        Módulo que da de baja a un cliente a partir del dni. Ademas recarga los datos del widget tablaCli
        con los datos actualizados de la BBDD y limpia los widgets de datos.

        :return: None
        :rtype: None

        Toma el dni cargado en el widget editDni, se lo pasa al módulo bajaCli de la clase Conexión y da de baja
        el cliente.
        Limpia los datos del formulario y recarga la tabla de clientes.

        """
        try:
            # Coge el texto del dni en el editText
            dni = var.ui.editDni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.mostrarClientes(self)
            Clientes.limpiarCli()

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def modifCliente(self):
        """

        A partir del código del cliente, lee los datos de los widgets y modifica en la tabla y en la BBDD
        los datos que se hayan modificado llamando al módulo modifCli de la clase Conexión.
        Recarga la tabla de clientes.

        :return: None
        :rtype: None
        """
        try:
            newdata = []
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editClialta, var.ui.editDir]
            for i in client:
                newdata.append(i.text())  # cargamos los valores que hay en los editline
            newdata.append(var.ui.cmbProv.currentText())
            newdata.append(var.sex)
            var.pay = Clientes.selPago()
            newdata.append(var.pay)
            valor = var.ui.spinEdad.value()
            newdata.append(valor)
            cod = var.ui.lblCodcli.text()
            conexion.Conexion.modifCli(cod, newdata)
            conexion.Conexion.mostrarClientes(self)

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def reloadCli(self):
        """

        Módulo que limpia los widgets de cliente y recarga la tabla de cliente

        :return: None
        :rtype: None
        """
        try:
            Clientes.limpiarCli()
            conexion.Conexion.mostrarClientes(None)
            var.ui.lblstatus.setText('Recarga de la lista finalizado con exito Fecha: ' + str(
                datetime.today().strftime('%A, %d de %B de %Y')))
        except Exception as error:
            print("Error en reload: % " % str(error))

    def searchCli(self):
        """

        Busca un cliente a partir de un dni que escribe el usuario

        :return: None
        :rtype: None

        Toma el dni del widget editDni y llama a la función buscaCli de la clase Conexion.

        """

        try:
            dni = var.ui.editDni.text()
            conexion.Conexion.buscaCli(dni)
        except Exception as error:
            print("Error en la busqueda: % " % str(error))

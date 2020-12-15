import conexion
import var
from Ventana import *
from datetime import datetime
class Clientes():
    '''
    eventos necesarios formulario clientes
    '''
    def validarDni(dni):
        '''
        Código que controla si el dni o nie es correcto
        :return:
        '''
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
        '''
        muestra mensaje de dni válido
        :return: none
        '''
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
        try:
            if var.ui.rbtFem.isChecked():
                var.sex =  'Mujer'
            if var.ui.rbtMasc.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error: %s' % str(error))

    def selPago():
        '''
        chequea que valores de pago han sido activados
        :return: devuelve una lista de valores
        '''
        try:
            var.pay = []
            #enumerate sirve para pillar el numero de botones(del grpbtnPay con el .buttons) y luego comprueba si esta marcado y la posicion
            for i, data in enumerate(var.ui.grpbtnPay.buttons()):
                    #agrupamos en QtDesigner los checkbox en un ButtonGroup
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
        try:
            global vpro
            vpro = prov
        except Exception as error:
            print('Error: %s' % str(error))


    def abrirCalendar(self):
        '''
        Abrir la ventana calendario
        '''
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        ''''
        Este módulo se ejecuta cuando clickeamos en un día del calendar, es decir, clicked.connect de calendar
        '''
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editClialta.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))

    def altaCliente(self):  #SE EJECUTA CON EL BOTÓN ACEPTAR
        '''
        cargará los clientes en la tabla y en la base de datos
        cargará datos cliente en el resto widgets
        en las búsquedas mostrará los datos del cliente
        :return: none
        '''
        #preparamos el registro
        try:
            newcli = [] #contiene todos los datos
            clitab = []  #será lo que carguemos en la tablas
            #Esto son los edits solo que se guardan en un array para luego solo tener que coger el texto con .text()
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editClialta, var.ui.editDir]
            k = 0
            for i in client:
                newcli.append(i.text())  #cargamos los valores que hay en los editline
                #Esto es para guardar los 3 primeros datoe en clitab para luego mostrarlos en las tablas cuando se seleccione en este caso seria editDni, editApel, editNome
                if k < 3:
                    clitab.append(i.text())
                    k += 1
            newcli.append(vpro)
            newcli.append(var.sex)
            var.pay2 = Clientes.selPago()
            newcli.append(var.pay2)
            #Como cojer el valor de un spin
            valor=var.ui.spinEdad.value()
            newcli.append(valor)
            #Si cliente no esta vacio
            if client:
            #comprobarmos que no esté vacío lo principal
            #aquí empieza como trabajar con la TableWidget
            #Inserta una fila vacia con el insertRow en el espacio 0
            # y va metiendo los datos de clitab por orden aumentando la columna
            #NO HACE FALTA CREO HACER ESTO PQ LUEGO VA A MOSTRAR CLIENTE QUE LO HACE DIRECTAMENTE GRACIAS A LA BASE DE DATOS
                row = 0
                column = 0
                var.ui.tableCli.insertRow(row)
                for registro in clitab:
                    cell = QtWidgets.QTableWidgetItem(registro)
                    var.ui.tableCli.setItem(row, column, cell)
                    column +=1
                #Atencion a pasarle el array con el mismo orden de datos que esta en la base de datos
                # para evitar compliaciones a la hora de meterle los valores a la base de datos
                conexion.Conexion.altaCli(newcli)
            else:
                print('Faltan Datos')
            #Clientes.limpiarCli()
        except Exception as error:
            print('Error alta : %s ' % str(error))

    def limpiarCli():
        '''
        limpia los datos del formulario cliente
        :return: none
        '''
        try:
            #Coje los editText y con el for hace que se vacie el texto
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editClialta, var.ui.editDir]
            for i in range(len(client)):
                client[i].setText('')
            var.ui.grpbtnSex.setExclusive(False)  #necesario solo para los radiobutton
            for dato in var.rbtsex:
                dato.setChecked(False)
            for data in var.chkpago:
                data.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0) #El index 0 es el vacio que es el predeterminado
            var.ui.lblValidar.setText('')
            var.ui.lblCodcli.setText('')
            var.ui.spinEdad.setValue(18)
        except Exception as error:
            print('Error limpiar widgets: %s ' % str(error))

    def cargarCli():
        '''
        carga en widgets formulario cliente los datos
        elegidos en la tabla
        :return: none
        '''
        try:
            fila = var.ui.tableCli.selectedItems()
            client = [ var.ui.editDni, var.ui.editApel, var.ui.editNome ]
            #Esto sirve para guardar en el array de fila cada dato que esta seleccionado en la tabla
            if fila:
                fila = [dato.text() for dato in fila]
            i = 0
            #Esto creo que va poniendo cada valor en su editText
            for i, dato in enumerate(client):
                dato.setText(fila[i])
            conexion.Conexion.cargarCliente()
        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def bajaCliente(self):
        '''
        módulos para dar de baja un cliente
        :return:
        '''
        try:
            #Coge el texto del dni en el editText
            dni = var.ui.editDni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.mostrarClientes(self)
            Clientes.limpiarCli()

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))


    def modifCliente(self):
        '''
        módulos para modificar datos de un cliente con determinado código
        :return:
        '''
        try:
            newdata = []
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var.ui.editClialta, var.ui.editDir]
            for i in client:
                newdata.append(i.text())  # cargamos los valores que hay en los editline
            newdata.append(var.ui.cmbProv.currentText())
            newdata.append(var.sex)
            var.pay = Clientes.selPago()
            newdata.append(var.pay)
            valor=var.ui.spinEdad.value()
            newdata.append(valor)
            cod = var.ui.lblCodcli.text()
            conexion.Conexion.modifCli(cod, newdata)
            conexion.Conexion.mostrarClientes(self)

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def reloadCli(self):
        "modulo para el boton de recargar la lista de clientes"

        try:
            Clientes.limpiarCli()
            conexion.Conexion.mostrarClientes(None)
            var.ui.lblstatus.setText('Recarga de la lista finalizado con exito Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        except Exception as error:
            print("Error en reload: % " % str(error))

    def searchCli(self):
        '''
        modulo para el boton de buscar cliente
        :return:
        '''

        try:
            dni = var.ui.editDni.text()
            conexion.Conexion.buscaCli(dni)
        except Exception as error:
            print("Error en la busqueda: % " % str(error))
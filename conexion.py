from PyQt5 import QtWidgets, QtSql
import pymongo, var
from Ventana import *
from datetime import datetime

class Conexion():
    def db_connect(filename):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(filename)
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos','No se puede establecer conexion.\n'
                                            'Haz Click para Cancelar.', QtWidgets.QMessageBox.Cancel)
            return False
        else:
            print('Conexión Establecida')
        return True

    def altaCli(cliente):
        query = QtSql.QSqlQuery()
        query.prepare('insert into clientes (dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formaspago, edad)'
                    'VALUES (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, :formaspago, :edad)')
        #El array empieza en posicion 0 siempre
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        # pagos = ' '.join(cliente[7]) si quiesesemos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formaspago', str(cliente[7]))
        query.bindValue(':edad', int(cliente[8]))
        #Si la query se ejecuta sin errores hace lo siguiente
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Alta Cliente con dni ' + str(cliente[0] + '       Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y'))))
            Conexion.mostrarClientes(super)
        else:
            print("Error: ", query.lastError().text())

    def cargarCliente():
        '''
        Módulo que carga el resto de widgets con los datos del cliente dni
        :return: None
        '''
        dni = var.ui.editDni.text()
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editDniFac.setText(str(query.value(1)))
                var.ui.editApellidoFac.setText(str(query.value(2)))
                #Se salta el 1 2 y 3 pq son los datos que ya estan cargados de antes dni nombre y apellidos
                var.ui.editClialta.setText(query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))
                if str(query.value(7)) == 'Mujer':
                    var.ui.rbtFem.setChecked(True)
                    var.ui.rbtMasc.setChecked(False)
                else:
                    var.ui.rbtMasc.setChecked(True)
                    var.ui.rbtFem.setChecked(False)
                #Primero descheckea todos los pago y luego va comprobando cuales estan en la base de datos
                for data in var.chkpago:
                    data.setChecked(False)
                if 'Efectivo' in query.value(8):
                    var.chkpago[0].setChecked(True)
                if 'Tarjeta' in query.value(8):
                    var.chkpago[1].setChecked(True)
                if 'Transferencia' in query.value(8):
                    var.chkpago[2].setChecked(True)
                var.ui.spinEdad.setValue(int(query.value(9)))
    def mostrarClientes(self):
        '''
        Carga los datos principales del cliente en la tabla
        se ejecuta cuando lanzamos el programa, actualizamos, insertamos y borramos un cliente
        :return: None
        '''
        #Fundamental para que se borre bien cuando quede solo una fila
        while var.ui.tableCli.rowCount() > 0:
            var.ui.tableCli.removeRow(0)
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                #cojo los valores
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                # crea la fila
                var.ui.tableCli.setRowCount(index+1)
                #voy metiendo los datos en cada celda de la fila
                #ESTO LO VA METIENDO EN (FILA,COLUMNA,CELDA) con el setItem
                var.ui.tableCli.setItem(index,0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableCli.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableCli.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    def bajaCli(dni):
        ''''
        modulo para eliminar cliente. se llama desde fichero clientes.py
        :return None
        '''
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            print('Baja cliente')
            var.ui.lblstatus.setText('Cliente con dni '+ dni + ' dado de baja      Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        else:
            print("Error mostrar clientes: ", query.lastError().text())


    def modifCli(codigo, newdata):
        #El codigo no se lo mete en el array porque se utiliza para que se guarde el array en esa posicion con el where de la query
        query = QtSql.QSqlQuery()
        codigo = int(codigo)
        print(codigo, newdata)
        query.prepare('update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, fechalta=:fechaAlta,'
                      'direccion=:direccion, provincia = :provincia, sexo=:sexo, formaspago=:formasPago, edad=:edad where codigo=:codigo')
        query.bindValue(':codigo', int(codigo))
        query.bindValue(':dni', str(newdata[0]))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':nombre', str(newdata[2]))
        query.bindValue(':fechaAlta', str(newdata[3]))
        query.bindValue(':direccion', str(newdata[4]))
        query.bindValue(':provincia', str(newdata[5]))
        query.bindValue(':sexo', str(newdata[6]))
        query.bindValue(':formasPago', str(newdata[7]))
        query.bindValue(':edad', int(newdata[8]))
        if query.exec_():
            print('Cliente modificado')
            var.ui.lblstatus.setText('Cliente con dni '+str(newdata[0])+' modificado        Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        else:
            print('Error modificar cliente: ', query.lastError().text())

    def buscaCli(dni):

        '''
        selecciona un cliente a partir de un dni
        :return:
        '''

        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                var.ui.lblCodcli.setText(str(query.value(0)))
                var.ui.editApel.setText(str(query.value(2)))
                var.ui.editNome.setText(str(query.value(3)))
                var.ui.editClialta.setText(query.value(4))
                var.ui.editDir.setText(query.value(5))
                var.ui.cmbProv.setCurrentText(str(query.value(6)))
                if str(query.value(7)) == 'Mujer':
                    var.ui.rbtFem.setChecked(True)
                    var.ui.rbtMasc.setChecked(False)
                else:
                    var.ui.rbtMasc.setChecked(True)
                    var.ui.rbtFem.setChecked(False)
                for data in var.chkpago:
                    data.setChecked(False)
                if 'Efectivo' in query.value(8):
                    var.chkpago[0].setChecked(True)
                if 'Tarjeta' in query.value(8):
                    var.chkpago[1].setChecked(True)
                if 'Transferencia' in query.value(8):
                    var.chkpago[2].setChecked(True)
                var.ui.spinEdad.setValue(query.value(9))

                var.ui.tableCli.setRowCount(index + 1)
                # voy metiendo los datos en cada celda de la fila
                var.ui.tableCli.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(1))))
                var.ui.tableCli.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(2))))
                var.ui.tableCli.setItem(index, 2, QtWidgets.QTableWidgetItem(str(query.value(3))))


    def altaPro(producto):
        query = QtSql.QSqlQuery()
        query.prepare('insert into articulos (nombre, precio, stock)'
                    'VALUES (:nombre, :precio, :stock)')
        #El array empieza en posicion 0 siempre
        query.bindValue(':nombre', str(producto[0]))
        query.bindValue(':precio', float(producto[1]))
        query.bindValue(':stock', int(producto[2]))
        #Si la query se ejecuta sin errores hace lo siguiente
        if query.exec_():
            print("Inserción Correcta")
            var.ui.lblstatus.setText('Alta Producto con nombre ' + str(producto[0]) + '       Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
            Conexion.mostrarProducto(super)
        else:
            print("Error: ", query.lastError().text())

    def mostrarProducto(self):

        #Fundamental para que se borre bien cuando quede solo una fila
        while var.ui.tablePro.rowCount() > 0:
            var.ui.tablePro.removeRow(0)
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select nombre, precio, stock from articulos')
        if query.exec_():
            while query.next():
                #cojo los valores
                nombre = query.value(0)
                precio = query.value(1)
                stock = query.value(2)
                # crea la fila
                var.ui.tablePro.setRowCount(index+1)
                #voy metiendo los datos en cada celda de la fila
                #ESTO LO VA METIENDO EN (FILA,COLUMNA,CELDA) con el setItem
                var.ui.tablePro.setItem(index,0, QtWidgets.QTableWidgetItem(nombre))
                var.ui.tablePro.setItem(index, 1, QtWidgets.QTableWidgetItem(str(precio)))
                var.ui.tablePro.setItem(index, 2, QtWidgets.QTableWidgetItem(str(stock)))
                index += 1
        else:
            print("Error mostrar producto: ", query.lastError().text())

    def cargarProducto():
        nombre = var.ui.editNomPro.text()
        query = QtSql.QSqlQuery()
        query.prepare('select * from articulos where nombre = :nombre')
        query.bindValue(':nombre', nombre)
        if query.exec_():
            while query.next():
                var.ui.lblCodpro.setText(str(query.value(0)))

        else:
            print("Error cargar codigo producto: ", query.lastError().text())

    def modifPro(codigo, newdata):
        #El codigo no se lo mete en el array porque se utiliza para que se guarde el array en esa posicion con el where de la query
        query = QtSql.QSqlQuery()
        codigo = int(codigo)
        print(codigo, newdata)
        query.prepare('update articulos set nombre=:nombre, precio=:precio, stock=:stock where codigo=:codigo')
        query.bindValue(':codigo', int(codigo))
        query.bindValue(':nombre', str(newdata[0]))
        query.bindValue(':precio', str(newdata[1]))
        query.bindValue(':stock', str(newdata[2]))
        if query.exec_():
            print('Producto modificado')
            var.ui.lblstatus.setText('Producto con nombre '+str(newdata[0])+' modificado        Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        else:
            print('Error modificar producto: ', query.lastError().text())

    def bajaPro(nombre):

        query = QtSql.QSqlQuery()
        query.prepare('delete from articulos where nombre = :nombre')
        query.bindValue(':nombre', nombre)
        if query.exec_():
            print('Baja producto')
            var.ui.lblstatus.setText('Producto con nombre '+ nombre + ' dado de baja      Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        else:
            print("Error baja producto: ", query.lastError().text())
















# class Conexion():
#     HOST = 'localhost'
#     PORT = '27017'
#     URI_CONNECTION = 'mongodb://' + HOST + ':' + PORT + '/'
#     var.DATABASE = 'empresa'
#     try:
#         var.client = pymongo.MongoClient(URI_CONNECTION)
#         var.client.server_info()
#         print('Conexión realizada al servidor %s'  %HOST)
#     except:
#         print('Error conexion')

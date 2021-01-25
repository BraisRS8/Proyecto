import bills
from PyQt5 import QtWidgets, QtSql,QtCore
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

    def altaFac(dni,fecha,apel):
        query = QtSql.QSqlQuery()
        query.prepare('insert into facturas (dni, fecha, apellidos) VALUES (:dni, :fecha, :apellidos )')
        query.bindValue(':dni', str(dni))
        query.bindValue(':fecha', str(fecha))
        query.bindValue(':apellidos', str(apel))
        if query.exec_():
            var.ui.lblstatus.setText('Factura Creada        Fecha: '+str(datetime.today().strftime('%A, %d de %B de %Y')))
        else:
            print("Error alta factura: ", query.lastError().text())
        query1 = QtSql.QSqlQuery()
        query1.prepare('select max(codfactura) from facturas')
        if query1.exec_():
            while query1.next():
                var.ui.lblCodFac.setText(str(query1.value(0)))

    def mostrarFacturas(self):
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select codfactura, fecha from facturas order by codfactura desc')
        if query.exec_():
            while query.next():
                # crea la fila
                var.ui.tableFac.setRowCount(index + 1)
                # voy metiendo los datos en cada celda de la fila
                var.ui.tableFac.setItem(index, 0, QtWidgets.QTableWidgetItem(str(query.value(0))))
                var.ui.tableFac.setItem(index, 1, QtWidgets.QTableWidgetItem(str(query.value(1))))
                index += 1
            Conexion.limpiarFac(self)
            var.ui.tableFac.selectRow(0)
            var.ui.tableFac.setFocus()
        else:
            print("Error mostrar facturas: ", query.lastError().text())
        if index == 0:
            var.ui.tableFac.clearContents()

    def mostrarFacturascli(self):
        index = 0
        cont = 0
        dni = var.ui.editDniFac.text()
        query = QtSql.QSqlQuery()
        query.prepare('select codfactura, fecha from facturas where dni = :dni order by codfactura desc')
        query.bindValue(':dni', str(dni))
        if query.exec_():
            while query.next():
                # cojo los valores
                cont = cont + 1
                codfactura = query.value(0)
                fecha = query.value(1)
                # crea la fila
                var.ui.tableFac.setRowCount(index + 1)
                # voy metiendo los datos en cada celda de la fila
                var.ui.tableFac.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codfactura)))
                var.ui.tableFac.setItem(index, 1, QtWidgets.QTableWidgetItem(str(fecha)))
                index += 1
            if cont == 0:
                var.ui.tableFac.setRowCount(0)
                var.ui.lblstatus.setText('Cliente sin Facturas')
        else:
            print("Error mostrar facturas cliente: ", query.lastError().text())

    def limpiarFac(self):
        datosfac = [var.ui.editDniFac, var.ui.editFecha, var.ui.lblCodFac, var.ui.editApellidoFac]
        for i, data in enumerate(datosfac):
            datosfac[i].setText('')

    def cargarFac(cod):
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos from facturas where codfactura = :codfactura')
        query.bindValue(':codfactura', int(cod))
        if query.exec_():
            while query.next():
                var.ui.editDniFac.setText(str(query.value(0)))
                var.ui.editApellidoFac.setText(str(query.value(1)))

    def cargarFac2(self):
        query = QtSql.QSqlQuery()
        query.prepare('select codfactura, dni, fecha, apellidos from facturas ORDER BY codfactura DESC LIMIT 1')
        if query.exec_():
            while query.next():
                var.ui.lblCodFac.setText(str(query.value(0)))
                var.ui.editDniFac.setText(str(query.value(1)))
                var.ui.editFecha.setText(str(query.value(2)))
                var.ui.editApellidoFac.setText(str(query.value(3)))

    def cargarCmbventa(cmbventa):
        var.cmbventa.clear()
        query = QtSql.QSqlQuery()
        var.cmbventa.addItem('')
        query.prepare('select codigo, nombre from articulos order by nombre')
        if query.exec_():
            while query.next():
                var.cmbventa.addItem(str(query.value(1)))

    def obtenCodPrec(articulo):
        dato = []
        query = QtSql.QSqlQuery()
        query.prepare('select codigo, precio from articulos where nombre = :nombre')
        query.bindValue(':nombre', str(articulo))
        if query.exec_():
            while query.next():
                dato = [str(query.value(0)), str(query.value(1))]
        return dato

    def altaVenta():
        query = QtSql.QSqlQuery()
        query.prepare('insert into ventas (codfacventa, codarticventa, cantidad, precio) VALUES (:codfacventa, :codarticventa,'
                      ' :cantidad, :precio )')
        query.bindValue(':codfacventa', int(var.venta[0]))
        query.bindValue(':codarticventa', int(var.venta[1]))
        query.bindValue(':cantidad', int(var.venta[3]))
        query.bindValue(':precio', float(var.venta[4]))
        row = var.ui.tableArtFac.currentRow()
        if query.exec_():
            var.ui.lblstatus.setText('Venta Realizada')
            var.ui.tableArtFac.setItem(row, 1, QtWidgets.QTableWidgetItem(str(var.venta[2])))
            var.ui.tableArtFac.setItem(row, 2, QtWidgets.QTableWidgetItem(str(var.venta[3])))
            var.ui.tableArtFac.setItem(row, 3, QtWidgets.QTableWidgetItem(str(var.venta[4])))
            var.ui.tableArtFac.setItem(row, 4, QtWidgets.QTableWidgetItem(str(var.venta[5])))
            row = row + 1
            var.ui.tableArtFac.insertRow(row)
            var.ui.tableArtFac.setCellWidget(row, 1, var.cmbventa)
            var.ui.tableArtFac.scrollToBottom()
            Conexion.cargarCmbventa(var.cmbventa)
        else:
            print("Error alta venta: ", query.lastError().text())


    def anulaVenta(codVenta):
        query = QtSql.QSqlQuery()
        query.prepare('delete from ventas where codventa = :codVenta')
        query.bindValue(':codVenta', codVenta)
        if query.exec_():
            var.ui.lblstatus.setText('Venta Anulada')
        else:
            print("Error baja venta: ", query.lastError().text())

    def borraFac(self,codfactura):
        query = QtSql.QSqlQuery()
        query.prepare('delete from facturas where codfactura = :codfactura')
        query.bindValue(':codfactura', int(codfactura))
        if query.exec_():
            var.ui.lblstatus.setText('Factura Anulada')
            Conexion.mostrarFacturas(self)
        else:
            print("Error anular factura en borrafac: ", query.lastError().text())

        query1 = QtSql.QSqlQuery()
        query1.prepare('delete from ventas where codfacventa = :codfactura')
        query1.bindValue(':codfac', int(codfactura))
        if query1.exec_():
            var.ui.lblstatus.setText('Factura Anulada')
        else:
            print("Error anular factura en borrafac: ", query.lastError().text())
        var.ui.lblSubtotal.setText('0.00')
        var.ui.lblIVA.setText('0.00')
        var.ui.lblTotal.setText('0.00')


    def listadoVentasfac(codfac):
        """

        Módulo que lista las ventas contenidaa en una factura

        :param codfac: valor factura a la que se incluirán las líneas de venta
        :type codfac: int

        Recibe el código de la factura para seleccionar los datos de las ventas cargadas a esta.
        De la BB.DD toma el nombre del producto y su precio para cada línea de venta. El precio lo multiplica
        por las unidades y se obtiene el subtotal de cada línea. Después en cada línea de la tabla irá
        el código de la venta, el nombre del producto, las unidades y dicho subotal.
        Finalmente, va sumando el subfact, que es la suma de todas las ventas de esa factura, le aplica el IVA y
        el importe total de la factura. Los tres valores, subfact, iva y fac los muestra en los label asignados.

        En excepciones se recoge cualquier error que se produzca en la ejecución del módulo.

        """
        try:
            var.ui.tableArtFac.clearContents()
            var.subfac = 0.00
            query = QtSql.QSqlQuery()
            query1 = QtSql.QSqlQuery()
            query.prepare('select codventa, codarticventa, cantidad from ventas where codfacventa = :codfactura')
            query.bindValue(':codfactura', int(codfac))
            if query.exec_():
                index = 0
                while query.next():
                    codventa = query.value(0)
                    codarticventa = query.value(1)
                    cantidad = query.value(2)
                    var.ui.tableArtFac.setRowCount(index + 1)
                    var.ui.tableArtFac.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codventa)))
                    query1.prepare('select nombre, precio from articulos where codigo = :codarticventa')
                    query1.bindValue(':codarticventa', int(codarticventa))
                    if query1.exec_():
                        while query1.next():
                            articulo = query1.value(0)
                            precio = query1.value(1)
                            var.ui.tableArtFac.setItem(index, 1, QtWidgets.QTableWidgetItem(str(articulo)))
                            var.ui.tableArtFac.setItem(index, 2, QtWidgets.QTableWidgetItem(str(cantidad)))
                            subtotal = round(float(cantidad) * float(precio), 2)
                            var.ui.tableArtFac.setItem(index, 3, QtWidgets.QTableWidgetItem("{0:.2f}".format(float(precio)) + ' €'))
                            var.ui.tableArtFac.setItem(index, 4, QtWidgets.QTableWidgetItem("{0:.2f}".format(float(subtotal))+ ' €'))
                    index += 1
                    var.subfac = round(float(subtotal) + float(var.subfac), 2)
                #ventas.Ven tas.prepararTablaventas(index)
            if int(index) > 0:
                bills.Facturas.prepararTablaventas(index)
            else:
                print(index)
                var.ui.tableArtFac.setRowCount(0)
                bills.Facturas.prepararTablaventas(0)
            var.ui.lblSubtotal.setText("{0:.2f}".format(float(var.subfac)))
            var.iva = round(float(var.subfac) * 0.21, 2)
            var.ui.lblIVA.setText("{0:.2f}".format(float(var.iva)))
            var.fac = round(float(var.iva) + float(var.subfac), 2)
            var.ui.lblTotal.setText("{0:.2f}".format(float(var.fac)))
        except Exception as error:
            print('Error Listado de la tabla de ventas: %s ' % str(error))





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

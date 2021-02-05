import conexion
import var
from Ventana import *
from datetime import datetime

class Facturas():

    def abrirCalendar(self):
        '''

        Modulo que abre la ventana calendario para cargar la fecha de factura.

        '''
        try:
            var.dlgcalendar2.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        ''''

        Modulo que se ejecuta cuando clickamos en un dia del calendar.

        :param qDate: Formateo de la fecha.
        :return: None
        :rtype: None

        Cuando clickamos en el calendario carga la fecha en editFecha

        '''
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editFecha.setText(str(data))
            var.dlgcalendar2.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))

    def altaFactura(self):
        """

        Modulo que graba una factura previa al proceso de ventas.

        :return: None
        :rtype: None

        Una vez grabada

        """
        try:
            dni = var.ui.editDniFac.text()
            fecha = var.ui.editFecha.text()
            apel = var.ui.editApellidoFac.text()
            if dni != '' and fecha != '':
                conexion.Conexion.altaFac(dni, fecha, apel)
            conexion.Conexion.mostrarFacturas(self)
            conexion.Conexion.cargarFac2(self)
            Facturas.prepararTablaventas(0)
        except Exception as error:
            print('Error alta Factura: %s ' % str(error))


    def cargarFact(self):
        '''

        Módulo que carga los datos de la factura y cliente al clickar en la tabla Factura

        :return: None
        :rtype: None

        '''
        try:
            var.subfac = 0.00
            var.fac = 0.00
            var.iva = 0.00
            fila = var.ui.tableFac.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
            var.ui.lblCodFac.setText(str(fila[0]))
            var.ui.editFecha.setText(str(fila[1]))
            conexion.Conexion.cargarFac(str(fila[0]))
        except Exception as error:
            print('Error cargar Factura: %s ' % str(error))

    def prepararTablaventas(index):
        '''

        Modulo que prepara tabla Ventas

        :param index: fila de la tabla
        :type index: int
        :return: None
        :rtype: None

        Carga un combo en la tabla Ventas con los datos del producto e inserta nueva fila.

        '''
        try:
            var.cmbventa = QtWidgets.QComboBox()
            conexion.Conexion.cargarCmbventa(var.cmbventa)
            var.ui.tableArtFac.setRowCount(index + 1)
            var.ui.tableArtFac.setItem(index, 0, QtWidgets.QTableWidgetItem())
            var.ui.tableArtFac.setCellWidget(index, 1, var.cmbventa)
            var.ui.tableArtFac.setItem(index, 2, QtWidgets.QTableWidgetItem())
            var.ui.tableArtFac.setItem(index, 3, QtWidgets.QTableWidgetItem())
            var.ui.tableArtFac.setItem(index, 4, QtWidgets.QTableWidgetItem())
        except Exception as error:
            print('Error Preparar tabla de ventas: %s ' % str(error))

    def borrarFactura(self):
        try:
            codfactura = var.ui.lblCodFac.text()
            conexion.Conexion.borraFac(self, codfactura)
            Facturas.prepararTablaventas(0)
        except Exception as error:
            print('Error Borrar Factura en Cascada: %s ' % str(error))

    def procesoVenta(self):
        try:
            var.subfac = 0.00
            var.venta = []
            codfac = var.ui.lblCodFac.text()
            var.venta.append(int(codfac))
            articulo = var.cmbventa.currentText()
            dato = conexion.Conexion.obtenCodPrec(articulo)
            var.venta.append(int(dato[0]))
            var.venta.append(articulo)
            row = var.ui.tableArtFac.currentRow()
            cantidad = var.ui.tableArtFac.item(row, 2).text()
            cantidad = cantidad.replace(',', '.')
            var.venta.append(int(cantidad))
            precio = dato[1].replace(',', '.')
            var.venta.append(round(float(precio), 2))
            subtotal = round(float(cantidad)*float(dato[1]), 2)
            var.venta.append(subtotal)
            var.venta.append(row)
            #sleep(1)
            if codfac != '' and articulo != '' and cantidad != '':
                conexion.Conexion.altaVenta()
                var.subfac = round(float(subtotal) + float(var.subfac), 2)
                var.ui.lblSubtotal.setText(str(var.subfac))
                var.iva = round(float(var.subfac) * 0.21, 2)
                var.ui.lblIVA.setText(str(var.iva))
                var.fac = round(float(var.iva) + float(var.subfac), 2)
                var.ui.lblTotal.setText(str(var.fac))
                Facturas.mostrarVentasfac()
            else:
               var.ui.lblstatus.setText('Faltan Datos de la Factura')

        except Exception as error:
            print('Error proceso venta: %s ' % str(error))

    def mostrarVentasfac():
        try:
            var.cmbventa = QtWidgets.QComboBox()
            conexion.Conexion.cargarCmbventa(var.cmbventa)
            codfac = var.ui.lblCodFac.text()
            conexion.Conexion.listadoVentasfac(codfac)

        except Exception as error:
            print('Error proceso mostrar ventas por factura: %s' %str(error))

    def anularVenta(self):
        try:
            fila = var.ui.tableArtFac.selectedItems()
            if fila:
                fila = [dato.text() for dato in fila]
            codventa = int(fila[0])
            conexion.Conexion.anulaVenta(codventa)
            Facturas.mostrarVentasfac()

        except Exception as error:
            print('Error proceso anular venta de una factura: %s' % str(error))
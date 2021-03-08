from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os,var
from datetime import *
from PyQt5 import QtSql
from datetime import datetime

class Printer():

    def reportCli(self):
        """

        Modulo que llama a la BBDD captura datos de los clientes ordenados alfabeticamente
        y los va mostrando en el informe.

        :return: None
        :rtype: None

        La variable i representa los valores del eje x.
        La variable j representa los valores del eje j.
        Los informes se guardan en la carpeta informe y al mismo tiempo se muestran
        con el lector pdf por defecto del sistema.

        """
        try:
            textlistado = "LISTADO DE CLIENTES"
            var.rep = canvas.Canvas('informes/listadoclientes.pdf')
            Printer.cabecera(self)
            Printer.cabeceraCli(self)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apellidos, nombre, fechalta from clientes order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50
                j = 690
            Printer.pie(textlistado)
            while query.next():
                if j <= 80:
                    var.rep.showPage()
                    Printer.cabecera(self)
                    Printer.pie(textlistado)
                    Printer.cabeceraCli(self)
                    i = 50
                    j = 690
                var.rep.setFont('Helvetica', size=10)
                var.rep.drawString(i, j, str(query.value(0)))
                var.rep.drawString(i + 30, j, str(query.value(1)))
                var.rep.drawString(i + 130, j, str(query.value(2)))
                var.rep.drawString(i + 280, j, str(query.value(3)))
                var.rep.drawRightString(i + 470, j, str(query.value(4)))
                j = j - 25
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile("%s/%s" % (rootPath,file))
                cont = cont + 1

        except Exception as error:
            print('Error en reportCli %s' % str(error))

    def cabecera(self):
        """

        Modulo que carga la cabecera de todos los informes de la empresa, datos fiscales...

        :return: None
        :rtype: None

        """
        try:
            logo = '.\\img\logo.jpg'
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administracion')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            textcif = 'A0000000H'
            textnom = 'IMPORTACION Y EXPORTACION TEIS, S.L.'
            textdir = 'Avenida Galicia, 101 - Vigo'
            texttlfo = '886 12 04 64'
            var.rep.drawImage(logo, 450, 752)
            var.rep.drawString(50, 805, textcif)
            var.rep.drawString(50, 790, textnom)
            var.rep.drawString(50, 775, textdir)
            var.rep.drawString(50, 760, texttlfo)
        except Exception as error:
            print('Error en cabecera %s' % str(error))

    def pie(textlistado):
        """

        Modulo que carga el pie del informe.

        :return: None
        :rtype: None

        """
        try:
            var.rep.line(50,50,525,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460,40,str(fecha))
            var.rep.drawString(275, 40, str('Pagina %s' % var.rep.getPageNumber()))
            var.rep.drawString(50, 40, str(textlistado))
        except Exception as error:
            print('Error en pie de pagina %s' % str(error))

    def cabeceraCli(self):
        """

        Modulo que carga la cabecera de pagina del informe cliente

        :return: None
        :rtype: None

        """
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE CLIENTES'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            itemCli=["Cod","DNI","APELLIDOS","NOMBRE","FECHA ALTA"]
            var.rep.drawString(45,710,itemCli[0])
            var.rep.drawString(90, 710, itemCli[1])
            var.rep.drawString(180, 710, itemCli[2])
            var.rep.drawString(325, 710, itemCli[3])
            var.rep.drawString(465, 710, itemCli[4])
            var.rep.line(45,703,525,703)
        except Exception as error:
            print('Error en cabecera de cliente %s' % str(error))

    def reportPro(self):
        """

        Modulo que llama a la BBDD captura datos de los articulos ordenados alfabeticamente
        y los va mostrando en el informe.

        :return: None
        :rtype: None

        La variable i representa los valores del eje x.
        La variable j representa los valores del eje j.
        Los informes se guardan en la carpeta informe y al mismo tiempo se muestran
        con el lector pdf por defecto del sistema.

        """
        try:
            textlistado = "LISTADO DE PRODUCTOS"
            var.rep = canvas.Canvas('informes/listadoproductos.pdf')
            Printer.cabecera(self)
            Printer.cabeceraPro(self)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio, stock from articulos')
            if query.exec_():
                i = 50
                j = 690
            Printer.pie(textlistado)
            while query.next():
                if j <= 80:
                    var.rep.showPage()
                    Printer.cabecera(self)
                    Printer.pie(self)
                    Printer.cabeceraPro(self)
                    i = 50
                    j = 690
                var.rep.setFont('Helvetica', size=10)
                var.rep.drawString(i, j, str(query.value(0)))
                var.rep.drawString(i + 30, j, str(query.value(1)))
                var.rep.drawString(i + 130, j, str(query.value(2)))
                var.rep.drawString(i + 450, j, str(query.value(3)))
                j = j - 25
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath,file))
                cont = cont + 1

        except Exception as error:
            print('Error en reportCli %s' % str(error))

    def cabeceraPro(self):
        """

        Modulo que carga la cabecera de pagina del informe articulos

        :return: None
        :rtype: None

        """
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE PRODUCTOS'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            itemPro=["Cod","Nombre","Precio","Stock"]
            var.rep.drawString(45,710,itemPro[0])
            var.rep.drawString(90, 710, itemPro[1])
            var.rep.drawString(180, 710, itemPro[2])
            var.rep.drawString(500, 710, itemPro[3])
            var.rep.line(45,703,525,703)
        except Exception as error:
            print('Error en cabecera de cliente %s' % str(error))

    def cabecerafac(codfac):
        """

        Modulo que carga la cabecera de pagina del informe facturas

        :param codfac: Codigo de la factura
        :type codfac: int
        :return: None
        :rtype: None

        Toma datos de dos tablas. Las del cliente a la que esta asociado el codigo
        factura y la de la tabla facturas para tomar los datos de dni y fecha.

        """
        try:
            var.rep.setFont('Helvetica-Bold', size=11)
            var.rep.drawString(55, 725, 'Cliente: ')
            var.rep.setFont('Helvetica', size=10)
            var.rep.drawString(50, 650, 'Factura nº : %s' % str(codfac))
            var.rep.line(45, 665, 525, 665)
            var.rep.line(45, 640, 525, 640)
            var.rep.setFont('Helvetica', size=10)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, fecha from facturas where codfactura = :codfactura')
            query.bindValue(':codfactura', int(codfac))
            if query.exec_():
                while query.next():
                    dni = str(query.value(0))
                    var.rep.drawString(55, 710, 'DNI: %s' % str(query.value(0)))
                    var.rep.drawString(420, 650, 'Fecha: %s' % str(query.value(1)))
            query1 = QtSql.QSqlQuery()
            query1.prepare('select apellidos, nombre, direccion, provincia, formaspago from clientes where dni = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec_():
                while query1.next():
                    var.rep.drawString(55, 695, str(query1.value(0)) + ', ' + str(query1.value(1)))
                    var.rep.drawString(300, 695, 'Formas de Pago: ')
                    var.rep.drawString(55, 680, str(query1.value(2)) + ' - ' + str(query1.value(3)))
                    var.rep.drawString(300, 680, str(query1.value(4).strip('[]').replace('\'', '').replace(',', ' -')))  #\ caracter escape indica que lo siguiente tiene un significado especial
            var.rep.line(45, 625, 525, 625)
            var.rep.setFont('Helvetica-Bold', size=10)
            temven = ['CodVenta', 'Artículo', 'Cantidad', 'Precio-Unidad(€)', 'Subtotal(€)']
            var.rep.drawString(50, 630, temven[0])
            var.rep.drawString(140, 630, temven[1])
            var.rep.drawString(275, 630, temven[2])
            var.rep.drawString(360, 630, temven[3])
            var.rep.drawString(470, 630, temven[4])
            var.rep.setFont('Helvetica-Bold', size=12)
            var.rep.drawRightString(500, 160, 'Subtotal:   ' + "{0:.2f}".format(float(var.ui.lblSubtotal.text())) + ' €')
            var.rep.drawRightString(500, 140, 'IVA:     ' + "{0:.2f}".format(float(var.ui.lblIVA.text())) + ' €')
            var.rep.drawRightString(500, 115, 'Total Factura: ' + "{0:.2f}".format(float(var.ui.lblTotal.text())) + ' €')
        except Exception as error:
            print('Error cabecera factura %s' % str(error))

    def reportFac(self):
        """

        Modulo que llama a la BBDD captura datos de las facturas de un cliente
        ordenados alfabeticamente y los va mostrando en el informe.

        :return: None
        :rtype: None

        La variable i representa los valores del eje x.
        La variable j representa los valores del eje j.
        Los informes se guardan en la carpeta informe y al mismo tiempo se muestran
        con el lector pdf por defecto del sistema.

        """
        try:
            textlistado = 'FACTURA'
            var.rep = canvas.Canvas('informes/factura.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.pie(textlistado)
            codfac = var.ui.lblCodFac.text()
            Printer.cabecerafac(codfac)
            query = QtSql.QSqlQuery()
            query.prepare('select codventa, codarticventa, cantidad, precio from ventas where codfacventa = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 55  # valores del eje X
                j = 600  # valores del eje Y
                while query.next():
                    if j <= 100:
                        var.rep.drawString(440, 110, 'Página siguiente...')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerafac(self)
                        i = 50
                        j = 600
                    var.rep.setFont('Helvetica', size=10)
                    nomartic= Printer.codArticulo(str(query.value(1)))
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 90, j, str(nomartic))
                    var.rep.drawRightString(i + 245, j, str(query.value(2)))
                    var.rep.drawRightString(i + 355, j, "{0:.2f}".format(float(query.value(3))))
                    subtotal = round(float(query.value(2)) * float(query.value(3)),2)
                    var.rep.drawRightString(i + 450, j, "{0:.2f}".format(float(subtotal)) + ' €')
                    j = j - 20

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reporfac %s' % str(error))

    def codArticulo(codarticventa):
        """

        Modulo que se encarga de buscar el nombre del articulo segun su codigo en la tabla de Ventas

        :return: nomartic
        :rtype nomartic: string

        """

        try:
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from articulos where codigo = :codigo')
            query.bindValue(':codigo', int(codarticventa))
            if query.exec_():
                while query.next():
                    nomartic = query.value(0)
            return nomartic
        except Exception as error:
            print("Error al intentar coger el nombre del articulo: %s" %str(error))

    def cabeceraFacCli(dni,apel,textlistado):
        """

        Modulo que carga la cabecera de facturas por cliente

        :param dni: DNI del cliente
        :type dni: String
        :param apel: Apellidos del cliente
        :type apel: String
        :param textlistado: Titulo del informe
        :type textlistado: String
        :return: None
        :rtype: None

        """
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            var.rep.drawString(230, 725, textlistado)
            var.rep.line(45, 710, 525, 710)
            var.rep.drawString(45, 725, 'Cliente: %s ' % str(apel) + '       DNI: %s' % str(dni))
            itempro = ['Nº Factura', 'FECHA FACTURA', 'Total (€)']
            var.rep.line(45, 680, 525, 680)
            var.rep.drawString(45, 690, itempro[0])
            var.rep.drawString(245, 690, itempro[1])
            var.rep.drawString(470, 690, itempro[2])
        except Exception as error:
            print("Error en la cabecera de Facturas por Cliente: %s" % str(error))

    def infFacCli(self):
        '''

        Modulo que se encarga de hacer un informe con todas las facturas de un cliente ordenadas
        por fecha y con el total

        :return: None
        :rtype: None

        '''
        try:
            textlistado = 'FACTURAS POR CLIENTE'
            var.rep = canvas.Canvas('informes/facturasCliente.pdf', pagesize=A4)
            Printer.cabecera(self)
            Printer.pie(textlistado)
            dni = var.ui.editDniFac.text()
            apel = var.ui.editApellidoFac.text()
            Printer.cabeceraFacCli(dni,apel,textlistado)
            query = QtSql.QSqlQuery()
            query.prepare('select codfactura, fecha from facturas where dni = :dni')
            query.bindValue(':dni', str(dni))
            total = 0.00
            if query.exec_():
                i = 55
                j = 650
                while query.next():
                    if j <= 100:
                        var.rep.drawString(440, 110, 'Página siguiente...')
                        var.rep.showPage()
                        Printer.cabecera(self)
                        Printer.pie(textlistado)
                        Printer.cabecerafac(self)
                        i = 50
                        j = 600
                    var.rep.setFont('Helvetica', size=10)
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawRightString(i + 240, j, str(query.value(1)))

                    query1 = QtSql.QSqlQuery()
                    query1.prepare('select cantidad, precio from ventas where codfacventa = :codfacventa')
                    query1.bindValue(':codfacventa', int(query.value(0)))
                    subtotal = 0.00
                    if query1.exec_():
                        while query1.next():
                            subtotal = subtotal + float(query1.value(0)) * float(query1.value(1))
                        var.rep.drawRightString(i + 440, j, "{0:.2f}".format(float(subtotal) * 1.21) + ' €')
                        total = total + subtotal
                    j = j - 20

            var.rep.drawRightString(i + 460, 90, 'Total Facturación Cliente:   ' + "{0:.2f}".format(float(total) * 1.21) + ' €')

            var.rep.save()
            rootPath = ".\\informes"
            cont = 0

            for file in os.listdir(rootPath):
                if file.endswith('facturasCliente.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error informe facturas por cliente:  %s ' % str(error))
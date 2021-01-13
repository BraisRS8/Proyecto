from reportlab.pdfgen import canvas
import os,var
from datetime import *
from PyQt5 import QtSql

class Printer():

    def reportCli(self):
        try:
            textlistado = "LISTADO DE CLIENTES"
            var.rep = canvas.Canvas('informes/listadoclientes.pdf')
            Printer.cabecera(self)
            Printer.cabeceraCli(self)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apellidos, nombre, fechalta from clientes order by apellidos, nombre')
            if query.exec_():
                i = 50
                j = 690
            Printer.pie(self)
            while query.next():
                if j <= 80:
                    var.rep.showPage()
                    Printer.cabecera(self)
                    Printer.pie(self)
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
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath,file))
                cont = cont + 1

        except Exception as error:
            print('Error en reportCli %s' % str(error))

    def cabecera(self):
        try:
            logo = '.\\img\logo.jpg'
            var.rep.setTitle('INFORMES')
            var.rep.setAuthor('Administracion')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            textcif = 'A0000000H'
            textnom = 'IMPORTACION Y EXPORTACION TEAIS, S.L.'
            textdir = 'Avenida Galicia, 101 - Vigo'
            texttlfo = '886 12 04 64'
            var.rep.drawImage(logo, 450, 752)
            var.rep.drawString(50, 805, textcif)
            var.rep.drawString(50, 790, textnom)
            var.rep.drawString(50, 775, textdir)
            var.rep.drawString(50, 760, texttlfo)
        except Exception as error:
            print('Error en cabecera %s' % str(error))

    def pie(self):
        try:
            var.rep.line(50,50,525,50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460,40,str(fecha))
            var.rep.drawString(275, 40, str('Pagina %s' % var.rep.getPageNumber()))
            var.rep.drawString(50, 40, str('Listado de Clientes'))
        except Exception as error:
            print('Error en pie de pagina %s' % str(error))

    def cabeceraCli(self):
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
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
            Printer.pie(self)
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
        try:
            var.rep.setFont('Helvetica-Bold', size=9)

            itemPro=["Cod","Nombre","Precio","Stock"]
            var.rep.drawString(45,710,itemPro[0])
            var.rep.drawString(90, 710, itemPro[1])
            var.rep.drawString(180, 710, itemPro[2])
            var.rep.drawString(500, 710, itemPro[3])
            var.rep.line(45,703,525,703)
        except Exception as error:
            print('Error en cabecera de cliente %s' % str(error))
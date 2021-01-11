from reportlab.pdfgen import canvas
import os,var

class Printer():

    def reportCli(self):
        try:
            var.rep = canvas.Canvas('informes/listadoclientes.pdf')
            Printer.cabecera(self)
            var.rep.drawString(255,735,'Listado Clientes')
            var.rep.line(50, 728, 525, 728)
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


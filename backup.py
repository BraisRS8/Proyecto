import sys, var, clients, events, conexion, zipfile, os, shutil, xlrd
from datetime import datetime
from PyQt5 import QtWidgets,QtSql
import time

class Backups():

    def crearBackup(self):
        """

        Modulo que se encarga de realizar el backup de la base de datos

        :return: None
        :rtype: None

        Utiliza la librería zipfile, añade la fecha y hora de la copia al nombre de esta y tras realizar la copia
        la mueve al directorio deseado por el cliente. Para ello abre una ventana de diálogo

        """
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            nombre = (str(fecha)+'_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.filedlgabrir.getSaveFileName(None, 'Guardar Copia', nombre, '.zip', options=option)
            if var.filedlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(nombre, 'w')
                fichzip.write(var.filebd, os.path.basename(var.filebd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.lblstatus.setText('Backup creado correctamente        Fecha: ' + str(datetime.today().strftime('%A, %d de %B de %Y')))
                shutil.move(str(nombre), str(directorio))
        except Exception as error:
            print('Error en la creacion de backup: %s' %str(error))

    def restaurarBackup(self):
        """

        Modulo que restaura un Backup

        :return: None
        :rtype: None

        Abre ventana de diálogo para buscar el directorio donde está copia de la BBDD y la restaura haciendo suo
        de la librería zipfile

        """
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Restaurar Copia de Seguridade','','*.zip;;All Files', options= option)
            if var.filedlgabrir.Accepted and filename != '':
                file = filename[0]
                with zipfile.ZipFile(str(file),'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
            conexion.Conexion.db_connect(var.filebd)
            conexion.Conexion.mostrarClientes(self)
            conexion.Conexion.mostrarProducto(self)
            conexion.Conexion.mostrarFacturas(self)
            var.ui.lblstatus.setText('Backup restaurado correctamente      Fecha: ' + str(datetime.today().strftime('%A, %d de %B de %Y')))
        except Exception as error:
            print('Error restaurar base de datos: %s '  % str(error))

    def importarDatos(self):
        """

        Modulo que prepara la importacion de datos de un archivo Excel

        :return: None
        :rtype: None

        Abre la ventana de seleccion de archivo y llama a la ventana de confirmacion

        """
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.filedlgabrir.getOpenFileName(None, 'Importar datos','','*.xls;;All Files', options=option)
            if var.filedlgabrir.Accepted and filename[0] != '':
                var.fileimp = filename[0]
                var.dlgimp.show()

        except Exception as error:
            print('Error importar datos: %s ' % str(error))

    def cargaDatos(self):
        """

        Modulos que se encarga de la importacion de los datos de un Excel

        :return: None
        :rtype: None

        Dependiendo de si ya existen los productos o no solo actualiza el stock,
        despues actualiza la tabla de Productos.

        """
        try:
            documento = xlrd.open_workbook(str(var.fileimp))

            productos = documento.sheet_by_index(0)

            filas_prod = productos.nrows
            cont = 0

            for i in range(1, filas_prod):
                prod_nom = str(productos.cell_value(i, 0))
                prod_precio = repr(productos.cell_value(i, 1))
                prod_stock = int(productos.cell_value(i, 2))

                query = QtSql.QSqlQuery()
                query.prepare('select codigo, precio, stock from articulos where nombre = :nombre')
                query.bindValue(':nombre', str(prod_nom))

                if query.exec_():
                    while query.next():
                        cont = cont + 1
                        query1 = QtSql.QSqlQuery()
                        query1.prepare('update articulos set precio=:precio, stock=:stock where nombre = :nombre')
                        query1.bindValue(':nombre', str(prod_nom))
                        query1.bindValue(':precio', float(prod_precio))
                        stock = int(query.value(2)) + prod_stock
                        query1.bindValue(':stock', int(stock))
                        if query1.exec_():
                            var.ui.lblstatus.setText('Articulos actualizados    Fecha: ' + str(datetime.today().strftime('%A, %d de %B de %Y')))
                        else:
                            print("Error actualizando productos: ", query1.lastError().text())

                    if cont == 0:
                        query2 = QtSql.QSqlQuery()
                        query2.prepare('insert into articulos (nombre, precio, stock) VALUES (:nombre, :precio, :stock)')
                        query2.bindValue(':nombre', str(prod_nom))
                        query2.bindValue(':precio', float(prod_precio))
                        query2.bindValue(':stock', int(prod_stock))

                        if query2.exec_():
                            var.ui.lblstatus.setText('Articulos añadidos    Fecha: ' + str(datetime.today().strftime('%A, %d de %B de %Y')))
                        else:
                            print("Error añadiendo productos: ", query2.lastError().text())

            conexion.Conexion.db_connect(var.filebd)
            conexion.Conexion.mostrarProducto(self)
            print("---------")

        except Exception as error:
            print('Error en la carga de datos: %s' % str(error))




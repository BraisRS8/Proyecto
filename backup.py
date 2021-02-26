import sys, var, clients, events, conexion, zipfile, os, shutil
from datetime import datetime
from PyQt5 import QtWidgets
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
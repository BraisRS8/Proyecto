import sys, var
from clients import *

class Eventos():

    def Salir(event):
        """

        Modulo para cerrar el programa

        :return: None
        :rtype: None

        Muestra ventana de aviso

        """
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec_():
                #print(event)
                sys.exit()
            else:
                var.dlgsalir.hide()
                event.ignore()


        except Exception as error:
            print('Error %s' % str(error))

    def closeSalir(event):
        """

        Modulo que cierra las ventanas

        :param event: evento de la ventana
        :type event: None
        :return: None
        :rtype: None

        """
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec_():
                print(event)
                var.dlgsalir.hide()
               #necesario para que ignore X de la ventana
        except Exception as error:
            print('Error %s' % str(error))

    def cargarProv(self):
        """

        Modulo que se ejecuta al inicio para cargar las provincias. En version
        posterior cargaremos las provincias y municipios desde la BBDD.

        :return: None
        :rtype: None

        """
        try:
            prov = ['','A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Vigo']
            for i in prov:
                var.ui.cmbProv.addItem(i)

        except Exception as error:
            print('Error: %s' % str(error))

    def AbrirDir(self):
        """

        Modulo que abre la ventana de abrir.

        :return: None
        :rtype: None

        """
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print('Error %s' % str(error))

    def Print(self):
        """

        Modulo que abre la ventana de imprimir.

        :return: None
        :rtype: None

        """
        try:
            var.printdlgabrir.show()
        except Exception as error:
            print('Error %s' % str(error))

    def Conf(event):
        """

        Modulo que abre ventana de confirmacion.

        :return: None
        :rtype: None

        """
        try:
            if (var.ui.editDni.text() != ''):
                var.dlgconf.show()

        except Exception as error:
            print('Error %s' % str(error))

    def About(self):
        """

        Modulo que abre la ventana de informacion.

        :return: None
        :rtype: None
        """
        try:
            var.dlgabout.show()
        except Exception as error:
            print('Error %s' % str(error))
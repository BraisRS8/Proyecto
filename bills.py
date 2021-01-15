import conexion
import var
from Ventana import *
from datetime import datetime

class Facturas():

    def abrirCalendar(self):
        '''
        Abrir la ventana calendario
        '''
        try:
            var.dlgcalendar2.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        ''''
        Este módulo se ejecuta cuando clickeamos en un día del calendar, es decir, clicked.connect de calendar
        '''
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.editFecha.setText(str(data))
            var.dlgcalendar2.hide()
        except Exception as error:
            print('Error cargar fecha: %s ' % str(error))
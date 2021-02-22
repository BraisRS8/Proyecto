import unittest
import clients, conexion, var
from PyQt5 import QtSql

class MyTestCase(unittest.TestCase):

    def test_conexion(self):
        value = conexion.Conexion.db_connect(var.filebd)
        msg = 'Conexion no valida'
        self.assertTrue(value,msg)

    def test_dni(self):
        dni = '00000000T'
        value = clients.Clientes.validarDni(str(dni))
        msg = 'Prueba dni no valido'
        self.assertTrue(value,msg)

    def test_fact(self):
        valor = 48.40
        codfac = 5
        try:
            msg = 'Calculos erroneos'
            var.subfac = 0.00
            query = QtSql.QSqlQuery()
            query1 = QtSql.QSqlQuery()
            query.prepare('select codventa, codarticventa, cantidad from ventas where codfacventa = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                while query.next():
                    codarticventa = query.value(1)
                    cantidad = query.value(2)
                    query1.prepare('select nombre, precio from articulos where codigo = :codarticventa')
                    query1.bindValue(':codarticventa', int(codarticventa))
                    if query1.exec_():
                        while query1.next():
                            precio = query1.value(1)
                            subtotal = round(float(cantidad)*float(precio), 2)
                    var.subfac = round(float(subtotal)+float(var.subfac), 2)
            var.iva = round(float(var.subfac)*0.21, 2)
            var.fac = round(float(var.iva)+float(var.subfac), 2)
        except Exception as error:
            print('Error listado de la tabla ventas: %s ' % str(error))
        self.assertEqual(round(float(valor),2), round(float(var.fac),2),msg)
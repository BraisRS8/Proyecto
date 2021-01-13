import conexion
import var
from Ventana import *
from datetime import datetime

class Productos():

    def altaProducto(self):
        try:
            newpro = []
            product = [var.ui.editNomPro, var.ui.editPrecio, var.ui.editStock]
            for i in product:
                newpro.append(i.text())
            if product:
                conexion.Conexion.altaPro(newpro)
                Productos.limpiarPro()
            else:
                print('Faltan datos en producto')
        except Exception as error:
            print('Error en altaProducto: %s ' % str(error))

    def cargarPro(self):
        try:
            fila = var.ui.tablePro.selectedItems()
            #Esto sirve para guardar en el array de fila cada dato que esta seleccionado en la tabla
            if fila:
                fila = [dato.text() for dato in fila]


            var.ui.editNomPro.setText(str(fila[0]))
            var.ui.editPrecio.setText(fila[1])
            var.ui.editStock.setText(fila[2])
            print(fila[1])
            var.ui.lblstatus.setText('Carga Producto realizada      Fecha: ' + str(datetime.today().strftime('%A, %d de %B de %Y')))
            conexion.Conexion.cargarProducto()

        except Exception as error:
            print('Error cargar producto: %s ' % str(error))

    def modifProducto(self):
        try:
            newdata = []
            client = [var.ui.editNomPro, var.ui.editPrecio, var.ui.editStock]
            for i in client:
                newdata.append(i.text())  # cargamos los valores que hay en los editline
            cod = var.ui.lblCodpro.text()
            conexion.Conexion.modifPro(cod, newdata)
            conexion.Conexion.mostrarProducto(self)
            Productos.limpiarPro()

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def bajaProducto(self):

        try:

            nombre = var.ui.editNomPro.text()
            conexion.Conexion.bajaPro(nombre)
            conexion.Conexion.mostrarProducto(self)
            Productos.limpiarPro()


        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def limpiarPro():

        try:
            #Coje los editText y con el for hace que se vacie el texto
            client = [var.ui.editNomPro, var.ui.editPrecio, var.ui.editStock]
            for i in range(len(client)):
                client[i].setText('')
            var.ui.lblCodpro.setText('')
        except Exception as error:
            print('Error limpiar widgets: %s ' % str(error))
import var, sys

class Eventos():

        def Saludo():
            try:
                var.ui.lbl_saludo.setText('Pulsaste el botón')
            except Exception as error:
                print("Error: %s " % str(error))

        def Salir():
            try:
                sys.exit()
            except Exception as error:
                print("Error %s: " % str(error))
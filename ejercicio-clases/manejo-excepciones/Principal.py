

from paquete_excepciones.miexepcion import *
try:
    edad = input("Ingrese su edad: \n")
    edad = int(edad)
    print("Su edad es: %d"%(edad))
#except NameError as e:
 #   print("Existe un error")
except Exception as e:
    print("Existe un error: (%s): %s" %(e.__class__, e))
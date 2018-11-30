#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

import codecs


class MiArchivo:
    """Clase para cargar el archivo informacion.csv"""

    def __init__(self, ruta):
        """Constructror de la clase"""
        self.archivo = codecs.open(ruta+"informacion.csv", "r")

    # Metodo que lee todo el archivo
    def obtener_informacion(self):
        return self.archivo.readlines()

    # Metodo que sierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """Clase para escribir el nuevo archivo informacion2.csv"""

    def __init__(self, ruta):
        """Constructor de la clase"""
        self.archivo = codecs.open(ruta+"informacion2.csv", "a")

    # Metodo que escribe un encabezado en el nuevo archivo
    def agregar_encabezado(self, encabezado):
        self.archivo.write(encabezado)

    # Metodo que escribe la informacion de la persona en el nuevo archivo
    def agregar_informacion(self, p):
        self.archivo.write("%s\n" % (p))

    # Metodo que sierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()

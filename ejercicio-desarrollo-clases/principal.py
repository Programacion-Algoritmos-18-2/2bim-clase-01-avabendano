#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria

# Importamos la clase os para funciones de sistema
import os

# importamos nuestaras clases
from paquete_archivo.archivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.modelo import Persona

# Generamos la ruta absoluta asta este archivo 'principal.py'
directorioBase = os.path.dirname(os.path.abspath(__file__))
# Unimos la ruta de este archivo mas el nombre de la carpeta
# donde se encuentran nuestros csv
directorioArchivo = os.path.join(directorioBase, 'data\\')

# Creamos los dos obejtos que admistran nuestros arcivos
# pasamos la urata para que pueda encontrar el archivo
m = MiArchivo(directorioArchivo)
nm = MiArchivoEscribir(directorioArchivo)

# obtenemos toda la informacion
lista = m.obtener_informacion()
# separamos cada fila en sus daos
lista = [l.split("|") for l in lista]
# Excluimos la primera linea de encabezado
lista = lista[1:]

# Creamos un encabezado nuevpo
nm.agregar_encabezado('alumno|promedio\n')
# recorremos las filas
for fila in lista:
    # Evitamos el error de fuera de indice por la ultima linea que tiene un salto de line (\n)
    if fila[0] != '\n':
        # Creamos el objeto persona, con sus atributos
        p = Persona(fila[0], fila[1], fila[2], fila[3])
        # Agragamos la informacion al archivo nuemo
        nm.agregar_informacion(p)

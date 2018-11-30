#!/usr/bin/python
# -*- coding: utf-8 -*-
# Victoria


class Persona(object):
    """Clase Persona"""

    def __init__(self, nombre, nota1, nota2, nota3):
        """Constructor de clase"""
        self.nombre = nombre
        self.nota1 = int(nota1)
        self.nota2 = int(nota2)
        self.nota3 = int(nota3)

    # Metodos Agregar y Obtener atributos
    def agregar_nombre(self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

    def agregar_nota1(self, nota1):
        self.nota1 = int(nota1)

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota2(self, nota2):
        self.nota2 = int(nota2)

    def obtener_nota2(self):
        return self.nota2
    
    def agregar_nota3(self, nota3):
        self.nota3 = int(nota3)

    def obtener_nota3(self):
        return self.nota3

    # Metodo que calcula el promedio de notas
    def calc_prom(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    # Sobreescribimos el metodo __str__
    # Para impirmir en el nuevo archivo
    def __str__(self):
        return "%s|%.2f" % (self.nombre, self.calc_prom())

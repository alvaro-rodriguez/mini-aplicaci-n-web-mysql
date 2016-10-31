#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
from mysql.connector import (connection)

#En esta variable se guardan los datos de inicio de sesión
cnx = connection.MySQLConnection(user='usuario', password='usuario',
                                 host='192.168.0.68',
                                 database='prueba')
cursor = cnx.cursor()
#Aquí se guarda la Queri, obviamente..
query = ("SELECT CIF, Ciudad FROM empresas")

#Se lanza la Query 
cursor.execute(query)
"""
# Esta funciona =~
for row in cursor.fetchall():
    print row[0]
"""

#Esta  SÍ funciona.
#Además con CASI cialquier select.


#Se muestran los datos, esto esá orientado a operaciones de búsqueda de datos
#para la inserción de datos o creación de tabals (ect..)no sería necesario.

for row in cursor.fetchall():
  print "+------------------------"
  print "|",
  for r in row:
    print r ,
  print "|"
      

cursor.close()
cnx.close()

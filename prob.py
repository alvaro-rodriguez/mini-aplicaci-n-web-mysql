#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
from mysql.connector import (connection)
import mysql.connector
from bottle import default_app, get, post, route , run , template, request, redirect
import os

#lista de variables para las credenciales:

cred =[]

@get('/')
def menu():
    return template('credencial.tpl')

@post('/')
def menu_post():
  redirect ('/query')
  cred[0] = request.forms.get("user")
  cred[1] = request.forms.get("passwod")
  cred[2] = request.forms.get("host")
  cred[3] = request.forms.get("database")

  cnx = connection.MySQLConnection(user=cred[0], password=cred[1],
				host=cred[2],
				database=cred[3])
  global cnx 
  return template('aplication.tpl')

""" 
@get('/')
def menu():
    return template('aplication.tpl')
 """

@post('/query')
def query_submit():
  texto = request.forms.get("query")
  usuario = request.forms.get("user")
  contrasena = request.forms.get("password")
  host = request.forms.get("host")
  database = request.forms.get("database")
  cnx = connection.MySQLConnection(user=usuario, password=contrasena,
				host=host,
				database=database)
  cursor = cnx.cursor()
  query = (texto)
  cursor.execute(query)
  return template('query.tpl',cursor=cursor)

@route('/query')
def querymostrar():
    return template('aplication.tpl')
  
@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)

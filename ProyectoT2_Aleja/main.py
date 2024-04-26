#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def abrirArchivo():
    miJSON=[]
    with open('ProyectoT2_Aleja/info.json',encoding='utf-8') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("ProyectoT2_Aleja/info.json","w") as outfile:
        json.dump(miData,outfile)


print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
print("Hola! Por favor escoge alguna de estas opciones: \n1.Añadir estudiantes\n2.Modificar estudiantes\n3.Revisar estudiantes\n4.Eliminar estudiantes")
x=int(input("Cual opción escoges: "))
miInfo=[]
if(x==1):
   miInfo=abrirArchivo()
   for i in miInfo[0]["estudiantes"]:
        print("################")
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento:",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
        nombreNE = input("Ingresa el nombre del nuevo estudiante: ")
        apellidoNE = input("Ingresa el apellido del nuevo estudiante: ")
        edadNE = int(input("Ingresa la edad del estudiante: "))
        fechaNacimientoNE = int(input("Ingresa la fecha de nacimiento del nuevo estudiante: "))
        cedulaNE = int(input("Ingresa el número de cédula del nuevo estudiante: "))
        emailNE = input("Ingresa el email del nuevo estudiante: ")
        gitHubNE= input("Ingresa el enlace de gitHub del nuevo estudiante: ")
        nuevoEstudiante = {
            "nombre": nombreNE,
            "apellido": apellidoNE,
            "edad": edadNE,
            "fechaNacimiento": fechaNacimientoNE,
            "cedula": cedulaNE,
            "email": emailNE,
            "github": gitHubNE
        }
        ["info"].append(nuevoEstudiante)
        def guardarArchivo(miData):
         with open("ProyectoT2_Aleja/info.json","w") as outfile:
          json.dump(miData,outfile)
  
   
elif(x==2):
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]: 
        print("################")
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento:",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("") 
        estudiante = int(input("Cual numero de identificacion vas a cambiar? "))
    datoCambiar=int(input("Que te gustaría cambiar del estudiante: \n1.Nombre\n2.Apellido\n3.Edad\n4.Fecha de nacimiento\n5.Cédula\n6.Email:"))
    if (datoCambiar==1):
        nuevoNombre = input("Ingresa el nuevo nombre: ")
        miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    if (datoCambiar==2):
        nuevoApellido = input("Ingresa el nuevo apellido: ")
        miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    if (datoCambiar==3):
        nuevaEdad = input("Ingresa la nueva edad: ")
        miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    if (datoCambiar==4):
        nuevaFecha = input("Ingresa la nueva fecha de nacimiento: ")
        miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = nuevaFecha
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    if (datoCambiar==5):
        nuevaCedula = input("Ingresa la nueva cédula: ")
        miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    if (datoCambiar==6):
        nuevoEmail = input("Ingresa el nuevo email: ")
        miInfo[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento:",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0
elif(x==3):
   miInfo=abrirArchivo()
   for i in miInfo[0]["estudiantes"]:
        print("################")
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento:",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")

#Desarrollado por Alejandra Machuca Grupo T2
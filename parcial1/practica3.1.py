#Practica 3.1 Arreglos

alumnos=[[],[],[]]

cant=int(input("CUANTAS PERSONAS SERAN?\n"))

if cant>0:
    for i in range(cant):
        print("INFORMACIÓN DEL USUARIO", i+1)
        nombre=input("NOMBRE:\n")
        edad=int(input("EDAD: \n"))
        pais=input("PAIS: \n")

        alumnos[0].append(nombre)
        alumnos[1].append(edad)
        alumnos[2].append(pais)

    info=int(input("QUE ALUMNO DESEAS REVISAR\n"))-1
    if info>cant-1:
        print("NO SE ENCONTRO")
    else:
        print(f"EL ALUMNO CON EL NUMERO {info+1} TIENE LA SIGUIENTE INFORMACIÓN: {alumnos[0][info]}, {alumnos[1][info]}, {alumnos[2][info]}")

    infoDel=int(input("QUE ALUMNO ELIMINARA\n"))-1
    if infoDel>cant-1:
        print("NO SE ENCONTRO")
    else:
        alumnos[0].pop(infoDel)
        alumnos[1].pop(infoDel)
        alumnos[2].pop(infoDel)
        print("ACTUALIZADO: \n",alumnos)

else:
    print("CANTIDAD MENOR A 0")


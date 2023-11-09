#INTRODUCCIÓN
print('MUNDO HOLA')
name = input('ESCRIBE TU NOMBRE')
edad = int(input('ESCRIBE TU EDAD'))

#CONCATENADO
print('HOLA '+name+ 'LA EDAD QUE INGRESASTE ES: '+edad) #SUMA(+)
print('HOLA ',name, 'LA EDAD QUE INGRESASTE ES: ',edad) #COMAS(,)
if edad < 18 :
    print('ERES MENOR DE EDAD')
else:
    print('YA PUEDES VOTAR')
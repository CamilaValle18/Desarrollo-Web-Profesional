def saludar():
    print('Hola mundo')
saludar()

#Funcion sin argumentos
def sumar_numeros(numero_x, numero_y):
    suma = numero_x + numero_y
    print(f'El resultado de la suma es: {suma}')
    return suma

# Llamada a la función
sumatoria = sumar_numeros(numero_x=10, numero_y=20)
print(f'El valor de la sumatoria es: {sumatoria}')

#Funcion con valores por defecto
def valores_por_defecto_suma(numero_x=0, numero_y=1, numero_z = 2):
    suma=numero_x +numero_y +   numero_z
    print(f'Eñ resultado de la suma con valores por defecto es : {suma}')
    return suma
def alumnos_materias (nombre, *args):
    print(f'Nombre:{nombre}, materias: {args}')
    print(f'Nombre:{type(nombre)},materias:{type(args)}')

def alumnos_calificaciones (nombre, **kwargs):
    print(f'Nombre:{nombre}, calificaciones: {kwargs}')
    print(f'Nombre:{type(nombre)},calificaciones:{type(kwargs)}')



#saludar()
#sumatoria=sumar_numeros(10, 20)
#print(f'El valor de sumatoria es :{sumatoria')
#sumatoria= valores_por_defecto_suma(numero_x=10, numero_z= 20)

#alumnos_materias('josesito','programacion','matematicas', 'ingles'
alumnos_calificaciones(nombre= 'josesito', programacion=10, matematicas=9, ingles=10)
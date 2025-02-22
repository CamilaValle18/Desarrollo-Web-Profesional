import pandas as pd

good_student_qualities = ['Disciplinado', 'Puntualidad', 'Respetuoso', 'Honesto', 'Amigoso']
serie = pd.Series(good_student_qualities)
print(serie)

#Tamaño de la serie
print(f'El tamaño de la serie es el siguiente: {serie.size}')

#La serie tiene valores duplicados
print(f'La serie tiene valores duplicados: {serie.is_unique}')

#Informacion de los indices
print(f'Este atributo muestra informacion de los indices: {serie.index}')

#Formacion del almacenamiento de los valores de la serie
print(f'Informacion de los valores de la serie: {serie.values}')

#Informacion del tipo de datos que se utilizan para almacenar los valores de la serie
print(f'Tipo de datos: {type(serie.values)}')
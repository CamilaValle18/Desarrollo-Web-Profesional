result = None
numero_x = 10
numero_y = 2

try:
    numero_x = int(input("Ingrese el numero para x: "))
    numero_y = int(input("Ingrese el numero para y: "))
    result = numero_x / numero_y
    print(f'El resultado de la division es: {result}')
except ZeroDivisionError as e:
    print(f'La excepcion es la siguiente: {e}')
except ValueError as e:
    print(f'La excepcion de ValueError genero el siguiente mensaje: {e}')
except Exception as e:
    print(f'La excepcion de Exceptio genero el siguiente mensaje: {e}')
finally:
    print(f'Nuestro programa a finalizado')
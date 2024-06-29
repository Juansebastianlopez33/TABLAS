'''
Este modulo se encarga de crear las tablas desde 1 asta un numero aleatorio
y que cada numero desde 1 se le cre una tabla asta el 10
version: 2.0
'''
#con este modulo  generamos numeros aleatorios y colores aleatorios
from random import randint

#Proporciona funciones relacionadas con el manejo del tiempo
from  time import sleep 

#con este modulo escoji una plataforma (windows)para identificar el tipo de sistema
from platform import system

#Proporciona funciones para la interacción con el sistema operativo
from os import system as osystem

#propocionamos funciones al interactuar con el teclado 
from msvcrt import getwch

#importamos colorama para poder colocar color y diseño al codigo
from colorama import Fore,Back

#definicmos una funcion en la cual vamos a hacer el codigo para que se generen las tablas
def operacion():
    #generamos un numero aleatorio y lo almacenamos en numram
    numero_aleatorio = randint(1, 20)

    #imprimimos el numero aleatorio para que el usuario vea asta donde se van a generar las tablas
    print("el numero generado es: "+ Fore.GREEN , numero_aleatorio)
    print('\n'+"presione enter para continuar"+ Fore.RESET)
    ele_ini = None
    while ele_ini not in ['\r']:
        ele_ini = getwch()

    if system() =="Windows":
        osystem("cls")
    else:
        osystem("clear")
    #creamos un bucle que imprima el el numero de la tabla actual asta el numero aleatorio que se genero
    for i in range(1,numero_aleatorio +1):
            print(Fore.GREEN + Back.WHITE)
            print(f"La tabla del numero {i} es:"+ '\n')

            #creamos la tabla basada en el numero actual de blucle anteior y limitamos asta 10 
            for j in range(1, 11):
                #multiplicamos el numero del bucle anterior por el del el bucle actual
                producto = i * j

                #mostamos el resultado de multiplicar el numero del bucle anterior por el de el bucle actual
                print(f"{i} x {j} es: {producto}")
                print("")
            print(Fore.RESET + Back.RESET)
            '''
            creamos un print que le indique al usuario precione una tecla para continuar 
            luego utilisando el modulo msvcrt y su funcion getch capturamos cualquier tecla que precione el usuario para poder continuar
            '''
            print("presione enter para continuar")
            ele_ini = None
            while ele_ini not in ['\r']:
                ele_ini = getwch()
            sleep(0.1)
            '''
             aqui creamos una estructura de control con la cual podemos verificar si se esta ejecutando el codigo en windows
             con esto sabes si debemso indicar que escriba cls o clear para limpiar la consola y  no saturar la pantalla con nuestro codigo 
            '''
            if system() =="Windows":
                osystem("cls")
            else:
                osystem("clear")
if __name__ == '__main__':
    operacion()

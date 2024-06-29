#Juan Sebastian Lopez
#Ficha: 287795
#CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIO 
#version = 3.0

#importamos la funcion choise del modulo random
from random import choice

#importamos la funcion getch de el modulo msvcrt
from msvcrt import getwch

#importamos system de el modulo os y lo renombramos osystem para evitar errores y confuciones
from os import system as osystem

#importamos system de  el modulo plataform
from platform import system

#importamos selecion_final del archivo final que esta dentro de la carpeta Modules
from Modules.final import main as selecion_final

#importamos fore de el modulo colorama
from colorama import Fore

#importamos saludo de el archivo saludo_personalisado que esta dentro de la carpeta Modules
from Modules.saludo_personalisado import main as saludo

#importamos la funcion operacion del archivo operaciones que esta dentro de la carpeta Modules
from Modules.opreciones import operacion

def main():
        #creamos una variable colores_disponibles en la cual guardamos con ayuda de el modulo colorama 6 colores distintos
        
        colores_disponibles = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        
        #le desimos que la variable color aleatorio tome un color diferente cada ves que se invoca a la variable
         
        color_aleatorio = choice(colores_disponibles)
        
        #invocamos la funcion saludo
        
        saludo()
        
        #le decimos al usuario que precione cualquier enter para que con la funcion getch continue el programa 
        print("presione enter para continuar")
        ele_ini = None
        while ele_ini not in ['\r']:
            ele_ini = getwch()
        #verificamos si estamos trabajando con windows para usar la funcion osystem y limpiar la pantalla 
        if system() =="Windows":
                osystem("cls")
        else:
            osystem("clear")                                              

        #creamos el buqle prinsipal con while true
        while True:
            #verificamos si estamos trabajando con windows para usar la funcion osystem y limpiar la pantalla 
            if system() =="Windows":
                osystem("cls")
            else:
                osystem("clear")
            #creamso un print para dejar un espacio entre cada linea
            print("")

            #llamamos a la funcion que se encarga de generar las tablas 
            operacion() 

            '''
            Creamos una variable con la cual podemos guardar el return que nos bota la funcion 
            que se encarga de darle la opcion si reiniciar o no el programa
            '''
            verifi = selecion_final()
            #Con este if verificamos si return es igual a N para poder cerrar el programa 
            if verifi == 'N':
                osystem("cls")
                break
    
if __name__ == '__main__':
    main()
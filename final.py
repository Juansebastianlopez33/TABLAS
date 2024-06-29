'''
Este modulo se encarga de darle la opcion final al ususario de repetir o terminar el codigo 
version: 1.0
'''
#importamos getwch de msvcrt
from msvcrt import getwch
def main():
    #creamos una funcion para capturar la decicion final de el usuario
    def selecion_final():
        #definimos entrada como una variable vacia para poder usarla como lista mas a delante
        Entrada = None
        #creamos una estructura de control que nos permite repetir un codigo si el usuario preciono S(para continuar ) o N (para salir)
        print("Presiona 'S' para generar una nueva lista  o 'N' para salir EN MAYUSCULA")
        while Entrada not in ["S", "N"]:
            #capturamos la entrada del usuario 
            Entrada = getwch()
            # Ignorar el carácter de nueva línea
            if Entrada == '\r':
                continue
        return Entrada
    return selecion_final()
if __name__ == '__main__':
    main()
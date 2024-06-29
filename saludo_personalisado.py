import random
from colorama import Fore, Back
def main():
        color_letra_aleatorio = [Fore. RED, Fore.GREEN, Fore.LIGHTMAGENTA_EX]
        color_letra = random.choice(color_letra_aleatorio)
        def saludo():
                print(color_letra)
                #creamos sello para el programa 
                print("""
                _____________                
             __|             |__             
            |        JS      |  |            
            |__|__         __|__|            
                 |__     __|                 
                 __|____|__                  
               __|__|__|__|__                
              |__|__|__|__|__|              
"""+ Fore.RESET)
        saludo()
if __name__ == '__main__':
        main()
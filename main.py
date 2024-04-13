from User import *
from Password import *
from common import *

# Import necessary modules or packages

# Define any global variables or constants

# Define any helper functions or classes
def login(username, password):
    while(not confirm_username(username)):
        username = input("Ingresa nuevamente tu nombre de usuario: ")
    while(not confirm_password(username, password)):
        password = input("Ingresa nuevamente tu contraseña de usuario: ")
    return True

# Define the main function
def main():
    exit = False
    while(not exit):
        print("Bienvenido a MyPass!\n Por favor escoge una de las siguientes opciones (Para seleccionar, indica el número del ítem)\n")
        print(" 1) Iniciar sesión.\n 2) Regístrate.\n 3) Cerrar aplicación\n")
        choice = input("Escribe tu opción aquí: ")
        if(choice == "1"):
            username = input("Ingresa tu nombre de usuario: ")
            password = input("Ingresa tu contraseña de usuario: ")
            login(username, password)
        elif(choice == "2"):
            


# Check if the file is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()

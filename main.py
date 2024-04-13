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
    return username

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
            username = login(username, password)
        elif(choice == "2"):
            user = create_profile()
        else:
            exit = True
    while(not exit):
        print("Hola" + username + ", ¿Qué deseas hacer?\n")
        print("Sobre contraseñas almacenadas:\n 1) Agregar contraseña\n 2) Visualizar palabras claves\n 2) Modificar palabra clave de contraseña\n 3) Modificar contraseña\n 4) Eliminar contraseñas\n")
        print("\nSobre gestión de cuenta\n 5) Actualizar nombre de usuario\n 6) Cambiar contraseña")
# Check if the file is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()

"""
Descripción: Como futuro Usuario quiero crear mi perfil para usar las funcionalidades del sistema y, de esa forma, almacenar mis contraseñas.

Criterios de aceptación: Dado un futuro usuario, cuando quiera crear su perfil, entonces el sistema le solicita un nombre de usuario (Nickname), una contraseña, la verificación de la contraseña y responder una pregunta personal (¿Nombre de la primera escuela?) con el fin de añadir seguridad.
El sistema verifica si hay algún usuario con ese nickname, si lo hay, el sistema envía un mensaje de error y le solicita otro nombre de usuario y, si no hay usuario existente con el mismo nombre, entonces lo acepta.
La contraseña debe cumplir con:

Longitud mínima: 8.
y los caracteres permitidos son:

números de 0 a 9.
Letras de A hasta Z y a hasta z.
Caracteres especiales: ° . ! ” # $ % & / ( ) < = > ¿ ? ¡ { } * _ - + . [ ] @ [ ^ ;
"""

class User:
    def __init__(self, username, password, question):
        self.username = username
        self.password = password
        self.question = question

def create_profile():
    # Get user input
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirmpassword = input("Confirm password: ")
    question = input("What is the name of your first school? ")
    if check_profile(username, password, confirmpassword, question):
        user = User(username, password, question)
        return user
    


def check_profile(username, password, confirmpassword, question):
    ######### ADD WHEN DATABASE IS ESTABLISHED ##########
    # # Check if username already exists
    # with open('/path/to/usernames.txt', 'r') as file:
    #     usernames = file.read().splitlines()
    #     if username in usernames:
    #         print("Username already exists. Please choose another username.")
    #         return False
    
    # Check if password is longer than 8 characters
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Check if password and confirm password match
    if password != confirmpassword:
        print("Passwords do not match. Please try again.")
        return False
    
    # Check if password contains only allowed characters
    allowed_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz°.!\"#$%&/()<=¿?¡{}*_+-[].@[^;"
    for char in password:
        if char not in allowed_chars:
            print("Password contains invalid characters. Please try again.")
            return False
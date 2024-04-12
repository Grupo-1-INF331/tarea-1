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
import pandas as pd

class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.question = None
        self.create_profile()

    def create_profile(self):
        # Get user input
        while (self.username == None):
            username = input("Enter username: ")
            password = input("Enter password: ")
            confirmpassword = input("Confirm password: ")
            question = input("What is the name of your first school? ")
            if self.check_profile(username, password, confirmpassword, question):
                self.username = username
                self.password = password
                self.question = question
            

    def check_profile(self, username, password, confirmpassword, question):
        # Path to the Excel file
        excel_path = 'main/users_data.xlsx'

        # Read the Excel file
        try:
            df = pd.read_excel(excel_path)
            # Assuming the column for usernames in the Excel file is named 'Username'
            if username in df['Username'].values:
                print("Username already exists. Please choose another username.")
                return False
        except FileNotFoundError:
            print(f"Error: The file '{excel_path}' does not exist.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        
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
from common import *

class User:
    def __init__(self, username, password, question):
        self.username = username
        self.password = password
        self.question = question

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
    def create_profile():
        # Define username
        confirm = False
        while (not confirm):
            username = input("Ingresa tu nombre de usuario: ")
            if(check_username(username)):
                print("El nombre de usuario es " + username + " ¿Confirmas el nombre de usuario?")
                choice = input("1) Confirmar. \n2) Cancelar")
                if choice == "1":
                    confirm = True
            else:
                print("Nombre de usuario existente! Por favor, escribe un nombre de usuario distinto.\n")

        # Define question
        confirm = False
        while (not confirm):
            question = input("¿Cuál es el nombre de la primera escuela a la que ingresaste?: ")
            print("La respuesta es '" + question + "' ¿Confirmas tu respuesta?")
            choice = input("1) Confirmar. \n2) Cancelar")
            if choice == "1":
                confirm = True

        # Define password
        password = input("Ingresa la nueva contraseña: ")
        confirmpassword = input("Confirma la nueva contraseña: ")
        while (not check_password(password, confirmpassword)):
            password = input("Ingresa la nueva contraseña: ")
            confirmpassword = input("Confirma la nueva contraseña: ")
        #AQUÍ SE DEBERÍA HASHEAR "password"
        user = User(username, password, question)
        return user
    
    """
    Descripción: Como Usuario quiero actualizar el nombre de usuario para poder ingresar al sistema con otro nombre.
    Criterios de aceptación: Dado un usuario, cuando desea actualizar el nombre de usuario, entonces el sistema pregunta por el nuevo 
    nombre y verifica si hay algún usuario con ese nickname, si lo hay, el sistema envía un mensaje de error y le solicita otro nombre 
    de usuario y, si no hay usuario existente con el mismo nombre, entonces se actualiza.
    """
    def update_username(username):
        confirm = False
        while (not confirm):
            username = input("Ingresa el nuevo nombre de usuario: ")
            if(check_username(username)):
                print("El nuevo nombre de usuario es " + username + " ¿Confirmas el nombre de usuario?")
                choice = input("1) Confirmar. \n2) Cancelar")
                if choice == "1":
                    confirm = True
            else:
                print("Nombre de usuario existente! Por favor, escribe un nombre de usuario distinto.\n")

        user_password = input("Ingresa tu contraseña de usuario: ")
        while (not confirm_password(username, user_password)):
            user_password = input("Ingresa tu contraseña de usuario: ")
        return username
    
    """
    Descripción: Como Usuario quiero actualizar mi contraseña de usuario para que poder ingresar al sistema con una nueva contraseña.

    Criterios de aceptación: Dado un usuario, cuando desea actualizar su contraseña, entonces el sistema pregunta por la nueva 
    contraseña y, si cumple con todos los requisitos entonces el sistema actualiza la contraseña, sino, envía un mensaje de error y 
    vuelve a solicitar la nueva contraseña.
    La contraseña debe cumplir con:
        Longitud mínima: 8.
    y los caracteres permitidos son:
        números de 0 a 9.
        Letras de A hasta Z y a hasta z.
        Caracteres especiales: ° . ! ” # $ % & / ( ) < = > ¿ ? ¡ { } * _ - + . [ ] @ [ ^ ;
    """

    def update_user_password(user, question):
        # update password
        password = input("Ingresa la nueva contraseña: ")
        confirmpassword = input("Confirma la nueva contraseña: ")
        while (not check_password(password, confirmpassword)):
            password = input("Ingresa la nueva contraseña: ")
            confirmpassword = input("Confirma la nueva contraseña: ")

        # confirm change
        confirm = False
        while (not confirm):
            answer = input("Para confirmar, por favor responde la siguiente pregunta\n¿Cuál es el nombre de la primera escuela a la que ingresaste?: ")
            print("La respuesta es '" + answer + "' ¿Confirmas tu respuesta?")
            choice = input("1) Confirmar. \n2) Cancelar")
            if choice == "1":
                if answer == question:
                    confirm = True
                else:
                    print("Respuesta incorrecta! Por favor inténtalo otra vez.")
        return password
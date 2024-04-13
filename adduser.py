from common import *

class User:
    def __init__(self, username, password, question):
        self.username = None
        self.password = None
        self.question = None

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
        # Get user input
        
        
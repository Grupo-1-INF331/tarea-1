from common import *

class Password:
    def __init__(self, keyword, password, username):
        self.keyword = keyword
        self.password = password
        self.username = username

    # Métodos de instancia

    """
    Descripción: Como Usuario quiero agregar una contraseña para poder almacenarla en el sistema.
    Criterios de aceptación: Dado un usuario, cuando desea ingresar una contraseña, entonces el sistema pregunta por la nueva contraseña 
    y, si cumple con todos los requisitos entonces el sistema ingresa la contraseña, sino, envía un mensaje de error y vuelve a 
    solicitar la nueva contraseña. O también se puede usar la opción de "generar contraseña". Y para finalizar, requiere de una palabra
    clave la cual no debe estar repetida en alguna otra contraseña.
    """
    def create_password(username):
        # Define word key
        confirm = False
        while (not confirm):
            keyword = input("Ingresa la palabra clave para referenciar tu nueva contraseña: ")
            print("La palabra clave escogida es " + keyword + " ¿Estás seguro que esta es la palabra correcta?")
            choice = input("1) Confirmar. \n2) Cancelar")
            if choice == "1":
                confirm = True

        # Define password
        password = input("Ingresa la nueva contraseña: ")
        confirmpassword = input("Confirma la nueva contraseña: ")
        while (not check_password(password, confirmpassword)):
            password = input("Ingresa la nueva contraseña: ")
            confirmpassword = input("Confirma la nueva contraseña: ")
        #AQUÍ SE DEBERÍA ENCRIPTAR "password"
        password = Password(keyword, password, username)
        return password
    
    """
    Descripción: Como Usuario quiero visualizar alguna contraseña para poder usar la contraseña.
    Criterios de aceptación: Dado un usuario, cuando desea visualizar alguna contraseña, entonces el sistema pide la contraseña del 
    usuario. Si se escribió correctamente, se puede visualizar la contraseña, sino, se pide nuevamente la clave.
    """
    def read_password(username):
        keyword = input("Ingresa la palabra clave asociada a la contraseña que quieres visualizar: ")
        wb = load_workbook('users_data.xlsx')
        hoja = wb.worksheets[0]
        for fila in hoja.iter_rows(min_row = 2):
            val_row = [celda.value for celda in fila]
            if val_row[0] == username :
                user_db = wb.worksheets[int(val_row[2])]
                for row in user_db.iter_rows(min_row=2):
                    val_fila = [celda.value for celda in row]
                    if keyword == val_fila[0]: 
                        user_password = input("Ingresa la contraseña de usuario: ")
                        while (not confirm_password(username, user_password)):
                            user_password = input("Ingresa la contraseña de usuario: ")
                        return(val_fila[1]) # AQUÍ DEBERÍA DESENCRIPTAR
        return "Palabra clave no encontrada!\n"

    """
    Descripción: Como Usuario quiero actualizar la palabra clave de alguna contraseña para actualizar el uso de la clave.
    Criterios de aceptación: Dado un usuario, cuando desea actualizar la palabra clave de alguna contraseña, entonces el sistema 
    requiere la nueva palabra clave y, luego de que el usuario la escribe, se solicita la confirmación la cual es ingresar la clave del
    usuario. Si el usuario confirma el cambio, entonces se actualiza la palabra clave, sino, se vuelve a requerir la nueva palabra clave.
    """
    def update_wordKey(username):
        # update word key
        confirm = False
        while (not confirm):
            keyword = input("Ingresa la nueva palabra clave para referenciar tu nueva contraseña: ")
            print("La palabra clave escogida es " + keyword + " ¿Estás seguro que es la palabra correcta?")
            choice = input("1) Confirmar. \n2) Cancelar")
            if choice == "1":
                confirm = True

        # confirm change
        user_password = input("Ingresa la contraseña de usuario: ")
        while (not confirm_password(username, user_password)):
            user_password = input("Ingresa la contraseña de usuario: ")
        return keyword
    
    """
    Descripción: Como Usuario quiero actualizar alguna contraseña para actualizar el uso de la clave.
    Criterios de aceptación: Dado un usuario, cuando desea actualizar alguna contraseña, entonces el sistema pregunta por la nueva 
    contraseña y, si cumple con todos los requisitos entonces el sistema actualiza la contraseña, sino, envía un mensaje de error y 
    vuelve a solicitar la nueva contraseña. O también se puede usar la opción de "generar contraseña". Y para confirmar el cambio, se 
    solicitará la confirmación la cual es ingresar la clave del usuario. Si el usuario confirma el cambio, entonces se actualiza clave,
    sino, se vuelve a requerir la nueva clave.
    """
    def update_password(username):
        # update password
        password = input("Ingresa la nueva contraseña: ")
        confirmpassword = input("Confirma la nueva contraseña: ")
        while (not check_password(password, confirmpassword)):
            password = input("Ingresa la nueva contraseña: ")
            confirmpassword = input("Confirma la nueva contraseña: ")

        # confirm change
        user_password = input("Ingresa la contraseña de usuario: ")
        while (not confirm_password(username, user_password)):
            user_password = input("Ingresa la contraseña de usuario: ")
        return password
    
    """
    Descripción: Como Usuario quiero eliminar alguna contraseña para gestionar mis contraseñas.
    Criterios de aceptación: Dado un usuario, cuando desea eliminar alguna contraseña, entonces el sistema pregunta por la palabra clave
    y, luego, se debe escribir la contraseña del usuario para confirmar la eliminación de la clave. Si la contraseña del usuario es 
    correcta, entonces se elimina la clave, sino, se pregunta nuevamente por la contraseña del usuario.
    """
    def delete_password(username):
        keyword = input("Ingresa la palabra clave asociada a la contraseña que quieres visualizar: ")
        wb = load_workbook('users_data.xlsx')
        hoja = wb.worksheets[0]
        row_index = 1
        for fila in hoja.iter_rows(min_row = 2):
            val_row = [celda.value for celda in fila]
            if val_row[0] == username :
                user_db = wb.worksheets[int(val_row[2])]
                for row in user_db.iter_rows(min_row=2):
                    val_fila = [celda.value for celda in row]
                    if keyword == val_fila[0]: 
                        user_password = input("Ingresa la contraseña de usuario: ")
                        while (not confirm_password(username, user_password)):
                            user_password = input("Ingresa la contraseña de usuario: ")
                        user_db.delete_rows(2)
                        wb.save('users_data.xlsx')
                        return("Contraseña eliminada con éxito!")
            row_index += 1
        return "Palabra clave no encontrada!\n"
    
    """
    Descripción: Como Usuario quiero buscar alguna contraseña para conocer cuales y/o cuantas contraseñas tengo registradas en el 
    sistema.
    Criterios de aceptación: Dado un usuario, cuando desea buscar alguna contraseña, entonces el sistema despliega una lista con las 
    palabras claves de las contraseñas.
    """

    def read_all_password(username):
        wb = load_workbook('users_data.xlsx')
        hoja = wb.worksheets[0]
        for fila in hoja.iter_rows(min_row = 2):
            val_row = [celda.value for celda in fila]
            if val_row[0] == username :
                user_db = wb.worksheets[int(val_row[2])]
                for row in user_db.iter_rows(min_row=3):
                    val_fila = [celda.value for celda in row]
                    print(" - " + val_fila[0])
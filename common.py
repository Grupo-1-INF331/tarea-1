from openpyxl import load_workbook

def check_username(username):
    wb = load_workbook('users_data.xlsx')
    hoja = wb.worksheets[0]
    repetido = False
    for fila in hoja.iter_rows(min_row = 2):
        val_row = [celda.value for celda in fila]
        if val_row[0] == username :
            repetido = True
    return repetido

def check_password(password, confirmpassword):
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
    return True

def confirm_username(username):
    wb = load_workbook('users_data.xlsx')
    hoja = wb.worksheets[0]
    for fila in hoja.iter_rows(min_row = 2):
        val_row = [celda.value for celda in fila]
        if val_row[0] == username :
            return True
    print("El nombre de usuario ingresado no existe!\n")
    return False

def confirm_password(username, password):
    wb = load_workbook('users_data.xlsx')
    hoja = wb.worksheets[0]
    for fila in hoja.iter_rows(min_row = 2):
        val_row = [celda.value for celda in fila]
        if val_row[0] == username :
            user_db = wb.worksheets[int(val_row[2])]
            for row in user_db.iter_rows(min_row=2, max_row=2):
                val_fila = [celda.value for celda in row]
                if password == val_fila[1]: 
                    return True
    print("Contraseña errónea!\n")
    return False
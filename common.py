import random

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

def generate_password():
    # Define the default characters
    numbers = '0123456789'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    special_chars = '°.!\"#$%&/()<=>?¡{}*_+-.[\]@[;^'
    
    # Prompt user for the password length
    length = int(input("Ingrese la longitud de contraseña deseada (mínimo 8): "))
    while length < 8:
        length = int(input("Longitud demasiado corta. Por favor ingrese un mínimo de 8: "))
    
    # Allow users to add or remove characters
    print("Se utiliza el juego de caracteres predeterminado. ¿Quieres personalizarlo? (si/no): ")
    customize = input().strip().lower()
    
    allowed_characters = numbers + letters + special_chars
    if customize == 'si':
        print("Ingrese su conjunto personalizado de caracteres: ")
        allowed_characters = input()
    
    # Generate the password
    password = ''.join(random.choice(allowed_characters) for _ in range(length))
    return password
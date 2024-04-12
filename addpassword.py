class Password:
    def __init__(self, word_key, password, username):
        self.word_key = word_key
        self.password = password
        self.username = username

    # Métodos de instancia

    def create_password(username):
        # Define word key
        confirm = False
        while (not confirm):
            word_key = input("Ingresa la palabra clave para referenciar tu nueva contraseña: ")
            print("La palabra clave escogida es " + word_key + " ¿Estás seguro que esta sea la palabra correcta?")
            choice = input("1) Confirmar. \n2) Cancelar")
            if choice == "1":
                confirm = True

        # Define password
        password = input("Enter password: ")
        confirmpassword = input("Confirm password: ")
        while (not check_password(password, confirmpassword)):
            password = input("Enter password: ")
            confirmpassword = input("Confirm password: ")
        password = Password(word_key, password, username)
        return password
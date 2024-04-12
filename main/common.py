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
from User import *
from addpassword import *
from common import *

# Import necessary modules or packages

# Define any global variables or constants

# Define any helper functions or classes


# Define the main function
def main():
    # user1 = User()
    # Example usage
    password = "SecurePassword123!"
    hashed = hash_password(password)

    # Encrypt and decrypt a password
    password = "SecurePassword123!"
    encrypted = encrypt_password(password, hashed)
    print("Encrypted:", encrypted)

    decrypted = decrypt_password(encrypted, hashed)
    print("Decrypted:", decrypted)
    
    # Your code goes here


# Check if the file is being run as the main program
if __name__ == "__main__":
    # Call the main function
    main()

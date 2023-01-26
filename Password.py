import random
import string

# Longitud deseada de la contraseña
password_length = 22

# Caracteres permitidos en la contraseña
characters = string.ascii_letters + string.digits + string.punctuation

password = []

# print(characters)

for i in range(password_length):
    part = random.choice(characters)
    password.append(part)


password = ''.join(password)
print(password)

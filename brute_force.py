import hashlib  # Para crear los hashes MD5

# Función que compara el hash de la contraseña real con las palabras de un diccionario
def fuerza_bruta(hashed_password, diccionario):
    try:
        with open(diccionario, 'r') as archivo:  # Abrimos el archivo que contiene las contraseñas
            for palabra in archivo.readlines():  # Leemos línea por línea
                palabra = palabra.strip()  # Quitamos espacios y saltos de línea
                # Calculamos el hash MD5 de la palabra actual
                intento_hash = hashlib.md5(palabra.encode()).hexdigest()
                
                # Comparamos el hash de la palabra con el hash de la contraseña almacenada
                if intento_hash == hashed_password:
                    print(f"¡Contraseña encontrada!: {palabra}")
                    return True
        print("No se encontró la contraseña en el diccionario.")
        return False

    except FileNotFoundError:
        print("El archivo de diccionario no existe.")
        return False

# Ejemplo: Hash de la contraseña almacenada (md5 de "12345")
hashed_password = hashlib.md5("12345".encode()).hexdigest()

# Iniciamos el ataque de fuerza bruta
fuerza_bruta(hashed_password, "diccionario.txt")
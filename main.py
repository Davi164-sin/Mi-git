import matplotlib.pyplot as plt
import hashlib
import getpass

#Datos de usuarios
usuarios = {
    "david": hashlib.sha256("1234".encode()).hexdigest()
}

#Trabajos
trabajos = [
    {
        "nombre": "AuthMaster",
        "descripcion": "Proyecto de autenticación segura",
        "tecnologias": ["Python", "Hashing", "Autenticación"],
        "estado": "En desarrollo"
    }
]

#Intentos
intentos = 0
intentos_max = 3
intentos_fallidos = []

def autenticar_usuario(nombre, contraseña):
    if nombre in usuarios:
        contraseña_hash = hashlib.sha256(contraseña.encode()).hexdigest()
        return usuarios[nombre] == contraseña_hash
    return False

def main():
    global intentos
    while intentos < intentos_max:
        nombre = input("Ingrese su nombre: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        
        if autenticar_usuario(nombre, contraseña):
            print("Bienvenido", nombre)
            while True:
                print("1. Trabajos")
                print("2. Modificar")
                print("3. Buscar dato por su índice")
                print("4. Salir")
                opciones = input("Elige una opción: ")
                
                if opciones == "1":
                     print(trabajos)
                elif opciones == "2":
                     print("Modificar")
                elif opciones == "3":
                     trabajos_index = trabajos.index[("AuthMaster")]
                     print(trabajos_index)
                elif opciones == "4":
                    break
                else:
                    print("Opción inválida")


            break
        else:
            intentos += 1
            intentos_fallidos.append(intentos)
            print(f"Acceso denegado. Intentos restantes: {intentos_max - intentos}")

    if intentos == intentos_max:
        print("No hay más intentos")

    if intentos_fallidos:
        plt.plot(intentos_fallidos)
        plt.title("Intentos fallidos de autenticación")
        plt.xlabel("Intentos")
        plt.ylabel("Número de intento")
        plt.show()

if __name__ == "__main__":
    main()

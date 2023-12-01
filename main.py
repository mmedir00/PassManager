from passGenerator import *
from cypher import *
from saveManager import *
import os

def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    path = "passwords.txt"
    cyph = cypher()

    print("-----BIENVENIDO A PASSMANAGER-----\n\n")
    print("1. Generar contraseña\n2. Guardar contraseña\n3. Ver contraseña\n4. Ver todas\n5. Borrar todas\n\nE. Salir\n")
    option = input("Ingrese una opcion: ")


    if option == "1":
        num = int(input("\nIngrese la cantidad de caracteres: "))

        print("Su contraseña es: " + passGenerator.generate(num))
        input("\nPresione enter para continuar")

        main()


    elif option == "2":
        page = str(input("\nIngrese la pagina: "))
        user = str(cyph.encrypt(str(input("Ingrese el usuario: "))))
        password = str(cyph.encrypt(str(input("Ingrese la contraseña: "))))

        saveManager(path).append(page + "/" + user + "/" + password + "\n")
        print("Guardado con exito")
        input("\nPresione enter para continuar")

        main()
    elif option == "3":
        try:
            page = str(input("\nIngrese la pagina: "))
            cUser = saveManager(path).getUser(page)
            cPass = saveManager(path).getPass(page)
            rUser = str(cyph.decrypt(cUser[2:-1]))[2:-1]
            rPass = str(cyph.decrypt(cPass[2:-1]))[2:-1]

            print("\n\nPagina: " + page + "\nUsuario: " + rUser + "\nSu contraseña es: " + rPass)
        except:
            print("\nNo se encontro ningun usuario y contraseña vinculados a la pagina")
        input("\nPresione enter para continuar")

        main()

    elif option == "4":
        print("\n\n\t" +"Pagina".ljust(15, ' ') + "\t║\t" + "Usuario".ljust(15, ' ') + "\t║\t" + "Contraseña".ljust(15, ' '))
        print("════════════════════════╬═══════════════════════╬════════════════════════")
        for i in saveManager(path).getInfo():
            print("\t"+i[0].ljust(15, ' ') + "\t║\t" + str(cyph.decrypt(i[1][2:-1]))[2:-1].ljust(15, ' ') + "\t║\t" + str(cyph.decrypt(i[2][2:-1]))[2:-1].ljust(15, ' '))
        input("\nPresione enter para continuar")

        main()

    elif option == "5":
        if (input("\nEsta seguro que desea borrar todas las contraseñas? (y/n): ") == ("y" or "Y") and input("\nToda la información se borrará (y/n): ") == ("y" or "Y")):
            saveManager(path).clear()
            print("\nBorrado con exito")
        else:
            print("\nOperacion cancelada")

        input("\nPresione enter para continuar")
        main()

    elif option == ("e" or "E"):
        exit()

    else:
        print("\nOpcion invalida")
        input("\nPresione enter para continuar")

        main()


main()
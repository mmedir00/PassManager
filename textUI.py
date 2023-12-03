import os
import logging
from datetime import datetime 

from passGenerator import *
from cypher import *
from saveManager import *
from autentification import *

date = datetime.now().strftime("%Y-%m-%d_%H:%M")


class TextUI:

    logging.basicConfig(filename=f"logs/{date}.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    path = "etc/passwords"
    cyph = cypher()
    
    def clean(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def init(self):

        self.clean()


        option = input("--------PASSMANAGER--------\n\n\n1. Generar contraseña\n2. Guardar contraseña\n3. Ver contraseña\n4. Ver todas\n5. Borrar todas\n6. Cambiar contraseña maestra\n\nE. Salir\n\nIngrese una opcion: ")


        if option in ["1"]:
            num = int(input("\nIngrese la cantidad de caracteres: "))

            print("Su contraseña es: " + passGenerator.generate(num))
            logging.info("Password generated")
            input("\nPresione enter para continuar")

            self.init()


        elif option in ["2"]:
            page = str(input("\nIngrese la pagina: "))
            user = str(self.cyph.encrypt(str(input("Ingrese el usuario: "))))
            password = str(self.cyph.encrypt(str(input("Ingrese la contraseña: "))))

            if len(saveManager(self.path).getUser(page)) != 0:
                print("Ya existe un usuario y contraseña vinculados a la pagina")
                logging.info(page + " password already exists")
            else: 
                saveManager(self.path).append(page + "/" + user + "/" + password + "\n")
                print("Guardado con exito")
                logging.info(page + " password saved")
            input("\nPresione enter para continuar")

            self.init()


        elif option in ["3"]:
            try:
                page = str(input("\nIngrese la pagina: "))
                cUser = saveManager(self.path).getUser(page)
                cPass = saveManager(self.path).getPass(page)
                rUser = str(self.cyph.decrypt(cUser[2:-1]))[2:-1]
                rPass = str(self.cyph.decrypt(cPass[2:-1]))[2:-1]

                print("\n\nPagina: " + page + "\nUsuario: " + rUser + "\nSu contraseña es: " + rPass)
                logging.warning(page + " password retrieved")
            except:
                print("\nNo se encontro ningun usuario y contraseña vinculados a la pagina")
                logging.info(page + " password not found")
            input("\nPresione enter para continuar")

            self.init()


        elif option in ["4"]:
            print("\n\n\t" +"Pagina".ljust(15, ' ') + "\t║\t" + "Usuario".ljust(15, ' ') + "\t║\t" + "Contraseña".ljust(15, ' '))
            print("════════════════════════╬═══════════════════════╬════════════════════════")
            for i in saveManager(self.path).getInfo():
                print("\t"+i[0].ljust(15, ' ') + "\t║\t" + str(self.cyph.decrypt(i[1][2:-1]))[2:-1].ljust(15, ' ') + "\t║\t" + str(self.cyph.decrypt(i[2][2:-1]))[2:-1].ljust(15, ' '))
            logging.warning("All passwords retrieved")
            input("\nPresione enter para continuar")

            self.init()


        elif option in ["5"]:
            if self.passModule():
                if (input("\nEsta seguro que desea borrar todas las contraseñas? (y/n): ") in  ["y", "Y"] and input("\nToda la información se borrará (y/n): ") in ["y", "Y"]):
                    saveManager(self.path).clear()
                    print("\nBorrado con exito")
                    logging.warning("All passwords deleted")
                else:
                    logging.info("All passwords deletion cancelled")
                    print("\nOperacion cancelada")
            else:
                logging.info("All passwords deletion cancelled")
                print("\nContraseña incorrecta. Operacion cancelada")

            input("\nPresione enter para continuar")

            self.init()


        elif option in ["6"]:
            if self.passModule():
                password = str(input("\nIngrese la nueva contraseña maestra: "))
                authentification().change(password)
                logging.warning("Master password changed")
                print("\nContraseña cambiada con exito")
                input("\nPresione enter para continuar")

            self.init()


        elif option in ["e", "E", "exit", "Exit"]:
            logging.debug("Program ended")
            exit()


        else:
            print("\nOpcion invalida")
            logging.info("Invalid option")
            input("\nPresione enter para continuar")

            self.init()


    def passModule(self):
        self.clean()
        password = str(input("\nIngrese la clave maestra: "))
        if authentification().check(password):
            logging.debug("Program started")
            return True
        else:   
            print("Contraseña incorrecta")
            return False

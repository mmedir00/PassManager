
# PassManager

A password manager made in python for using in the terminal, it cyphers all your passwords and users. Uses a master password to secure only you can see your passwords, also uses a logger to capture when someone sees your passwords.


## Run Locally

- Clone the project

    Using HTTPS:
    ```bash
    git clone https://github.com/mmedir00/PassManager.git
    ```
    Using SSH:
    ```bash
    git clone git@github.com:mmedir00/PassManager.git
    ```
- Go to the project directory

    ```bash
    cd PassManager
    ```

- Start PYCalc

    ```bash
    python3 main.py
    ```

## Used technologies

 - [Python 3.10.12](https://www.python.org/downloads/release/python-31012/)
 - [pyca/cryptography](https://cryptography.io/en/latest/)
 - [Random](https://docs.python.org/es/3.10/library/random.html)
 - [Logging](https://docs.python.org/3.10/library/logging.html)
 - [os](https://docs.python.org/3.10/library/os.html)
 - [datetime](https://docs.python.org/3.10/library/datetime.html)
## How to use

Is a basis text GUI, where once introduced the master password ("PassManager" by defoult) you can select from a menu.
 ```
 --------PASSMANAGER--------


1. Generar contraseña
2. Guardar contraseña
3. Ver contraseña
4. Ver todas
5. Borrar todas
6. Cambiar contraseña maestra

E. Salir

Ingrese una opcion: 
 ```

- "1": generate a new password randomly.
- "2": save a new user-password.
- "3": see some user and password, searching it from the page related to them.
- "4": reveal all users and passwords with its pages.
- "5": deleting all your passwords.
- "6": change your master password.
- "e", "E", "exit", "Exit": get out the password manager. 

Some actions may require the master password.

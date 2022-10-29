print("\x1b[1;33m"+"______        _         _      _            ___  _____  _____  ")      
print(  "|  _  \      (_)       (_)    | |          |_  ||  __ \/  __ \ ")
print(  "| | | |  ___  _ __   __ _   __| |            | || |  \/| /  \/ ")
print(  "| | | | / _ \| |\ \ / /| | / _` |            | || | __ | |     ")
print(  "| |/ / |  __/| | \ V / | || (_| |        /\__/ /| |_\ \| \__/\ ")
print(  "|___/   \___||_|  \_/  |_| \__,_|        \____/  \____/ \____/ ")
print(  "                                  ______                       ")
print(  "                                 |______|                      ")
print("Este script fue creado por")
print("\x1b[4;31m"+"@Deivid_JGC")
print("\x1b[4;34m"+"Deivid 🤠👍#3871")

import hashlib

encontrada = 0
input_hash = input("Inserte la Contraseña Hasheada: ")
pass_doc = input("Inserta el diccionario: ")

try:
    pass_file = open(pass_doc, 'r')
except:
    print("Error:" + pass_doc + " No ha Sido Encontrada :( ")

for palabra in pass_file:
    palabra_cifrada = palabra.incode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.script())
    digest = palabra_hasheada.hexdigest()

    if digest == input_hash:
        print("Contraseña Encontrada :D \n La contraseña es: " + palabra)
        encontrada = 1
        break

if not encontrada:
    print("Contraseña no encontrada :(( " + pass_doc)
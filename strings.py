


s = "Hello"
print(f"str[1]: {s[1]}") #e

#Upper
print(f"str.upper(): {s.upper()}") #HELLO pone todo en mayus

#lower() = hello pone todo en minuscula

#strip() = hello elimina caracteres no imprimibles y espacios en blanco

#replace() reemplaza un caracter por otro ej: replace("e", "a") = hallo

#find() ejemplo find(e) = 1 (H(0), E(1), L(2), L(3), O(4)

#join()
string=["Hello", "World"]
print(f"str.join(string): {' '.join(string)}") # Hello World

#lstrip() elimina espacios en blanco de la izquierda
#rstrip() elimina espacios en blanco de la derecha

#center() ejemplo "hola".center(10, '-') alinea el texto en el centro

#ljust() alinea a la izq
#rjust() alinea a la derecha

#zfill() rellena con 0 delante dl numero hasta la posicion especificada ej: "42".zfill(5) = 00042

#isdigit() pregunta si son digitos y devuelve booleano

#isdecimal() pregunta si son numeros y devuelve booleano

"""Como insertar una variable dentro de un texto"""

name = "Alice"
print(f"f\"texto{{variable}}\":Hello, {name}!")
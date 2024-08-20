import random

def crear_matriz_clientes(n,m):
    '''
    pre: recibe n y m. Donde n: filas y m: columnas
    pos: devuelve una matriz de NxM creada con ceros
    '''
    
    return [
        ["id_cliente", "nombre","contacto","fecha_alta"],
        [1, "Fernando","fernando@gmail.com", "12/08/2024"],
        [2, "Bautista", "bautista@gmail.com", "04/05/2024"],
        [3, "Francisco", "francisco@gmail.com", "25/09/2023"],
        [4, "Johanna", "johanna@gmail.com", "30/03/2024"]
    ]

def llenar_matriz(m):
    '''
    pre: recibe una matriz ya creada.
    pos: llena la matrizcon valores aleatorios entre 1 y 10.
    '''
    filas = len(m) # Cantidad de filas
    columnas = len(m[0]) # Cantidad de columnas
    for fil in range(filas):
        for col in range(columnas):
            num_aleatorio = random.randint(1,10)
            m[fil][col] = num_aleatorio
    
def imprimir_matriz(matriz):
    '''
    pre: recibe una matriz ya creada.
    pos: muestra por consola los elementos de la matriz.
    '''
    filas = len(matriz)
    columnas = len(matriz[0])
    for fil in range(filas):
        for col in range(columnas):
            '''
            Esta es una cadena de formato que se usa para dar formato al valor de matriz.
            "%3d" es un especificador de formato:
            3 indica que el número debe tener al menos 3 espacios.
            d significa que el valor es un entero (decimal).
            '''
            print("%3d" % matriz[fil][col], end="")
        print()
        
def mostrar_matriz_xfila(m):
    for fila in m:
        print(fila)
        

#Programa principal:
matriz = crear_matriz_clientes(5,4)
llenar_matriz(matriz)
imprimir_matriz(matriz)
help(llenar_matriz)

mostrar_matriz_xfila(matriz)

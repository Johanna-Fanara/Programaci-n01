from datetime import datetime

libros = [
    {'id': 1, 'titulo': '1984', 'autor': 'George Orwell', 'disponible': True},
    {'id': 2, 'titulo': 'El Gran Gatsby', 'autor': 'F. Scott Fitzgerald', 'disponible': True},
    # Agrega más libros aquí
]

# Listas para registrar préstamos y ventas
prestamos = []  # (fecha, id_libro, monto)
ventas = []     # (fecha, id_libro, monto)

def agregar_libro(id, titulo, autor):
    """Agrega un nuevo libro a la biblioteca."""
    libros.append({'id': id, 'titulo': titulo, 'autor': autor, 'disponible': True})
    print(f"Libro '{titulo}' agregado correctamente.")

def registrar_prestamo(id_libro, monto):
    """Registra un préstamo de libro."""
    libro = next((libro for libro in libros if libro['id'] == id_libro), None)
    if libro and libro['disponible']:
        libro['disponible'] = False
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        prestamos.append((fecha, id_libro, monto))
        print(f"Préstamo registrado para el libro ID {id_libro}.")
    else:
        print(f"El libro ID {id_libro} no está disponible para préstamo.")

def registrar_venta(id_libro, monto):
    """Registra una venta de libro."""
    libro = next((libro for libro in libros if libro['id'] == id_libro), None)
    if libro:
        libro['disponible'] = False
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ventas.append((fecha, id_libro, monto))
        print(f"Venta registrada para el libro ID {id_libro}.")
    else:
        print(f"El libro ID {id_libro} no existe.")

def mostrar_prestamos():
    """Muestra la lista de préstamos registrados."""
    print("Lista de Préstamos:")
    for prestamo in prestamos:
        fecha, id_libro, monto = prestamo
        libro = next((libro for libro in libros if libro['id'] == id_libro), None)
        titulo = libro['titulo'] if libro else "Desconocido"
        print(f"Fecha: {fecha}, ID Libro: {id_libro}, Título: {titulo}, Monto: {monto}")

def mostrar_ventas():
    """Muestra la lista de ventas registradas."""
    print("Lista de Ventas:")
    for venta in ventas:
        fecha, id_libro, monto = venta
        libro = next((libro for libro in libros if libro['id'] == id_libro), None)
        titulo = libro['titulo'] if libro else "Desconocido"
        print(f"Fecha: {fecha}, ID Libro: {id_libro}, Título: {titulo}, Monto: {monto}")

# Esto es chatGPT pero lo tomo como modelo o idea para moldear bien la pagina :)
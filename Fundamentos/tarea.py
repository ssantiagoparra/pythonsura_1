# Formulario para crear un cliente

# Solicita el nombre del cliente (tipo str)
nombre = input("Ingrese el nombre del cliente: ")

# Solicita la dirección del cliente (tipo str)
direccion = input("Ingrese la dirección del cliente: ")

# Solicita el teléfono del cliente y lo convierte a entero (tipo int)
telefono = int(input("Ingrese el teléfono del cliente (solo números): "))

# Imprime los datos del cliente usando diferentes métodos de formateo
print("\n--- Cliente creado ---")
print("Nombre: {}".format(nombre))  # Formateo con .format() para cadenas
print("Dirección: {}".format(direccion))  # Formateo con .format() para cadenas
print("Teléfono: {:d}".format(telefono))  # Formateo con .format() para enteros

# Formulario para crear un producto

# Solicita el nombre del producto (tipo str)
producto = input("\nIngrese el nombre del producto: ")

# Solicita el peso del producto y lo convierte a flotante (tipo float)
peso = float(input("Ingrese el peso del producto (kg): "))

# Solicita el precio del producto y lo convierte a flotante (tipo float)
precio = float(input("Ingrese el precio del producto ($): "))

# Solicita la cantidad del producto y lo convierte a entero (tipo int)
cantidad = int(input("Ingrese la cantidad del producto: "))

# Imprime los datos del producto usando diferentes métodos de formateo
print("\n--- Producto creado ---")
print("Producto: %s" % producto)  # Formateo con el operador % para cadenas
print("Peso: %.2f kg" % peso)  # Formateo con el operador % para mostrar dos decimales
print("Precio: ${:.2f}".format(precio))  # Formateo con .format() para mostrar dos decimales
print("Cantidad: {}".format(cantidad))  # Formateo con .format() para enteros
print("Valor total: ${:.2f}".format(precio * cantidad))  # Calcula el valor total y lo muestra con dos decimales ###
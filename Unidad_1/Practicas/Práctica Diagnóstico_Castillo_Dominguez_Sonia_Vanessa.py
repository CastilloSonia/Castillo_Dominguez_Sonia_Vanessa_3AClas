# Práctica diagnóstico_Vanessa.py
# Simulador de ticket de venta.
# Objetivo: Aplicar funciones, bucles, condiciones.
# Listas y variables.

# Elegir una temática de un negocio que vende 3 productos-

productos = ["Pan de muerto", "Empanadas de piña", "Bolillo"]
precios = [20, 12, 4]

# Función para calcular el total
def calcular_total(cantidades, precios):
    total = 0
    for i in range (len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Menú de usuario.
print("Bienvenido a la Panadería")
nombre = input("Ingresa tu nombre: ")

cantidades = []
print("Realiza tu pedido: ")
for i in range(len(productos)):
    print(f"{i + 1}. {productos[i]} = ${precios[i]}")
    cantidad = int(input(f"¿Cuántos {productos[i]} desea? "))
    cantidades.append(cantidad)

print("\n\t ***** TICKET DE VENTA *****")
print("-" * 40)
total = calcular_total(cantidades, precios)
for i in range(len(productos)):
    if cantidades[i] > 0:
        print(f"\n\t {cantidades[i]} | {productos[i]} = ${cantidades[i] * precios[i]}")
if total > 100:
    total *= 0.9
    print("\n\t" + "¡Felicidades! Has ganado un descuento del 10% por comprar más de $100".center(40))
print(f"\n\t Gracias por tu compra, {nombre}")
print(f"\n\t ****El total a pagar es: ${total}****")
import sys
"""

cosas del producto:

producto_codigo_lista
producto_nombre_lista
producto_precio_lista


cosas del cliente:
cliente_producto_lista
cliente_cantidad_lista
cliente_codigo_producto
cliente_cantidad_producto


pedido:
pedido_lista

"""

producto_codigo_lista = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

producto_nombre_lista = ["Botas punta de acero", "Bota alta con punta de acero", "Bota alta", "Casco", "Barbiquejo",
               "Casco con barbiquejo", "Mascarilla con filtro contra vapores y gases", "Respuestos de mascarilla con filtro",
               "Filtro contra polvos y olores", "Respirador 1 filtro", "Respirador contra polvo con filtro", "Gauntes anticorte",
               "Guantes de seguridad", "Guante de soldador", "Lentes de seguridad", "Orejera para cascos con cancelación de ruido"]

producto_precio_lista = [150, 150, 50, 44, 5, 50, 120, 50, 80, 14, 20, 20, 30, 30, 10, 130]

cliente_codigo_lista =[]
cliente_cantidad_lista =[]

pedido_lista =[]

pedido_lista.append(cliente_codigo_lista)
pedido_lista.append(cliente_cantidad_lista)

def añadir_producto(producto_codigo_lista, producto_nombre_lista, producto_precio_lista):
    print("\n\nLISTADO DE PRODUCTOS Y PRECIO(BRUTO) :\n")
    for i in range(16):
        print(f"{producto_codigo_lista[i]}. {producto_nombre_lista[i]} = ${producto_precio_lista[i]}")
    print("\n")
    cliente_codigo_producto = input("Ingrese el número de la opción que quiere agregar al carrito: ")
    cliente_codigo_producto=int(cliente_codigo_producto)
    return cliente_codigo_producto

def añadir_cantidad():
    cliente_cantidad_producto = input("Ingrese la cantidad deseada:")
    cliente_cantidad_producto= int(cliente_cantidad_producto)
    print("\n")
    return cliente_cantidad_producto

def mostrar_compra(cliente_codigo_producto, cliente_cantidad_producto):
    print("El codigo del producto que escogiste es: " + str(cliente_codigo_producto)+"\nLa cantidad que escogiste es:"+ str(cliente_cantidad_producto))


def mostrar_carrito(producto_codigo_lista, producto_nombre_lista, producto_precio_lista, cliente_cantidad_lista,cliente_codigo_lista):
    n=0
    print("CARRITO:\n\n"+
          "Codigo de Producto/ Nombre de Producto/Precio xU/ Cantidad de Producto/ SubTotal del producto")
    for n in range(len(cliente_codigo_lista)):
        #muestra el codigo del producto comprado
        print(f"{cliente_codigo_lista[n]}. {producto_nombre_lista[cliente_codigo_lista[n]]}({producto_precio_lista[cliente_codigo_lista[n]]})  Cantidad: {cliente_cantidad_lista[n]}")
    print("\n")

def proceso_pago(producto_codigo_lista, producto_nombre_lista, producto_precio_lista, cliente_cantidad_lista,cliente_codigo_lista):
    print("BOLETA")
    precio_neto=0
    precio_subtotal_producto=0
    precio_bruto=0
    precio_igv=0
    igv=0.18
    precio_subtotal_producto2=0

    print("\nSUBTOTAL POR PRODUCTO\n\n"+
          "Codigo de Producto/ Nombre de Producto/Precio xU\n")
    
    for n in range(len(cliente_codigo_lista)):
        #muestra el codigo del producto comprado
        cantidad = cliente_cantidad_lista[n]
        precio_producto = producto_precio_lista[cliente_codigo_lista[n]]
        precio_subtotal_producto= cantidad * precio_producto
        precio_subtotal_producto2 +=precio_subtotal_producto
        print(f"{cliente_codigo_lista[n]}. {producto_nombre_lista[cliente_codigo_lista[n]]}({producto_precio_lista[cliente_codigo_lista[n]]})\nCantidad: {cliente_cantidad_lista[n]}\nSubTotal por producto= {precio_subtotal_producto}\n")
        precio_subtotal_producto=0

    print("Precio subtotal:"+ str(precio_subtotal_producto2)+"\n")
    precio_igv=precio_subtotal_producto2*igv
    print("IGV:"+ str(round(precio_igv,2))+"\n")
    precio_neto=precio_subtotal_producto2+precio_igv
    print("Total a pagar:"+ str(round(precio_neto,2))+"\n")
    input()


def vista():
    i = 0
    while i != 4:
        print("Menu de Opciones\n" +
                "1. Comprar\n" +
                "2. Ver Carrito\n" +
                "3. Pagar\n" +
                "4. Salir del programa")
        i = int(input("Ingrese su opción: "))
        if i == 1:
            cliente_codigo_producto = añadir_producto(producto_codigo_lista, producto_nombre_lista, producto_precio_lista)
            cliente_cantidad_producto = añadir_cantidad()
            cliente_cantidad_lista.append(cliente_cantidad_producto)
            cliente_codigo_lista.append(cliente_codigo_producto)
            mostrar_compra(cliente_codigo_producto, cliente_cantidad_producto)
            print("\n")
        elif i == 2:
            print("")
            mostrar_carrito(producto_codigo_lista, producto_nombre_lista, producto_precio_lista, cliente_cantidad_lista,cliente_codigo_lista)
        elif i == 3:
            print("")
            proceso_pago(producto_codigo_lista, producto_nombre_lista, producto_precio_lista, cliente_cantidad_lista,cliente_codigo_lista)
        elif i == 4:
            sys.exit()

vista()



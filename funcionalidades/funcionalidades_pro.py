from utils.utils import conexion
from utils.utils import cambio_sql, consulta_sql
import tkinter as tk


# Eliminar un producto
def eliminar_prod():
    print("Eliminar un producto")
    eliminar_producto = int(input("ID del producto a eliminar: "))
    eliminar = conexion.cursor()
    eliminar.execute("DELETE FROM productos WHERE id = ?", (eliminar_producto,))
    conexion.commit()
    print(f"Producto con ID {eliminar_producto} eliminado.")


# Ver empleados
def ver_empleados():
    ver_cursor = conexion.cursor()
    ver_cursor.execute("SELECT * FROM empleados")
    empleados = ver_cursor.fetchall()
    for empl in empleados:
        print(f"Nombre: {empl["nombre"]}, Puesto: {empl['puesto']}")

# Ver ventas
def ver_ventas():
    ventas = consulta_sql("SELECT * FROM ventas")
    for v in ventas:
        print(
            f"ID: {v['id']}, Producto: {v['producto_id']}, Empleado: {v['empleado_id']}, Cantidad: {v['cantidad_vendida']}, Total: {v['total_venta']}")

# Agregar una venta
def agregar_venta():
    producto_id = int(input("ID del producto vendido: "))
    empleado_id = int(input("ID del empleado que realizó la venta: "))
    cantidad_vendida = int(input("Cantidad vendida: "))

    # Obtener precio y stock
    resultado = consulta_sql("SELECT cantidad, precio FROM productos WHERE id = ?",
                             (producto_id,))
    if not resultado:
        print("❌ Producto no encontrado.")
        return

    stock_disponible, precio_unitario = resultado[0]

    if cantidad_vendida > stock_disponible:
        print(f"❌ Stock insuficiente. Solo hay {stock_disponible} unidades.")
        return

    total_venta = cantidad_vendida * precio_unitario

    # Registrar la venta
    cambio_sql("""INSERT INTO ventas (producto_id, empleado_id, cantidad_vendida, fecha, total_venta)
VALUES (?, ?, ?, DATE('now'), ?)""", (producto_id, empleado_id, cantidad_vendida, total_venta))

    # Actualizar el stock
    cambio_sql("""
        UPDATE productos
        SET cantidad = cantidad - ?
        WHERE id = ?
    """, (cantidad_vendida, producto_id))

    print("✅ Venta registrada correctamente.")

# agregar empleado
def empleado():
    nombre = input("Ingresa el nombre del empleado: ")
    puesto = input("Ingresa el puesto: ")

    cambio_sql("INSERT INTO empleados (nombre, puesto) VALUES (?, ?)",
               (nombre, puesto))
    print("Empleado registrado correctamente.")

#eliminar empleado
def eliminar_empleado():
    nombre = input("Ingresa el nombre del empleado: ")
    id_empleado = int(input("Ingresa el id del empleado: "))

    cambio_sql("DELETE FROM empleados WHERE nombre = ? AND id = ?", (nombre, id_empleado,))

# Funcion para editar empleado
def editar_empleado():
    id_empleado = input("Ingrese el ID del empleado a editar: ")
    print("¿Qué desea cambiar del empleado?")
    opcion = input("Nombre o Puesto: ").lower()

    if opcion == "nombre":
        nuevo_nombre = input("Ingrese el nuevo nombre del empleado: ")
        cambio_sql("UPDATE empleados SET nombre = ? WHERE id = ?", (nuevo_nombre, id_empleado))
    elif opcion == "puesto":
        nuevo_puesto = input("Ingrese el nuevo puesto del empleado: ")
        cambio_sql("UPDATE empleados SET puesto = ? WHERE id = ?", (nuevo_puesto, id_empleado))
    else:
        print("Opción no válida. Solo se puede editar 'nombre' o 'puesto'.")
        return

    print("✅ Empleado actualizado correctamente.")

# Funcion para ver los productos
def ver_productos():
    productos = consulta_sql("SELECT nombre, cantidad, precio FROM productos")
    print(f"Productos: {productos}")
    for producto in productos:
        print(dict(producto))

# Funcion para cambiar un producto
def cambiar_producto():
    while True:
        producto_id = input("Ingresa el id del producto: ")
        producto_selec = consulta_sql("SELECT * FROM productos WHERE id = ?", [producto_id])
        print(f"El producto {producto_selec} fue seleccionado")
        cambio_pro = input("Que desea cambiar? Nombre/Precio/Stock/Cancelar: ").lower()
        if cambio_pro == "nombre":
            nuevo_nombre = input("Ingresa el Nuevo nombre del producto: ")
            cambio_sql("UPDATE productos SET nombre = ? WHERE id = ?", (nuevo_nombre, producto_id))
        elif cambio_pro == "precio":
            nuevo_precio = input("Ingresa el Nuevo precio: ")
            cambio_sql("UPDATE productos SET precio = ? WHERE id = ?", (nuevo_precio, producto_id))
        elif cambio_pro == "stock":
            nuevo_stock = input("Ingresa el nuevo stock del producto: ")
            cambio_sql("UPDATE productos SET cantidad = ? WHERE id = ?", (nuevo_stock, producto_id))
        elif cambio_pro == "cancelar":
                print("Cancelando cambios, saliendo...")
                break


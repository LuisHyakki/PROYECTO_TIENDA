import funcionalidades.funcionalidades_pro as f

# menu
while True:
    print("Que deseas hacer?")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver empleados")
    print("4. Ver ventas")
    print("5. agregar ventas")
    print("6. agregar empleados")
    print("7. Ver productos restantes")
    print("8. Eliminar Empleados")
    print("9. Cambiar Empleado")
    print("10. Cambiar Producto")
    print("11. Saliendo")
    opcion = input("elegi una opcion: ")

    if opcion == "1":
        f.agregar_prod()
    elif opcion == "2":
        f.eliminar_prod()
    elif opcion == "3":
        f.ver_empleados()
    elif opcion == "4":
        f.ver_ventas()
    elif opcion == "5":
        f.agregar_venta()
    elif opcion == "6":
        f.empleado()
    elif opcion == "7":
        f.ver_productos()
    elif opcion == "8":
        f.eliminar_empleado()
    elif opcion == "9":
        f.editar_empleado()
    elif opcion == "10":
        f.cambiar_producto()
    elif opcion == "11":
        print("Saliendo...")
        break
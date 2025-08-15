import tkinter as tk
from datetime import datetime
from utils.utils import *
from funcionalidades.funcionalidades_pro import *
import funcionalidades.funcionalidades_pro as f
from tkinter import messagebox
from tkinter import ttk





class app_tienda:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("Gestión de Negocios")
        self.root.geometry("800x600")
        self.root.configure(bg='#006D77')  # Gris no tan oscuro
        self.root.iconbitmap(ruta_icono)


        # Permitir redimensionar
        self.root.resizable(True, True)

        # Crear y mostrar la fecha
        self.crear_fecha()

        #grafico
        self.crear_area_grafico()

        #botones
        self.crear_botones()

        # Actualizar la fecha cada segundo
        self.actualizar_fecha()

    def crear_fecha(self):
        self.root.grid_columnconfigure(1, weight=1)

        self.tienda_label = tk.Label(
            self.root,
            text="Mi Tienda",  # Cambia esto por el nombre que quieras
            bg='#006D77',
            fg='white',
            font=('Arial', 14, 'bold')
        )
        self.tienda_label.grid(row=0, column=0, sticky='nw', padx=20, pady=20)

        """Crear el label de la fecha en la parte superior"""
        self.fecha_label = tk.Label(
            self.root,
            text="",  # Empezamos vacío, se llenará con actualizar_fecha()
            bg='#006D77',  # Mismo color que la ventana
            fg='white',  # Texto blanco
            font=('Arial', 14, 'bold')
        )
        self.fecha_label.grid(row=0, column=1, sticky='ne', padx=20, pady=20)

    def actualizar_fecha(self):
        """Actualizar la fecha y hora actual"""
        fecha_actual = datetime.now().strftime("%A, %d de %B de %Y - %H:%M:%S")
        self.fecha_label.config(text=fecha_actual)

        # Programar la próxima actualización en 1000ms (1 segundo)
        self.root.after(1000, self.actualizar_fecha)

    def crear_area_grafico(self):
        """Crear el área reservada para el gráfico"""
        self.root.grid_rowconfigure(1, weight=1)

        # Frame para el gráfico
        self.grafico_frame = tk.Frame(
            self.root,
            bg='#015159',  # Gris un poco más oscuro para diferenciarlo
            relief='sunken',  # Borde hundido
            bd=2  # Grosor del borde
        )

        # Posicionar el frame ocupando ambas columnas y expandiéndose
        self.grafico_frame.grid(row=1, column=1, sticky='nsew', padx=20, pady=(0, 20))

    def crear_botones(self):
        """Crear panel de botones de funcionalidades"""
        # Frame para contener todos los botones
        self.botones_frame = tk.Frame(
            self.root,
            bg='#006D77'  # Mismo color que la ventana principal
        )

        # Posicionar el frame de botones en la columna derecha
        self.botones_frame.grid(row=1, column=0, sticky='nsew',
                                padx=(10, 20), pady=(0, 20))

        # Lista de botones con sus textos y comandos
        botones_info = [
            ("Agregar Producto", self.agregar_producto),
            ("Eliminar Producto", self.eliminar_producto),
            ("Agregar Empleado", self.agregar_empleado),
            ("Eliminar Empleado", self.eliminar_empleado),
            ("Agregar Venta", self.agregar_venta),
            ("Ver Ventas", self.ver_ventas),
            ("Ver Productos", self.ver_productos),
            ("Cambiar Productos", self.cambiar_productos)
        ]


        # Crear los botones
        for i, (texto, comando) in enumerate(botones_info):
            btn = tk.Button(
                self.botones_frame,
                text=texto,
                command=comando,
                bg='#83C5BE',  # Color azul claro
                fg='#006D77',  # Texto color principal
                font=('Arial', 11, 'bold'),
                relief='raised',
                bd=2,
                pady=8,
                cursor='hand2',
                activebackground='#FFDDD2',  # Color al hacer hover
                activeforeground='#006D77'
            )
            btn.grid(row=i, column=0, sticky='ew', padx=10, pady=5)

#productos
    def agregar_producto(self):
        """Mostrar formulario para agregar producto en el área del gráfico"""
        # Limpiar el área del gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Título del formulario
        titulo = tk.Label(
            self.grafico_frame,
            text="AGREGAR NUEVO PRODUCTO",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Frame contenedor para el formulario
        form_frame = tk.Frame(
            self.grafico_frame,
            bg='#015159'
        )
        form_frame.pack(expand=True)

        # Campo: Nombre del producto
        tk.Label(
            form_frame,
            text="Nombre del Producto:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=0, column=0, sticky='w', padx=20, pady=10)

        self.entry_nombre = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=30
        )
        self.entry_nombre.grid(row=0, column=1, padx=20, pady=10)

        # Campo: Cantidad
        tk.Label(
            form_frame,
            text="Cantidad:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=1, column=0, sticky='w', padx=20, pady=10)

        self.entry_cantidad = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=30
        )
        self.entry_cantidad.grid(row=1, column=1, padx=20, pady=10)

        # Campo: Precio
        tk.Label(
            form_frame,
            text="Precio:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=2, column=0, sticky='w', padx=20, pady=10)

        self.entry_precio = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=30
        )
        self.entry_precio.grid(row=2, column=1, padx=20, pady=10)

        # Frame para los botones
        botones_frame = tk.Frame(
            form_frame,
            bg='#015159'
        )
        botones_frame.grid(row=3, column=0, columnspan=2, pady=30)

        # Botón Guardar
        btn_guardar = tk.Button(
            botones_frame,
            text="GUARDAR PRODUCTO",
            command=self.guardar_producto,
            bg='#83C5BE',
            fg='#006D77',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_guardar.pack(side='left', padx=10)

        # Botón Cancelar
        btn_cancelar = tk.Button(
            botones_frame,
            text="CANCELAR",
            command=self.limpiar_area_grafico,
            bg='#FFDDD2',
            fg='#006D77',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_cancelar.pack(side='left', padx=10)
    def guardar_producto(self):
        """Mostrar formulario para agregar producto en el área del gráfico"""
        # Limpiar el área del gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Obtener los valores de los campos
        nombre = self.entry_nombre.get().strip()
        cantidad = self.entry_cantidad.get().strip()
        precio = self.entry_precio.get().strip()

        # Validar que los campos no estén vacíos
        if not nombre or not cantidad or not precio:
            messagebox.showerror("Error", "Por favor, completa todos los campos")
            return

        # Validar que cantidad y precio sean números
        try:
            cantidad = int(cantidad)
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número entero y precio un número decimal")
            return

        try:
            # Usar tu función existente para insertar en la BD
            from utils.utils import cambio_sql  # Importar tu función

            # Usar tu función cambio_sql
            cambio_sql("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",(nombre, cantidad, precio))

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente")

            # Limpiar el formulario
            self.limpiar_area_grafico()

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el producto: {str(e)}")
    def eliminar_producto(self):
        # Limpiar el frame antes de agregar nuevos elementos
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.grafico_frame,
            text="ELIMINAR PRODUCTO",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Crear el estilo ANTES del TreeView
        style = ttk.Style()

        # Configurar el estilo personalizado para el TreeView
        style.configure("Custom.Treeview",
                        background="#76a9ad",  # Fondo blanco para las filas
                        foreground="#015159",  # Texto en color del tema
                        rowheight=30,  # Altura de las filas
                        fieldbackground="#76a9ad",  # Fondo del campo
                        borderwidth=1,
                        relief="solid")

        # Personalizar las cabeceras
        style.configure("Custom.Treeview.Heading",
                        background="#224447",  # Fondo de las cabeceras
                        foreground="black",
                        font=('Arial', 11, 'bold'),  # Fuente en negrita
                        borderwidth=1,
                        relief="solid")

        # Configurar colores cuando se selecciona una fila
        style.map("Custom.Treeview",
                  background=[('selected', '#0b8c99')],  # Verde al seleccionar
                  foreground=[('selected', 'black')])  # Texto blanco al seleccionar

        # Crear un frame contenedor SOLO para el TreeView y scrollbar
        frame_tree = tk.Frame(self.grafico_frame, bg='#015159')
        frame_tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Crear el TreeView CON el estilo personalizado
        tree = ttk.Treeview(frame_tree, style="Custom.Treeview", height=12)

        # Definir las columnas de tu tabla empleados
        columnas = ("Id", "Nombre", "Precio")
        tree["columns"] = columnas
        tree["show"] = "headings"  # Solo mostrar las cabeceras, no el árbol

        # Configurar cada columna con anchos apropiados
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.heading("Id", text="Id")


        # Ajustar el ancho de las columnas para que se vea mejor
        tree.column("Nombre", width=150, anchor="w", minwidth=100)
        tree.column("Precio", width=200, anchor="w", minwidth=150)
        tree.column("Id", width=200, anchor="w", minwidth=150)

        # Agregar scrollbar vertical
        scrollbar_v = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_v.set)

        # Posicionar el TreeView y scrollbar
        tree.pack(side="left", fill="both", expand=True)
        scrollbar_v.pack(side="right", fill="y")

        for producto_row in consulta_sql("SELECT id, nombre, precio FROM productos"):
            tree.insert("", "end", values=tuple(producto_row))

        def eliminar_producto_seleccionado(event):
            # Obtener lo que está seleccionado
            seleccionado = tree.selection()

            if seleccionado:
                # Obtener los datos del empleado
                item = tree.item(seleccionado[0])
                producto_dato = item['values']
                producto_nombre = producto_dato[1]
                producto_id = producto_dato[0]

                # Ventana de confirmación
                from tkinter import messagebox
                respuesta = messagebox.askyesno(
                    "Confirmar eliminación",
                    f"¿Está seguro de eliminar a {producto_nombre}?"
                )

                if respuesta:  # Si dice "Sí"
                    try:
                        # Consulta SQL para eliminar
                        cambio_sql(f"DELETE FROM productos WHERE id = {producto_id}")

                        # Eliminar de la tabla visual
                        tree.delete(seleccionado[0])

                        messagebox.showinfo("Éxito", "producto eliminado")
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo eliminar: {e}")

        # Vincular doble clic al TreeView
        tree.bind("<Double-1>", eliminar_producto_seleccionado)


##empleados
    def agregar_empleado(self):
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Título del formulario
        titulo = tk.Label(
            self.grafico_frame,
            text="AGREGAR NUEVO EMPLEADO",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Frame contenedor para el formulario
        form_frame = tk.Frame(
            self.grafico_frame,
            bg='#015159'
        )
        form_frame.pack(expand=True)

        # Campo: Nombre del producto
        tk.Label(
            form_frame,
            text="NOMBRE DEL EMPLEADO:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=0, column=0, sticky='w', padx=20, pady=10)

        self.entry_nombre_empleado = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=30
        )
        self.entry_nombre_empleado.grid(row=0, column=1, padx=20, pady=10)

        # Campo: puesto
        tk.Label(
            form_frame,
            text="PUESTO:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=2, column=0, sticky='w', padx=20, pady=10)

        self.entry_puesto = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=30
        )
        self.entry_puesto.grid(row=2, column=1, padx=20, pady=10)

        # Frame para los botones
        botones_frame = tk.Frame(
            form_frame,
            bg='#015159'
        )
        botones_frame.grid(row=3, column=0, columnspan=2, pady=30)

        # Botón Guardar
        btn_guardar = tk.Button(
            botones_frame,
            text="GUARDAR EMPLEADO",
            command=self.guardar_empleado,
            bg='#83C5BE',
            fg='#006D77',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_guardar.pack(side='left', padx=10)

        # Botón Cancelar
        btn_cancelar = tk.Button(
            botones_frame,
            text="CANCELAR",
            command=self.limpiar_area_grafico,
            bg='#FFDDD2',
            fg='#006D77',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_cancelar.pack(side='left', padx=10)
    def guardar_empleado(self):
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Obtener los valores de los campos
        nombre = self.entry_nombre_empleado.get().strip()
        puesto = self.entry_puesto.get().strip()

        # Validar que los campos no estén vacíos
        if not nombre or not puesto:
            messagebox.showerror("Error", "Por favor, completa todos los campos")
            return

        try:
            # Usar tu función existente para insertar en la BD
            from utils.utils import cambio_sql  # Importar tu función

            # Usar tu función cambio_sql
            cambio_sql("INSERT INTO empleados (nombre, puesto) VALUES (?, ?)",
                       (nombre, puesto))

            # Mostrar mensaje de éxito
            messagebox.showinfo(title="Enhorabuena", message="Empleado registrado correctamente.")

            # Limpiar el formulario
            self.limpiar_area_grafico()

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el empleado: {str(e)}")
    def eliminar_empleado(self):
        # Limpiar el frame antes de agregar nuevos elementos
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.grafico_frame,
            text="ELIMINAR EMPLEADOS",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Crear el estilo ANTES del TreeView
        style = ttk.Style()

        # Configurar el estilo personalizado para el TreeView
        style.configure("Custom.Treeview",
                        background="#76a9ad",  # Fondo blanco para las filas
                        foreground="#015159",  # Texto en color del tema
                        rowheight=30,  # Altura de las filas
                        fieldbackground="#76a9ad",  # Fondo del campo
                        borderwidth=1,
                        relief="solid")

        # Personalizar las cabeceras
        style.configure("Custom.Treeview.Heading",
                        background="#224447",  # Fondo de las cabeceras
                        foreground="black",
                        font=('Arial', 11, 'bold'),  # Fuente en negrita
                        borderwidth=1,
                        relief="solid")

        # Configurar colores cuando se selecciona una fila
        style.map("Custom.Treeview",
                  background=[('selected', '#0b8c99')],  # Verde al seleccionar
                  foreground=[('selected', 'black')])  # Texto blanco al seleccionar

        # Crear un frame contenedor SOLO para el TreeView y scrollbar
        frame_tree = tk.Frame(self.grafico_frame, bg='#015159')
        frame_tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Crear el TreeView CON el estilo personalizado
        tree = ttk.Treeview(frame_tree, style="Custom.Treeview", height=12)

        # Definir las columnas de tu tabla empleados
        columnas = ("ID", "Nombre", "Cargo")
        tree["columns"] = columnas
        tree["show"] = "headings"  # Solo mostrar las cabeceras, no el árbol

        # Configurar cada columna con anchos apropiados
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Cargo", text="Cargo")

        # Ajustar el ancho de las columnas para que se vea mejor
        tree.column("ID", width=60, anchor="center", minwidth=50)
        tree.column("Nombre", width=150, anchor="w", minwidth=100)
        tree.column("Cargo", width=200, anchor="w", minwidth=150)

        # Agregar scrollbar vertical
        scrollbar_v = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_v.set)

        # Posicionar el TreeView y scrollbar
        tree.pack(side="left", fill="both", expand=True)
        scrollbar_v.pack(side="right", fill="y")

        for empleado_row in consulta_sql("SELECT id, nombre, puesto FROM empleados"):
            tree.insert("", "end", values=tuple(empleado_row))

        def eliminar_empleado_seleccionado(event):
            # Obtener lo que está seleccionado
            seleccionado = tree.selection()

            if seleccionado:
                # Obtener los datos del empleado
                item = tree.item(seleccionado[0])
                empleado_datos = item['values']
                id_empleado = empleado_datos[0]
                nombre_empleado = empleado_datos[1]

                # Ventana de confirmación
                from tkinter import messagebox
                respuesta = messagebox.askyesno(
                    "Confirmar eliminación",
                    f"¿Está seguro de eliminar a {nombre_empleado}?"
                )

                if respuesta:  # Si dice "Sí"
                    try:
                        # Consulta SQL para eliminar
                        cambio_sql(f"DELETE FROM empleados WHERE id = {id_empleado}")

                        # Eliminar de la tabla visual
                        tree.delete(seleccionado[0])

                        messagebox.showinfo("Éxito", "Empleado eliminado")
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo eliminar: {e}")

        # Vincular doble clic al TreeView
        tree.bind("<Double-1>", eliminar_empleado_seleccionado)

        # Guardar referencia del tree para uso posterior
        self.tree_empleados = tree

        return tree

    def agregar_venta(self):
        # Limpiar el frame gráfico
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Título del formulario
        titulo = tk.Label(
            self.grafico_frame,
            text="AGREGAR NUEVA VENTA",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Frame contenedor para el formulario
        form_frame = tk.Frame(
            self.grafico_frame,
            bg='#015159'
        )
        form_frame.pack(expand=True)

        # Campo: ID del producto
        tk.Label(
            form_frame,
            text="ID DEL PRODUCTO:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=0, column=0, sticky='w', padx=20, pady=10)

        self.entry_id_producto = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=15
        )
        self.entry_id_producto.grid(row=0, column=1, padx=20, pady=10, sticky='w')

        # Botón buscar producto
        btn_buscar = tk.Button(
            form_frame,
            text="BUSCAR",
            command=self.buscar_producto,
            bg='#83C5BE',
            fg='#006D77',
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5,
            cursor='hand2'
        )
        btn_buscar.grid(row=0, column=2, padx=10, pady=10)

        # Campo: Nombre del producto (solo lectura)
        tk.Label(
            form_frame,
            text="NOMBRE DEL PRODUCTO:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=1, column=0, sticky='w', padx=20, pady=10)

        self.entry_nombre_producto = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=30,
            state='readonly'
        )
        self.entry_nombre_producto.grid(row=1, column=1, columnspan=2, padx=20, pady=10)

        # Campo: Precio unitario (solo lectura)
        tk.Label(
            form_frame,
            text="PRECIO UNITARIO:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=2, column=0, sticky='w', padx=20, pady=10)

        self.entry_precio_unitario = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=15,
            state='readonly'
        )
        self.entry_precio_unitario.grid(row=2, column=1, padx=20, pady=10, sticky='w')

        # Campo: Cantidad
        tk.Label(
            form_frame,
            text="CANTIDAD:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=3, column=0, sticky='w', padx=20, pady=10)

        self.entry_cantidad = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=15
        )
        self.entry_cantidad.grid(row=3, column=1, padx=20, pady=10, sticky='w')

        # Bind para calcular automáticamente cuando cambie la cantidad
        self.entry_cantidad.bind('<KeyRelease>', self.calcular_subtotal)

        # Campo: Descuento (%)
        tk.Label(
            form_frame,
            text="DESCUENTO (%):",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=4, column=0, sticky='w', padx=20, pady=10)

        self.entry_descuento = tk.Entry(
            form_frame,
            font=('Arial', 12),
            width=15
        )
        self.entry_descuento.grid(row=4, column=1, padx=20, pady=10, sticky='w')
        self.entry_descuento.insert(0, "0")  # Valor por defecto

        # Bind para calcular automáticamente cuando cambie el descuento
        self.entry_descuento.bind('<KeyRelease>', self.calcular_subtotal)

        # Campo: Total (solo lectura)
        tk.Label(
            form_frame,
            text="TOTAL:",
            font=('Arial', 12, 'bold'),
            bg='#015159',
            fg='white'
        ).grid(row=5, column=0, sticky='w', padx=20, pady=10)

        self.entry_total = tk.Entry(
            form_frame,
            font=('Arial', 12, 'bold'),
            width=15,
            state='readonly',
            bg='#83C5BE'
        )
        self.entry_total.grid(row=5, column=1, padx=20, pady=10, sticky='w')

        # Frame para los botones
        botones_frame = tk.Frame(
            form_frame,
            bg='#015159'
        )
        botones_frame.grid(row=6, column=0, columnspan=3, pady=30)

        # Botón Guardar
        btn_guardar = tk.Button(
            botones_frame,
            text="GUARDAR VENTA",
            command=self.guardar_venta,
            bg='#83C5BE',
            fg='#006D77',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_guardar.pack(side='left', padx=10)

        # Botón Cancelar
        btn_cancelar = tk.Button(
            botones_frame,
            text="CANCELAR",
            command=self.limpiar_area_grafico,
            bg='#FFDDD2',
            fg='#006D77',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_cancelar.pack(side='left', padx=10)

    def buscar_producto(self):
        id_producto = self.entry_id_producto.get().strip()

        if not id_producto:
            messagebox.showerror("Error", "Por favor, ingresa el ID del producto")
            return

        try:
            from utils.utils import consulta_sql  # Importar tu función de consulta

            # Buscar el producto en la base de datos
            resultado = consulta_sql("SELECT nombre, precio FROM productos WHERE id = ?", (id_producto,))

            if resultado:
                nombre, precio = resultado[0]

                # Habilitar temporalmente los campos para editarlos
                self.entry_nombre_producto.config(state='normal')
                self.entry_precio_unitario.config(state='normal')

                # Limpiar y llenar los campos
                self.entry_nombre_producto.delete(0, tk.END)
                self.entry_nombre_producto.insert(0, nombre)

                self.entry_precio_unitario.delete(0, tk.END)
                self.entry_precio_unitario.insert(0, f"{precio:.2f}")

                # Volver a solo lectura
                self.entry_nombre_producto.config(state='readonly')
                self.entry_precio_unitario.config(state='readonly')

                # Limpiar campos dependientes
                self.entry_cantidad.delete(0, tk.END)
                self.entry_cantidad.insert(0, "1")
                self.entry_descuento.delete(0, tk.END)
                self.entry_descuento.insert(0, "0")

                # Calcular total inicial
                self.calcular_subtotal()

                messagebox.showinfo("Éxito", f"Producto encontrado: {nombre}")

            else:
                messagebox.showerror("Error", "Producto no encontrado")
                # Limpiar campos si no se encuentra el producto
                self.entry_nombre_producto.config(state='normal')
                self.entry_precio_unitario.config(state='normal')
                self.entry_nombre_producto.delete(0, tk.END)
                self.entry_precio_unitario.delete(0, tk.END)
                self.entry_nombre_producto.config(state='readonly')
                self.entry_precio_unitario.config(state='readonly')

        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar el producto: {str(e)}")

    def calcular_subtotal(self, event=None):
        """Calcula el total basado en precio, cantidad y descuento"""
        try:
            precio_str = self.entry_precio_unitario.get().strip()
            cantidad_str = self.entry_cantidad.get().strip()
            descuento_str = self.entry_descuento.get().strip()

            if not precio_str or not cantidad_str:
                return

            precio = float(precio_str)
            cantidad = int(cantidad_str) if cantidad_str else 0
            descuento = float(descuento_str) if descuento_str else 0

            # Calcular subtotal
            subtotal = precio * cantidad

            # Aplicar descuento
            descuento_amount = subtotal * (descuento / 100)
            total = subtotal - descuento_amount

            # Actualizar campo total
            self.entry_total.config(state='normal')
            self.entry_total.delete(0, tk.END)
            self.entry_total.insert(0, f"{total:.2f}")
            self.entry_total.config(state='readonly')

        except ValueError:
            # Si hay error en la conversión, limpiar el total
            self.entry_total.config(state='normal')
            self.entry_total.delete(0, tk.END)
            self.entry_total.insert(0, "0.00")
            self.entry_total.config(state='readonly')

    def guardar_venta(self):
        """Guarda la venta en la base de datos"""
        # Limpiar frame después de guardar
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        # Obtener valores
        id_producto = self.entry_id_producto.get().strip()
        cantidad_str = self.entry_cantidad.get().strip()
        descuento_str = self.entry_descuento.get().strip()
        total_str = self.entry_total.get().strip()

        # Validaciones
        if not id_producto or not cantidad_str or not total_str:
            messagebox.showerror("Error", "Por favor, completa todos los campos necesarios")
            return

        try:
            cantidad = int(cantidad_str)
            descuento = float(descuento_str) if descuento_str else 0
            total = float(total_str)

            if cantidad <= 0:
                messagebox.showerror("Error", "La cantidad debe ser mayor a 0")
                return

            if descuento < 0 or descuento > 100:
                messagebox.showerror("Error", "El descuento debe estar entre 0 y 100%")
                return

            from utils.utils import cambio_sql
            from datetime import datetime

            # Insertar la venta (ajusta los campos según tu tabla de ventas)
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cambio_sql("""INSERT INTO ventas (id_producto, cantidad, descuento, total, fecha) 
                          VALUES (?, ?, ?, ?, ?)""",
                       (id_producto, cantidad, descuento, total, fecha_actual))

            messagebox.showinfo("Éxito", "Venta registrada correctamente")
            self.limpiar_area_grafico()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar la venta: {str(e)}")

    def ver_ventas(self):
        # Limpiar el frame antes de agregar nuevos elementos
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.grafico_frame,
            text="VENTAS",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Crear el estilo ANTES del TreeView
        style = ttk.Style()

        # Configurar el estilo personalizado para el TreeView
        style.configure("Custom.Treeview",
                        background="#76a9ad",  # Fondo blanco para las filas
                        foreground="#015159",  # Texto en color del tema
                        rowheight=30,  # Altura de las filas
                        fieldbackground="#76a9ad",  # Fondo del campo
                        borderwidth=1,
                        relief="solid")

        # Personalizar las cabeceras
        style.configure("Custom.Treeview.Heading",
                        background="#224447",  # Fondo de las cabeceras
                        foreground="black",
                        font=('Arial', 11, 'bold'),  # Fuente en negrita
                        borderwidth=1,
                        relief="solid")

        # Configurar colores cuando se selecciona una fila
        style.map("Custom.Treeview",
                  background=[('selected', '#0b8c99')],  # Verde al seleccionar
                  foreground=[('selected', 'black')])  # Texto blanco al seleccionar

        # Crear un frame contenedor SOLO para el TreeView y scrollbar
        frame_tree = tk.Frame(self.grafico_frame, bg='#015159')
        frame_tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Crear el TreeView CON el estilo personalizado
        tree = ttk.Treeview(frame_tree, style="Custom.Treeview", height=12)

        # Definir las columnas de tu tabla empleados
        columnas = ("Id", "Nombre", "Precio")
        tree["columns"] = columnas
        tree["show"] = "headings"  # Solo mostrar las cabeceras, no el árbol

        # Configurar cada columna con anchos apropiados
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.heading("Id", text="Id")

        # Ajustar el ancho de las columnas para que se vea mejor
        tree.column("Nombre", width=150, anchor="w", minwidth=100)
        tree.column("Precio", width=200, anchor="w", minwidth=150)
        tree.column("Id", width=200, anchor="w", minwidth=150)

        # Agregar scrollbar vertical
        scrollbar_v = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_v.set)

        # Posicionar el TreeView y scrollbar
        tree.pack(side="left", fill="both", expand=True)
        scrollbar_v.pack(side="right", fill="y")

        for producto_row in consulta_sql("SELECT id, nombre, precio FROM productos"):
            tree.insert("", "end", values=tuple(producto_row))

    def ver_productos(self):
        # Limpiar el frame antes de agregar nuevos elementos
        for widget in self.grafico_frame.winfo_children():
            widget.destroy()

        titulo = tk.Label(
            self.grafico_frame,
            text="ELIMINAR PRODUCTO",
            font=('Arial', 16, 'bold'),
            bg='#015159',
            fg='white'
        )
        titulo.pack(pady=20)

        # Crear el estilo ANTES del TreeView
        style = ttk.Style()

        # Configurar el estilo personalizado para el TreeView
        style.configure("Custom.Treeview",
                        background="#76a9ad",  # Fondo blanco para las filas
                        foreground="#015159",  # Texto en color del tema
                        rowheight=30,  # Altura de las filas
                        fieldbackground="#76a9ad",  # Fondo del campo
                        borderwidth=1,
                        relief="solid")

        # Personalizar las cabeceras
        style.configure("Custom.Treeview.Heading",
                        background="#224447",  # Fondo de las cabeceras
                        foreground="black",
                        font=('Arial', 11, 'bold'),  # Fuente en negrita
                        borderwidth=1,
                        relief="solid")

        # Configurar colores cuando se selecciona una fila
        style.map("Custom.Treeview",
                  background=[('selected', '#0b8c99')],  # Verde al seleccionar
                  foreground=[('selected', 'black')])  # Texto blanco al seleccionar

        # Crear un frame contenedor SOLO para el TreeView y scrollbar
        frame_tree = tk.Frame(self.grafico_frame, bg='#015159')
        frame_tree.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        # Crear el TreeView CON el estilo personalizado
        tree = ttk.Treeview(frame_tree, style="Custom.Treeview", height=12)

        # Definir las columnas de tu tabla empleados
        columnas = ("Id", "Nombre", "Precio")
        tree["columns"] = columnas
        tree["show"] = "headings"  # Solo mostrar las cabeceras, no el árbol

        # Configurar cada columna con anchos apropiados
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.heading("Id", text="Id")


        # Ajustar el ancho de las columnas para que se vea mejor
        tree.column("Nombre", width=150, anchor="w", minwidth=100)
        tree.column("Precio", width=200, anchor="w", minwidth=150)
        tree.column("Id", width=200, anchor="w", minwidth=150)

        # Agregar scrollbar vertical
        scrollbar_v = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_v.set)

        # Posicionar el TreeView y scrollbar
        tree.pack(side="left", fill="both", expand=True)
        scrollbar_v.pack(side="right", fill="y")

        for producto_row in consulta_sql("SELECT id, nombre, precio FROM productos"):
            tree.insert("", "end", values=tuple(producto_row))

    def cambiar_productos(self):
        f.cambiar_producto()  # Conecta aquí tu función de cambiar productos

# Crear y ejecutar la aplicación
    def ejecutar(self):
        """Iniciar la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    app = app_tienda()
    app.ejecutar()
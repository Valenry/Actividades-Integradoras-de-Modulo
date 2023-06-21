import mysql.connector


class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='big_bread_production',
            port='3306'
        )

    def conectar(self):
        try:
            self.conexion.connect()
            print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)

    def cerrar_conexion(self):
        self.conexion.close()
        print("Conexión cerrada")


class ControladorProductos:
    def __init__(self):
        self.conexion = Conexion()

    def listar_productos(self):
        self.conexion.conectar()

        query = "SELECT * FROM productos"

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query)
            productos = cursor.fetchall()
            if productos:
                print("Listado de Productos:")
                print("| ID | Código de Barras | Nombre | Descripción | Stock | Precio | Unidad de Medida | Fecha de Creación | Peso Unitario |")
                for producto in productos:
                    print("|", producto[0], "|", producto[1], "|", producto[2], "|", producto[3], "|", producto[4], "|", producto[5], "|", producto[6], "|", producto[7], "|", producto[8], "|")
            else:
                print("No hay productos registrados.")
        except mysql.connector.Error as error:
            print("Error al listar los productos:", error)

        self.conexion.cerrar_conexion()

    def insertar_producto(self):
        self.conexion.conectar()

        codigo_barras = input("Ingrese el código de barras del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        stock = int(input("Ingrese el stock del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        unidad_medida = input("Ingrese la unidad de medida del producto: ")
        fecha_creacion = input("Ingrese la fecha de creación del producto (YYYY-MM-DD): ")
        peso_unitario = float(input("Ingrese el peso unitario del producto: "))

        query = "INSERT INTO productos (codigo_barras, nombre, descripcion, stock, precio, unidad_medida, fecha_creacion, peso_unitario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (codigo_barras, nombre, descripcion, stock, precio, unidad_medida, fecha_creacion, peso_unitario)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Producto insertado correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar el producto:", error)

        self.conexion.cerrar_conexion()

    def actualizar_producto(self):
        self.conexion.conectar()

        producto_id = input("Ingrese el ID del producto a actualizar: ")

        codigo_barras = input("Ingrese el nuevo código de barras del producto: ")
        nombre = input("Ingrese el nuevo nombre del producto: ")
        descripcion = input("Ingrese la nueva descripción del producto: ")
        stock = int(input("Ingrese el nuevo stock del producto: "))
        precio = float(input("Ingrese el nuevo precio del producto: "))
        unidad_medida = input("Ingrese la nueva unidad de medida del producto: ")
        fecha_creacion = input("Ingrese la nueva fecha de creación del producto (YYYY-MM-DD): ")
        peso_unitario = float(input("Ingrese el nuevo peso unitario del producto: "))

        query = "UPDATE productos SET codigo_barras = %s, nombre = %s, descripcion = %s, stock = %s, precio = %s, unidad_medida = %s, fecha_creacion = %s, peso_unitario = %s WHERE id_producto = %s"
        values = (codigo_barras, nombre, descripcion, stock, precio, unidad_medida, fecha_creacion, peso_unitario, producto_id)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Producto actualizado correctamente.")
        except mysql.connector.Error as error:
            print("Error al actualizar el producto:", error)

        self.conexion.cerrar_conexion()

    def eliminar_producto(self):
        self.conexion.conectar()

        producto_id = input("Ingrese el ID del producto a eliminar: ")

        query = "DELETE FROM productos WHERE id_producto = %s"
        values = (producto_id,)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Producto eliminado correctamente.")
        except mysql.connector.Error as error:
            print("Error al eliminar el producto:", error)

        self.conexion.cerrar_conexion()

    def menu(self):
        while True:
            print("\n----- Menú de Productos -----")
            print("1. Listar productos")
            print("2. Insertar producto")
            print("3. Actualizar producto")
            print("4. Eliminar producto")
            print("5. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                self.listar_productos()
            elif opcion == '2':
                self.insertar_producto()
            elif opcion == '3':
                self.actualizar_producto()
            elif opcion == '4':
                self.eliminar_producto()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")


controlador = ControladorProductos()
controlador.menu()

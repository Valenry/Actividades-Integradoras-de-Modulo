import mysql.connector


class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='liam2011',
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


class ControladorInsumos:
    def __init__(self):
        self.conexion = Conexion()

    def listar_insumos(self):
        self.conexion.conectar()

        query = "SELECT * FROM insumos"

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query)
            insumos = cursor.fetchall()
            if insumos:
                print("Listado de Insumos:")
                print("| ID | Nombre | Descripción | Precio | Cantidad | Proveedor |")
                for insumo in insumos:
                    print("|", insumo[0], "|", insumo[1], "|", insumo[2], "|", insumo[3], "|", insumo[4], "|", insumo[5], "|")
            else:
                print("No hay insumos registrados.")
        except mysql.connector.Error as error:
            print("Error al listar los insumos:", error)

        self.conexion.cerrar_conexion()

    def insertar_insumo(self):
        self.conexion.conectar()

        nombre = input("Ingrese el nombre del insumo: ")
        descripcion = input("Ingrese la descripción del insumo: ")
        precio = float(input("Ingrese el precio del insumo: "))
        cantidad = int(input("Ingrese la cantidad del insumo: "))
        proveedor = input("Ingrese el proveedor del insumo: ")

        query = "INSERT INTO insumos (nombre, descripcion, precio, cantidad, proveedor) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, descripcion, precio, cantidad, proveedor)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Insumo insertado correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar el insumo:", error)

        self.conexion.cerrar_conexion()

    def actualizar_insumo(self):
        self.conexion.conectar()

        insumo_id = input("Ingrese el ID del insumo a actualizar: ")

        nombre = input("Ingrese el nuevo nombre del insumo: ")
        descripcion = input("Ingrese la nueva descripción del insumo: ")
        precio = float(input("Ingrese el nuevo precio del insumo: "))
        cantidad = int(input("Ingrese la nueva cantidad del insumo: "))
        proveedor = input("Ingrese el nuevo proveedor del insumo: ")

        query = "UPDATE insumos SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s, proveedor = %s WHERE id_insumo = %s"
        values = (nombre, descripcion, precio, cantidad, proveedor, insumo_id)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Insumo actualizado correctamente.")
        except mysql.connector.Error as error:
            print("Error al actualizar el insumo:", error)

        self.conexion.cerrar_conexion()

    def eliminar_insumo(self):
        self.conexion.conectar()

        insumo_id = input("Ingrese el ID del insumo a eliminar: ")

        query = "DELETE FROM insumos WHERE id_insumo = %s"
        values = (insumo_id,)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Insumo eliminado correctamente.")
        except mysql.connector.Error as error:
            print("Error al eliminar el insumo:", error)

        self.conexion.cerrar_conexion()

    def menu(self):
        while True:
            print("\n----- Menú de Insumos -----")
            print("1. Listar insumos")
            print("2. Insertar insumo")
            print("3. Actualizar insumo")
            print("4. Eliminar insumo")
            print("5. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                self.listar_insumos()
            elif opcion == '2':
                self.insertar_insumo()
            elif opcion == '3':
                self.actualizar_insumo()
            elif opcion == '4':
                self.eliminar_insumo()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")


controlador = ControladorInsumos()
controlador.menu()

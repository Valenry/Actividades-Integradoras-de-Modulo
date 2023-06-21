import mysql.connector


class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='Godoy1234',
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


class ControladorProduccionDiaria:
    def __init__(self):
        self.conexion = Conexion()

    def listar_produccion_diaria(self):
        self.conexion.conectar()

        fecha_inicio = input("Ingrese la fecha de inicio del intervalo (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin del intervalo (YYYY-MM-DD): ")

        query = "SELECT * FROM produccion_diaria WHERE fecha BETWEEN %s AND %s"
        values = (fecha_inicio, fecha_fin)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            produccion_diaria = cursor.fetchall()
            if produccion_diaria:
                print("Listado de Producción Diaria en el intervalo", fecha_inicio, "-", fecha_fin)
                print("| ID | Fecha | ID Producto | Cantidad Producida | Estado de Producción |")
                for produccion in produccion_diaria:
                    print("|", produccion[0], "|", produccion[1], "|", produccion[2], "|", produccion[3], "|", produccion[4], "|")
            else:
                print("No hay registros de producción diaria en el intervalo", fecha_inicio, "-", fecha_fin)
        except mysql.connector.Error as error:
            print("Error al listar la producción diaria:", error)

        self.conexion.cerrar_conexion()

    def insertar_produccion_diaria(self):
        self.conexion.conectar()

        fecha = input("Ingrese la fecha de producción diaria (YYYY-MM-DD): ")
        id_producto = int(input("Ingrese el ID del producto: "))
        cantidad_producida = int(input("Ingrese la cantidad producida: "))
        estado_produccion = input("Ingrese el estado de producción: ")

        query = "INSERT INTO produccion_diaria (fecha, id_producto, cantidad_producida, estado_produccion) VALUES (%s, %s, %s, %s)"
        values = (fecha, id_producto, cantidad_producida, estado_produccion)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Registro de producción diaria insertado correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar el registro de producción diaria:", error)

        self.conexion.cerrar_conexion()

    def actualizar_produccion_diaria(self):
        self.conexion.conectar()

        produccion_id = input("Ingrese el ID de la producción diaria a actualizar: ")

        fecha = input("Ingrese la nueva fecha de producción diaria (YYYY-MM-DD): ")
        id_producto = int(input("Ingrese el nuevo ID del producto: "))
        cantidad_producida = int(input("Ingrese la nueva cantidad producida: "))
        estado_produccion = input("Ingrese el nuevo estado de producción: ")

        query = "UPDATE produccion_diaria SET fecha = %s, id_producto = %s, cantidad_producida = %s, estado_produccion = %s WHERE id_produccion_diaria = %s"
        values = (fecha, id_producto, cantidad_producida, estado_produccion, produccion_id)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Producción diaria actualizada correctamente.")
        except mysql.connector.Error as error:
            print("Error al actualizar la producción diaria:", error)

        self.conexion.cerrar_conexion()

    def eliminar_produccion_diaria(self):
        self.conexion.conectar()

        produccion_id = input("Ingrese el ID de la producción diaria a eliminar: ")

        query = "DELETE FROM produccion_diaria WHERE id_produccion_diaria = %s"
        values = (produccion_id,)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Producción diaria eliminada correctamente.")
        except mysql.connector.Error as error:
            print("Error al eliminar la producción diaria:", error)

        self.conexion.cerrar_conexion()

    def menu(self):
        while True:
            print("\n----- Menú de Producción Diaria -----")
            print("1. Listar producción diaria")
            print("2. Insertar producción diaria")
            print("3. Actualizar producción diaria")
            print("4. Eliminar producción diaria")
            print("5. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                self.listar_produccion_diaria()
            elif opcion == '2':
                self.insertar_produccion_diaria()
            elif opcion == '3':
                self.actualizar_produccion_diaria()
            elif opcion == '4':
                self.eliminar_produccion_diaria()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")


controlador = ControladorProduccionDiaria()
controlador.menu()

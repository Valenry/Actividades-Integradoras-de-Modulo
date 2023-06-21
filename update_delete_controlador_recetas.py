import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='root',
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

    def actualizar_receta(self, id_receta, id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE recetas SET id_producto = %s, id_insumo = %s, cantidad_requerida = %s, orden_preparacion = %s, nombre_receta = %s WHERE id_receta = %s"

                data = (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta, id_receta)

                cursor.execute(sentenciaSQL, data)

                self.conexion.commit()
                print("Receta actualizada correctamente")
            except mysql.connector.Error as error:
                print("Error al actualizar la receta:", error)

    def eliminar_receta(self, id_receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM recetas WHERE id_receta = %s"

                data = (id_receta,)

                cursor.execute(sentenciaSQL, data)

                self.conexion.commit()
                print("Receta eliminada correctamente")
            except mysql.connector.Error as error:
                print("Error al eliminar la receta:", error)



# Prueba de actualización, eliminación 
conexion = Conexion()
conexion.conectar()

# Actualizar receta
conexion.actualizar_receta(1, 1, 1, 200, 1, "Receta A")

# Eliminar receta
conexion.eliminar_receta(2)

conexion.cerrar_conexion()
#######################################

import mysql.connector


class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='root',
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


class ControladorRecetas:
    def __init__(self):
        self.conexion = Conexion()

    def listar_recetas(self):
        self.conexion.conectar()

        query = "SELECT * FROM recetas"

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query)
            recetas = cursor.fetchall()
            if recetas:
                print("Listado de Recetas:")
                print("| ID | ID Producto | ID Insumo | Cantidad Requerida | Orden de Preparación | Nombre de Receta |")
                for receta in recetas:
                    print("|", receta[0], "|", receta[1], "|", receta[2], "|", receta[3], "|", receta[4], "|", receta[5], "|")
            else:
                print("No hay registros de recetas.")
        except mysql.connector.Error as error:
            print("Error al listar las recetas:", error)

        self.conexion.cerrar_conexion()

    def insertar_receta(self):
        self.conexion.conectar()

        id_producto = int(input("Ingrese el ID del producto: "))
        id_insumo = int(input("Ingrese el ID del insumo: "))
        cantidad_requerida = int(input("Ingrese la cantidad requerida: "))
        orden_preparacion = int(input("Ingrese el orden de preparación: "))
        nombre_receta = input("Ingrese el nombre de la receta: ")

        query = "INSERT INTO recetas (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta) VALUES (%s, %s, %s, %s, %s)"
        values = (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Receta insertada correctamente.")
        except mysql.connector.Error as error:
            print("Error al insertar la receta:", error)

        self.conexion.cerrar_conexion()

    def actualizar_receta(self):
        self.conexion.conectar()

        receta_id = input("Ingrese el ID de la receta a actualizar: ")

        id_producto = int(input("Ingrese el nuevo ID del producto: "))
        id_insumo = int(input("Ingrese el nuevo ID del insumo: "))
        cantidad_requerida = int(input("Ingrese la nueva cantidad requerida: "))
        orden_preparacion = int(input("Ingrese el nuevo orden de preparación: "))
        nombre_receta = input("Ingrese el nuevo nombre de la receta: ")

        query = "UPDATE recetas SET id_producto = %s, id_insumo = %s, cantidad_requerida = %s, orden_preparacion = %s, nombre_receta = %s WHERE id_receta = %s"
        values = (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta, receta_id)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Receta actualizada correctamente.")
        except mysql.connector.Error as error:
            print("Error al actualizar la receta:", error)

        self.conexion.cerrar_conexion()

    def eliminar_receta(self):
        self.conexion.conectar()

        receta_id = input("Ingrese el ID de la receta a eliminar: ")

        query = "DELETE FROM recetas WHERE id_receta = %s"
        values = (receta_id,)

        try:
            cursor = self.conexion.conexion.cursor()
            cursor.execute(query, values)
            self.conexion.conexion.commit()
            print("Receta eliminada correctamente.")
        except mysql.connector.Error as error:
            print("Error al eliminar la receta:", error)

        self.conexion.cerrar_conexion()

    def menu(self):
        while True:
            print("\n----- Menú de Recetas -----")
            print("1. Listar recetas")
            print("2. Insertar receta")
            print("3. Actualizar receta")
            print("4. Eliminar receta")
            print("5. Salir")

            opcion = input("Ingrese una opción: ")

            if opcion == '1':
                self.listar_recetas()
            elif opcion == '2':
                self.insertar_receta()
            elif opcion == '3':
                self.actualizar_receta()
            elif opcion == '4':
                self.eliminar_receta()
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")


controlador = ControladorRecetas()
controlador.menu()




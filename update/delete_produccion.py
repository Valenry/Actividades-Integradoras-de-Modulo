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

    def actualizar_produccion_diaria(self, id_produccion_diaria, fecha, id_producto, cantidad_producida, estado_produccion):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE produccion_diaria SET fecha = %s, id_producto = %s, cantidad_producida = %s, estado_produccion = %s WHERE id_produccion_diaria = %s"

                data = (fecha, id_producto, cantidad_producida, estado_produccion, id_produccion_diaria)

                cursor.execute(sentenciaSQL, data)

                self.conexion.commit()
                print("Producción diaria actualizada correctamente")
            except mysql.connector.Error as error:
                print("Error al actualizar la producción diaria:", error)

    def eliminar_produccion_diaria(self, id_produccion_diaria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM produccion_diaria WHERE id_produccion_diaria = %s"

                data = (id_produccion_diaria,)

                cursor.execute(sentenciaSQL, data)

                self.conexion.commit()
                print("Producción diaria eliminada correctamente")
            except mysql.connector.Error as error:
                print("Error al eliminar la producción diaria:", error)


# Prueba de actualización, eliminación
conexion = Conexion()
conexion.conectar()

# Actualizar producción diaria
conexion.actualizar_produccion_diaria(1, "2023-05-18", 1, 100, "Finalizada")

# Eliminar producción diaria
conexion.eliminar_produccion_diaria(2)


conexion.cerrar_conexion()



# ESTA FUNCIONA! NO BORRAR!!!

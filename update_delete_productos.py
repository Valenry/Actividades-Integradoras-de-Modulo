import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='****',
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

    def listar_productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as error:
                print("Error al listar los productos:", error)

    def actualizar_producto(self, id_producto, nombre, descripcion, stock, precio, unidad_medida, fecha_creacion, peso_unitario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE productos SET nombre = %s, descripcion = %s, stock = %s, precio = %s, unidad_medida = %s, fecha_creacion = %s, peso_unitario = %s WHERE id_producto = %s"

                data = (nombre, descripcion, stock, precio, unidad_medida, fecha_creacion, peso_unitario, id_producto)

                cursor.execute(sentenciaSQL, data)

                self.conexion.commit()
                print("Producto actualizado correctamente")
            except mysql.connector.Error as error:
                print("Error al actualizar el producto:", error)

    def eliminar_producto(self, id_producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM productos WHERE id_producto = %s"

                data = (id_producto,)

                cursor.execute(sentenciaSQL, data)

                self.conexion.commit()
                print("Producto eliminado correctamente")
            except mysql.connector.Error as error:
                print("Error al eliminar el producto:", error)

    def listar_productos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM productos"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as error:
                print("Error al listar los productos:", error)

# Prueba de actualización y eliminación 
conexion = Conexion()
conexion.conectar()

# Actualizar 
conexion.actualizar_producto(1, "Nuevo nombre", "Nueva descripción", 50, 19.99, "Unidad", "2023-05-18", 0.5)

# Eliminar 
conexion.eliminar_producto(2)


conexion.cerrar_conexion()

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

    def actualizar_insumo(self, id_insumo, nombre, descripcion, precio, cantidad, proveedor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE insumos SET nombre = %s, descripcion = %s, precio = %s, cantidad = %s, proveedor = %s WHERE id_insumo = %s"
                data = (nombre, descripcion, precio, cantidad, proveedor, id_insumo)
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                print("Insumo actualizado correctamente")
            except mysql.connector.Error as error:
                print("Error al actualizar el insumo:", error)

    def eliminar_insumo(self, id_insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM insumos WHERE id_insumo = %s"
                data = (id_insumo,)
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                print("Insumo eliminado correctamente")
            except mysql.connector.Error as error:
                print("Error al eliminar el insumo:", error)
                
                # Crear una instancia de la conexión
conexion = Conexion()
# Conectar 
conexion.conectar()
# Actualizar un insumo existente
conexion.actualizar_insumo(id_insumo=1, nombre="aaaaa", descripcion="h", precio=9.99, cantidad=50, proveedor="Nuevo proveedor")

# Cerrar 
conexion.cerrar_conexion()

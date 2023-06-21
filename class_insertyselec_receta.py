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


class Receta:
    IDReceta = 0
    IDProducto = 0
    IDInsumo = 0
    CantidadRequerida = 0
    OrdenPreparacion = 0
    NombreReceta = ""

    def __init__(self, id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta):
        self.IDProducto = id_producto
        self.IDInsumo = id_insumo
        self.CantidadRequerida = cantidad_requerida
        self.OrdenPreparacion = orden_preparacion
        self.NombreReceta = nombre_receta

    def insertar_receta(self):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            sql = "INSERT INTO recetas (id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta) VALUES (%s, %s, %s, %s, %s)"
            valores = (
                self.IDProducto,
                self.IDInsumo,
                self.CantidadRequerida,
                self.OrdenPreparacion,
                self.NombreReceta,
            )
            cursor.execute(sql, valores)
            conexion.conexion.commit()
            print("Receta insertada correctamente")
        except mysql.connector.Error as error:
            print("Error al insertar la receta:", error)
        finally:
            conexion.cerrar_conexion()

    def seleccionar_recetas(self):
        try:
            conexion = Conexion()
            conexion.conectar()
            cursor = conexion.conexion.cursor()
            sql = """SELECT id_receta, id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta
                     FROM recetas"""
            cursor.execute(sql)
            recetas = cursor.fetchall()
            for receta in recetas:
                print("ID Receta:", receta[0])
                print("ID Producto:", receta[1])
                print("ID Insumo:", receta[2])
                print("Cantidad Requerida:", receta[3])
                print("Orden Preparación:", receta[4])
                print("Nombre Receta:", receta[5])
                print("------------------------")
        except mysql.connector.Error as error:
            print("Error al seleccionar las recetas:", error)
        finally:
            conexion.cerrar_conexion()


# Ejemplo de inserción de una receta
receta = Receta(id_producto=1, id_insumo=1, cantidad_requerida=800, orden_preparacion=1, nombre_receta="Receta de Torta")
receta.insertar_receta()

# Ejemplo de selección de todas las recetas
receta.seleccionar_recetas()


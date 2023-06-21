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

conexion = Conexion()
conexion.conectar()

class Receta:
    ID_Receta = 0
    ID_Producto = 0
    ID_Insumo = 0
    Cantidad_Requerida = 0
    Orden_Preparacion = 0
    Nombre_Receta = ""

    def __init__(self, id_receta, id_producto, id_insumo, cantidad_requerida, orden_preparacion, nombre_receta):
        self.ID_Receta = id_receta
        self.ID_Producto = id_producto
        self.ID_Insumo = id_insumo
        self.Cantidad_Requerida = cantidad_requerida
        self.Orden_Preparacion = orden_preparacion
        self.Nombre_Receta = nombre_receta

    def getID_Receta(self):
        return self.ID_Receta

    def getID_Producto(self):
        return self.ID_Producto

    def getID_Insumo(self):
        return self.ID_Insumo

    def getCantidad_Requerida(self):
        return self.Cantidad_Requerida

    def getOrden_Preparacion(self):
        return self.Orden_Preparacion

    def getNombre_Receta(self):
        return self.Nombre_Receta

    def setID_Receta(self, id_receta):
        self.ID_Receta = id_receta

    def setID_Producto(self, id_producto):
        self.ID_Producto = id_producto

    def setID_Insumo(self, id_insumo):
        self.ID_Insumo = id_insumo

    def setCantidad_Requerida(self, cantidad_requerida):
        self.Cantidad_Requerida = cantidad_requerida

    def setOrden_Preparacion(self, orden_preparacion):
        self.Orden_Preparacion = orden_preparacion

    def setNombre_Receta(self, nombre_receta):
        self.Nombre_Receta = nombre_receta


        # Prueba
conexion = Conexion()
conexion.conectar()

receta = Receta(1, 1, 1, 2, 1, "Receta de Pan")


# Crear una instancia de la clase Receta
receta = Receta(1, 1, 1, 2, 1, "Receta de Pan")

# Obtener valores mediante get
print("ID de la Receta:", receta.getID_Receta())
print("ID del Producto:", receta.getID_Producto())
print("ID del Insumo:", receta.getID_Insumo())
print("Cantidad Requerida:", receta.getCantidad_Requerida())
print("Orden de Preparación:", receta.getOrden_Preparacion())
print("Nombre de la Receta:", receta.getNombre_Receta())

# Actualizar valores mediante set
receta.setNombre_Receta("Receta de Pan Multigrano")
receta.setCantidad_Requerida(3)

# Obtener nuevos valores con get
print("Nuevos valores:")
print("ID de la Receta:", receta.getID_Receta())
print("ID del Producto:", receta.getID_Producto())
print("ID del Insumo:", receta.getID_Insumo())
print("Cantidad Requerida:", receta.getCantidad_Requerida())
print("Orden de Preparación:", receta.getOrden_Preparacion())
print("Nombre de la Receta:", receta.getNombre_Receta())

# Cerrar 
conexion.cerrar_conexion() 

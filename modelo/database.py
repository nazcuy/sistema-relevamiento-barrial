import sqlite3
import os

class Database:
    def __init__(self):
        self.db_file = "relevamiento.db"
        self.connection = self.connect()
        self.crear_tabla()
        self.insertar_datos_ejemplo()
        
    def connect(self):
        try:
            return sqlite3.connect(self.db_file)
        except Exception as e:
            print(f"Error de conexión: {e}")
            return None
            
    def crear_tabla(self):
        query = """CREATE TABLE IF NOT EXISTS reportes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_problema TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            direccion TEXT NOT NULL,
            estado TEXT NOT NULL,
            fecha_reporte TEXT NOT NULL,
            observaciones TEXT
        )"""
        self.execute_query(query)
    
    def insertar_datos_ejemplo(self):
        # Verificar si ya hay datos
        if len(self.obtener_reportes()) == 0:
            datos_ejemplo = [
                ("Basura", "Contenedor de basura roto en la esquina", "Av. San Martín 123", "Pendiente", "2024-01-15", "Urgente reparación"),
                ("Iluminación", "Lámpara de la plaza no funciona", "Plaza Central", "En Proceso", "2024-01-10", "Ya se solicitó técnico"),
                ("Bache", "Bache grande en calle principal", "Calle Rivadavia 456", "Resuelto", "2024-01-05", "Reparado con asfalto"),
                ("Agua", "Fuga de agua en la vereda", "Calle Belgrano 789", "Pendiente", "2024-01-20", "Se necesita técnico especializado"),
                ("Otro", "Grafiti en pared municipal", "Av. Libertador 321", "En Proceso", "2024-01-18", "En proceso de limpieza")
            ]
            
            for dato in datos_ejemplo:
                self.crear_reporte(dato)
            
    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor
        except Exception as e:
            print(f"Error en consulta: {e}")
            return None
            
    def fetch_all(self, query, params=None):
        cursor = self.execute_query(query, params)
        return cursor.fetchall() if cursor else []
    
    # CRUD Operations
    def crear_reporte(self, data):
        query = """INSERT INTO reportes 
                (tipo_problema, descripcion, direccion, estado, fecha_reporte, observaciones)
                VALUES (?, ?, ?, ?, ?, ?)"""
        self.execute_query(query, data)
        
    def actualizar_reporte(self, data):
        query = """UPDATE reportes SET 
                tipo_problema = ?,
                descripcion = ?,
                direccion = ?,
                estado = ?,
                fecha_reporte = ?,
                observaciones = ?
                WHERE id = ?"""
        self.execute_query(query, data)
        
    def eliminar_reporte(self, id):
        query = "DELETE FROM reportes WHERE id = ?"
        self.execute_query(query, (id,))
        
    def obtener_reportes(self):
        return self.fetch_all("SELECT * FROM reportes")
    
    def obtener_reporte(self, id):
        return self.fetch_all("SELECT * FROM reportes WHERE id = ?", (id,))
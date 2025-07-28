from vista.dialogo_reporte import ReporteDialog
from modelo.reporte import Reporte
from PyQt5 import QtWidgets

class ReporteController:
    def __init__(self, main_view, db):
        self.main_view = main_view
        self.db = db
    
    def nuevo_reporte(self):
        dialog = ReporteDialog()
        if dialog.exec_():
            data = dialog.obtener_datos()
            # Crear reporte en la base de datos
            self.db.crear_reporte((
                data['tipo_problema'],
                data['descripcion'],
                data['direccion'],
                data['estado'],
                data['fecha_reporte'],
                data['observaciones']
            ))
            # Actualizar vista
            self.main_view.cargar_reportes(self.db.obtener_reportes())
    
    def editar_reporte(self):
        id_reporte = self.main_view.obtener_reporte_seleccionado()
        if id_reporte is None:
            return
            
        # Obtener reporte de la base de datos
        reporte_data = self.db.obtener_reporte(id_reporte)[0]
        reporte = Reporte(*reporte_data)
        
        dialog = ReporteDialog()
        dialog.cargar_datos(reporte)
        
        if dialog.exec_():
            data = dialog.obtener_datos()
            # Actualizar reporte en la base de datos
            self.db.actualizar_reporte((
                data['tipo_problema'],
                data['descripcion'],
                data['direccion'],
                data['estado'],
                data['fecha_reporte'],
                data['observaciones'],
                id_reporte
            ))
            # Actualizar vista
            self.main_view.cargar_reportes(self.db.obtener_reportes())
    
    def eliminar_reporte(self):
        id_reporte = self.main_view.obtener_reporte_seleccionado()
        if id_reporte is None:
            return
            
        confirm = QtWidgets.QMessageBox.question(
            self.main_view,
            "Confirmar",
            "¿Eliminar este reporte?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
        )
        
        if confirm == QtWidgets.QMessageBox.Yes:
            self.db.eliminar_reporte(id_reporte)
            self.main_view.cargar_reportes(self.db.obtener_reportes())
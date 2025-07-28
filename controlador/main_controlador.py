from vista.main_ventana import MainWindow
from controlador.reporte_controlador import ReporteController
from modelo.database import Database
from PyQt5 import QtWidgets
import csv
from datetime import datetime
from collections import Counter

class MainController:
    def __init__(self):
        self.view = MainWindow()
        self.db = Database()
        self.reporte_controller = ReporteController(self.view, self.db)
        
        # Conectar señales
        self.view.btn_actualizar.clicked.connect(self.cargar_reportes)
        self.view.btn_nuevo.clicked.connect(self.reporte_controller.nuevo_reporte)
        self.view.btn_editar.clicked.connect(self.reporte_controller.editar_reporte)
        self.view.btn_eliminar.clicked.connect(self.reporte_controller.eliminar_reporte)
        self.view.btn_exportar.clicked.connect(self.exportar_reportes)
        self.view.btn_limpiar_filtros.clicked.connect(self.limpiar_filtros)
        
        # Conectar filtros
        self.view.txt_buscar.textChanged.connect(self.aplicar_filtros)
        self.view.cb_filtro_tipo.currentTextChanged.connect(self.aplicar_filtros)
        self.view.cb_filtro_estado.currentTextChanged.connect(self.aplicar_filtros)
        
        self.cargar_reportes()
        self.mostrar_estadisticas()
        self.view.show()
        
    def cargar_reportes(self):
        reportes = self.db.obtener_reportes()
        self.view.cargar_reportes(reportes)
        self.actualizar_contador()
    
    def aplicar_filtros(self):
        texto_buscar = self.view.txt_buscar.text().lower()
        filtro_tipo = self.view.cb_filtro_tipo.currentText()
        filtro_estado = self.view.cb_filtro_estado.currentText()
        
        reportes = self.db.obtener_reportes()
        reportes_filtrados = []
        
        for reporte in reportes:
            # Filtro por texto
            if texto_buscar:
                descripcion = reporte[2].lower() if len(reporte) > 2 else ""
                direccion = reporte[3].lower() if len(reporte) > 3 else ""
                if texto_buscar not in descripcion and texto_buscar not in direccion:
                    continue
            
            # Filtro por tipo
            if filtro_tipo != "Todos":
                tipo = reporte[1] if len(reporte) > 1 else ""
                if tipo != filtro_tipo:
                    continue
            
            # Filtro por estado
            if filtro_estado != "Todos":
                estado = reporte[4] if len(reporte) > 4 else ""
                if estado != filtro_estado:
                    continue
            
            reportes_filtrados.append(reporte)
        
        self.view.cargar_reportes(reportes_filtrados)
        self.actualizar_contador()
    
    def limpiar_filtros(self):
        self.view.txt_buscar.clear()
        self.view.cb_filtro_tipo.setCurrentText("Todos")
        self.view.cb_filtro_estado.setCurrentText("Todos")
        self.cargar_reportes()
    
    def actualizar_contador(self):
        total = self.view.tabla_reportes.rowCount()
        self.view.statusbar.showMessage(f"Total de reportes: {total}")
    
    def mostrar_estadisticas(self):
        """Mostrar estadísticas básicas en un diálogo"""
        reportes = self.db.obtener_reportes()
        
        if not reportes:
            return
        
        # Contar por tipo
        tipos = [reporte[1] for reporte in reportes if len(reporte) > 1]
        contador_tipos = Counter(tipos)
        
        # Contar por estado
        estados = [reporte[4] for reporte in reportes if len(reporte) > 4]
        contador_estados = Counter(estados)
        
        # Crear mensaje de estadísticas
        stats_text = "📊 ESTADÍSTICAS GENERALES\n\n"
        stats_text += f"📋 Total de reportes: {len(reportes)}\n\n"
        
        stats_text += "🏷️ POR TIPO:\n"
        for tipo, cantidad in contador_tipos.items():
            porcentaje = (cantidad / len(reportes)) * 100
            stats_text += f"  • {tipo}: {cantidad} ({porcentaje:.1f}%)\n"
        
        stats_text += "\n📈 POR ESTADO:\n"
        for estado, cantidad in contador_estados.items():
            porcentaje = (cantidad / len(reportes)) * 100
            stats_text += f"  • {estado}: {cantidad} ({porcentaje:.1f}%)\n"
        
        # Mostrar en barra de estado
        self.view.statusbar.showMessage(f"Total: {len(reportes)} | Tipos: {len(contador_tipos)} | Estados: {len(contador_estados)}")
    
    def exportar_reportes(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.view,
            "Exportar Reportes",
            f"reportes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "Archivos CSV (*.csv)"
        )
        
        if filename:
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['ID', 'Tipo', 'Descripción', 'Dirección', 'Estado', 'Fecha', 'Observaciones'])
                    
                    for row in range(self.view.tabla_reportes.rowCount()):
                        fila = []
                        for col in range(self.view.tabla_reportes.columnCount()):
                            item = self.view.tabla_reportes.item(row, col)
                            fila.append(item.text() if item else "")
                        writer.writerow(fila)
                
                QtWidgets.QMessageBox.information(
                    self.view,
                    "Exportación Exitosa",
                    f"Los reportes se exportaron correctamente a:\n{filename}"
                )
            except Exception as e:
                QtWidgets.QMessageBox.critical(
                    self.view,
                    "Error de Exportación",
                    f"Error al exportar: {str(e)}"
                )
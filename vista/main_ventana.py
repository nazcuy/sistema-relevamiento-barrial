from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_ventana.ui", self)
        
        # Configurar tabla
        self.tabla_reportes.setColumnCount(6)
        self.tabla_reportes.setHorizontalHeaderLabels([
            "ID", "Tipo", "Descripción", "Dirección", "Estado", "Fecha"
        ])
        
        # Configurar tabla
        self.tabla_reportes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabla_reportes.setAlternatingRowColors(True)
        
        # Configurar colores de estado
        self.colores_estado = {
            "Pendiente": QColor(255, 255, 200),    # Amarillo claro
            "En Proceso": QColor(200, 255, 200),   # Verde claro
            "Resuelto": QColor(200, 200, 255)      # Azul claro
        }
    
    def cargar_reportes(self, reportes):
        self.tabla_reportes.setRowCount(0)
        for row, reporte in enumerate(reportes):
            self.tabla_reportes.insertRow(row)
            for col, dato in enumerate(reporte[:6]):  # Excluir observaciones
                item = QtWidgets.QTableWidgetItem(str(dato))
                self.tabla_reportes.setItem(row, col, item)
            
            # Aplicar color según el estado
            estado = reporte[4] if len(reporte) > 4 else "Pendiente"
            if estado in self.colores_estado:
                for col in range(6):
                    if self.tabla_reportes.item(row, col):
                        self.tabla_reportes.item(row, col).setBackground(self.colores_estado[estado])
    
    def obtener_reporte_seleccionado(self):
        fila = self.tabla_reportes.currentRow()
        if fila >= 0:
            return int(self.tabla_reportes.item(fila, 0).text())
        return None
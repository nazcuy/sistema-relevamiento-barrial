from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate

class ReporteDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/dialogo_reporte.ui", self)
        
        # Configurar valores por defecto
        self.fecha_reporte.setDate(QDate.currentDate())
        
        # Conectar botones
        self.btn_aceptar.clicked.connect(self.validar_y_aceptar)
        self.btn_cancelar.clicked.connect(self.reject)
        
        # Conectar validación en tiempo real
        self.txt_descripcion.textChanged.connect(self.validar_campos)
        self.txt_direccion.textChanged.connect(self.validar_campos)
    
    def validar_campos(self):
        """Validar campos en tiempo real"""
        descripcion_valida = len(self.txt_descripcion.toPlainText().strip()) > 0
        direccion_valida = len(self.txt_direccion.text().strip()) > 0
        
        # Cambiar color de fondo según validación
        if descripcion_valida:
            self.txt_descripcion.setStyleSheet("")
        else:
            self.txt_descripcion.setStyleSheet("background-color: #ffcccc;")
        
        if direccion_valida:
            self.txt_direccion.setStyleSheet("")
        else:
            self.txt_direccion.setStyleSheet("background-color: #ffcccc;")
        
        # Habilitar/deshabilitar botón aceptar
        self.btn_aceptar.setEnabled(descripcion_valida and direccion_valida)
    
    def validar_y_aceptar(self):
        """Validar todos los campos antes de aceptar"""
        descripcion = self.txt_descripcion.toPlainText().strip()
        direccion = self.txt_direccion.text().strip()
        
        errores = []
        
        if not descripcion:
            errores.append("La descripción es obligatoria")
        
        if not direccion:
            errores.append("La dirección es obligatoria")
        
        if errores:
            QtWidgets.QMessageBox.warning(
                self,
                "Campos Requeridos",
                "Por favor complete los siguientes campos:\n\n" + "\n".join(errores)
            )
            return
        
        self.accept()
    
    def cargar_datos(self, reporte):
        self.cb_tipo.setCurrentText(reporte.tipo_problema)
        self.txt_descripcion.setPlainText(reporte.descripcion)
        self.txt_direccion.setText(reporte.direccion)
        self.cb_estado.setCurrentText(reporte.estado)
        # Convertir fecha string a QDate
        fecha = QDate.fromString(reporte.fecha_reporte, "yyyy-MM-dd")
        self.fecha_reporte.setDate(fecha)
        self.txt_observaciones.setPlainText(reporte.observaciones or "")
        
        # Validar campos después de cargar
        self.validar_campos()
    
    def obtener_datos(self):
        return {
            'tipo_problema': self.cb_tipo.currentText(),
            'descripcion': self.txt_descripcion.toPlainText().strip(),
            'direccion': self.txt_direccion.text().strip(),
            'estado': self.cb_estado.currentText(),
            'fecha_reporte': self.fecha_reporte.date().toString("yyyy-MM-dd"),
            'observaciones': self.txt_observaciones.toPlainText().strip() or None
        }
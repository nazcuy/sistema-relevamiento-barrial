class Reporte:
    def __init__(self, id, tipo_problema, descripcion, direccion, estado, fecha_reporte, observaciones=None):
        self.id = id
        self.tipo_problema = tipo_problema
        self.descripcion = descripcion
        self.direccion = direccion
        self.estado = estado
        self.fecha_reporte = fecha_reporte
        self.observaciones = observaciones
        
    def to_dict(self):
        return {
            'id': self.id,
            'tipo_problema': self.tipo_problema,
            'descripcion': self.descripcion,
            'direccion': self.direccion,
            'estado': self.estado,
            'fecha_reporte': self.fecha_reporte,
            'observaciones': self.observaciones
        }
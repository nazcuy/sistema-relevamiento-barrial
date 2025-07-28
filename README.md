# 🏘️ Sistema de Relevamiento Barrial

Una aplicación de escritorio desarrollada en Python con PyQt5 para gestionar reportes de problemas barriales.

## 📋 Descripción

Este sistema permite a los administradores municipales o barriales gestionar reportes de problemas comunitarios como:
- 🗑️ Problemas de basura
- 💡 Problemas de iluminación
- 🕳️ Baches en calles
- 💧 Problemas de agua
- 🎨 Otros problemas urbanos

## ✨ Características

### 🎯 Funcionalidades Principales
- ✅ **Gestión completa de reportes** (Crear, Editar, Eliminar, Ver)
- 🔍 **Búsqueda y filtros** por tipo, estado y texto
- 📊 **Estadísticas** en tiempo real
- 📤 **Exportación** a archivos CSV
- 🎨 **Interfaz intuitiva** con colores según estado
- ✅ **Validaciones** en formularios

### 🎨 Interfaz de Usuario
- **Ventana principal** con tabla de reportes
- **Filtros dinámicos** por tipo y estado
- **Búsqueda en tiempo real**
- **Colores por estado**: Amarillo (Pendiente), Verde (En Proceso), Azul (Resuelto)
- **Formulario de reporte** con validaciones

### 💾 Base de Datos
- **SQLite** para almacenamiento local
- **Estructura simple** y eficiente
- **Datos de ejemplo** incluidos automáticamente

## 🛠️ Tecnologías Utilizadas

- **Python 3.11+**
- **PyQt5** - Framework de interfaz gráfica
- **SQLite** - Base de datos
- **Qt Designer** - Diseño de interfaces

## 📦 Instalación

### Requisitos Previos
```bash
# Instalar Python 3.11 o superior
# Descargar desde: https://www.python.org/downloads/
```

### Instalar Dependencias
```bash
pip install PyQt5
```

### Ejecutar la Aplicación
```bash
cd AppRelevamientoPyQT
python main.py
```

## 🏗️ Estructura del Proyecto

```
AppRelevamientoPyQT/
├── main.py                 # Punto de entrada de la aplicación
├── README.md              # Documentación del proyecto
├── relevamiento.db        # Base de datos SQLite
├── controlador/           # Lógica de control
│   ├── main_controlador.py
│   └── reporte_controlador.py
├── modelo/               # Acceso a datos
│   ├── database.py
│   └── reporte.py
├── vista/                # Interfaces de usuario
│   ├── main_ventana.py
│   └── dialogo_reporte.py
└── ui/                   # Archivos de diseño UI
    ├── main_ventana.ui
    └── dialogo_reporte.ui
```

## 🎮 Cómo Usar

### 1. **Ver Reportes**
- Al abrir la aplicación, verás todos los reportes en la tabla
- Los reportes están coloreados según su estado

### 2. **Crear Nuevo Reporte**
- Haz clic en "➕ Nuevo Reporte"
- Completa el formulario (descripción y dirección son obligatorios)
- Haz clic en "✅ Aceptar"

### 3. **Filtrar y Buscar**
- Usa la barra de búsqueda para buscar por descripción o dirección
- Usa los filtros de tipo y estado
- Haz clic en "🧹 Limpiar" para resetear filtros

### 4. **Editar Reporte**
- Selecciona un reporte en la tabla
- Haz clic en "✏️ Editar"
- Modifica los datos y acepta

### 5. **Eliminar Reporte**
- Selecciona un reporte en la tabla
- Haz clic en "🗑️ Eliminar"
- Confirma la eliminación

### 6. **Exportar Datos**
- Haz clic en "📊 Exportar"
- Elige ubicación y nombre del archivo CSV
- Los datos se exportarán con formato estándar

## 📊 Estados de Reportes

- **🟡 Pendiente**: Reporte nuevo, sin procesar
- **🟢 En Proceso**: Reporte siendo atendido
- **🔵 Resuelto**: Problema solucionado

## 🎨 Personalización

### Modificar Tipos de Problemas
Edita el archivo `vista/dialogo_reporte.py`:
```python
self.cb_tipo.addItems(["Basura", "Iluminación", "Bache", "Agua", "Otro"])
```

### Modificar Estados
Edita el archivo `vista/dialogo_reporte.py`:
```python
self.cb_estado.addItems(["Pendiente", "En Proceso", "Resuelto"])
```

### Cambiar Colores
Edita el archivo `vista/main_ventana.py`:
```python
self.colores_estado = {
    "Pendiente": QColor(255, 255, 200),    # Amarillo claro
    "En Proceso": QColor(200, 255, 200),   # Verde claro
    "Resuelto": QColor(200, 200, 255)      # Azul claro
}
```

## 🔧 Desarrollo

### Arquitectura MVC
- **Modelo**: `modelo/database.py` - Acceso a datos
- **Vista**: `vista/` - Interfaces de usuario
- **Controlador**: `controlador/` - Lógica de negocio

### Agregar Nuevas Funcionalidades
1. Modifica la interfaz en `ui/` o `vista/`
2. Actualiza la lógica en `controlador/`
3. Modifica la base de datos en `modelo/`

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz un fork del proyecto
2. Crea una rama para tu feature
3. Haz commit de tus cambios
4. Abre un Pull Request

## 📞 Contacto

Para preguntas o sugerencias, abre un issue en GitHub.

---

**Desarrollado con ❤️ usando Python y PyQt5** 
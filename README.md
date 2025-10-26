# 🌌 Proyecto Aurelion 

### Descripción general

El **Proyecto Aurelion** forma parte del curso *Fundamentos de Inteligencia Artificial* impulsado por **Guayerd & IBM SkillsBuild (2025)**.  
Su objetivo es integrar, limpiar y analizar datos de ventas mediante un conjunto de herramientas en **Python** que incluyen:

- Un **explorador interactivo** de documentación desde terminal.  
- Un **notebook en Jupyter (.ipynb)** con widgets, visualizaciones y KPIs interactivos.

---

### 🧩 Estructura del Proyecto


```
AurelionProyecto/
│
├── README.md                      # Este archivo
├── Informe.md                     # Documento principal del proyecto
├── Directrices.md                 # Registro del análisis y mejoras
├── Interactivo_LeerArchivo.py     # Módulo para lectura y carga de archivos
├── ExploradorDoc.py               # Navegador interactivo de documentación (terminal)
├── LeerArchivo.py                 # Módulo para lectura y carga de archivos
├── AnalisisVenta.ipynb            # Notebook interactivo con gráficos y KPIs
│
├── FlujoDelProceso.drawio         # Diagrama del flujo del programa
│
└── Aurelion/                      # Carpeta de datos
   ├── clientes.csv                # Base de datos de clientes
   ├── productos.csv               # Base de datos de productos
   ├── ventas.csv                  # Base de datos de ventas
   └── detalle_ventas.csv          # Base de datos de detalle de ventas
```

---

### ⚙️ Requisitos previos

Asegurate de tener instalado **Python 3.8 o superior** y las siguientes bibliotecas:

```bash
pip install pandas numpy openpyxl matplotlib seaborn
```

💡 *Para usar la versión .ipynb, también necesitás tener Jupyter Notebook o JupyterLab instalado.*

---

### 🚀 Cómo ejecutar el proyecto
🖥️ Modo terminal
1. Abrí una terminal (CMD, PowerShell o desde Visual Studio Code).
2. Navegá hasta la carpeta del proyecto:

   ```bash
   cd "ruta\a\AurelionProyecto"
   ```
3. Ejecutá el programa interactivo:

   ```bash
   python ExploradorDoc.py
   ```

---

### 📊 Modo interactivo (Jupyter Notebook) 

1. Abrí Jupyter y cargá el archivo AnalisisVenta.ipynbb
2. Ejecutá las celdas en orden para explorar los datos, generar gráficos y navegar por la
   documentación mediante widgets interactivos.

---

### 🧭 Funcionalidades principales

* **Exploración de documentación técnica desde terminal.**
* **Interfaz interactiva en Jupyter con filtros y gráficos.**
* **Análisis de ventas por cliente, producto, ciudad y medio de pago.**
* **KPIs automáticos: ticket promedio, total vendido, clientes inactivos.**
* **Limpieza, validación y resumen de datos.**
* **Compatibilidad multiplataforma (Windows / Linux / macOS).**

---

### 🧱 Modelos incluidos

* **Modelo Conceptual (ER):** Relaciones entre Clientes, Ventas, Detalle_Ventas y Productos.
* **Modelo Lógico:** Definición de tablas y claves principales/foráneas.
* **Modelo Físico:** Representación de las bases de datos en formato `.csv`.
* **Diagrama de Flujo:** Representa el proceso de análisis y visualización.

---

### 💬 Créditos
```
📌 Autora: Nancy Vargas
🎓 Curso: Fundamentos de Inteligencia Artificial – Guayerd & IBM SkillsBuild
📅 Año: 2025
💻 Lenguaje: Python 3.
📚 Temática: Integración y análisis de datos de ventas
🎨 Formatos: CLI + Jupyter Notebook
```
---


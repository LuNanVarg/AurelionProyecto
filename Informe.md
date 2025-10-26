
# 🌟 Información del Proyecto Aurelion 

---

## 🟢 1. Preparación del entorno y archivos

### ✅ Pasos iniciales
1. Crear carpeta **Carlos Padilla - Proyecto Aurelion**  
2. Descargar archivos `.xlsx` desde Google Drive  
3. Abrir carpeta en VS Code → **Add Folder to Workspace**  
4. Revisar estructura de datos de cada archivo  
5. Crear archivo `.md` para documentar el proyecto  

> 💡 Tip: Mantener los archivos originales intactos para respaldos

---

## 🟡 2. Tablas y estructura de datos
```
| Tabla | Archivo | Columnas | Registros | Observaciones |
|-------|--------|----------|----------|---------------|
| Clientes | `clientes.xlsx` | 5 | 100 | Revisar duplicados en `nombre_cliente` y `email` |
| Productos | `productos.xlsx` | 4 | 100 | Verificar categoría y duplicados en `nombre_producto` |
| Ventas | `ventas.xlsx` | 6 | 120 | Clientes pueden tener varias ventas |
| Detalle_Ventas | `detalle_ventas.xlsx` | 6 | 343 | Cada venta puede tener varios productos |
```
> 📌 Notas de validación: fechas correctas, IDs positivos, precios > 0, integridad referencial

---

## 🔵 3. Requisitos de instalación

### 💻 Software
- Python ≥ 3.8  
- Editor: VS Code o PyCharm  

### 📦 Librerías
```bash
pip install pandas numpy openpyxl matplotlib seaborn
````

> ⚡ Tip: Mantener las versiones indicadas para reproducibilidad

---

## 🟠 4. Estándares de datos y validaciones

| Concepto         | Estándar          |
| ---------------- | ----------------- |
| Fechas           | `YYYY-MM-DD`      |
| IDs              | Enteros positivos |
| Precios/Importes | 2 decimales       |
| Cantidad         | Enteros positivos |

### Validaciones Clave

1. `fecha_alta` < `fecha` de venta
2. `precio_unitario` > 0
3. `importe` = `cantidad * precio_unitario`
4. Integridad referencial de IDs
5. Evitar duplicados en emails y nombres de productos

> ✅ Esto garantiza KPIs confiables y análisis precisos

---

## 🟣 5. Problema y solución

### ❗ Problema

* No hay visión consolidada de ventas
* Difícil segmentación de clientes por comportamiento
* Información por ciudad, categoría y medio de pago dispersa

### 💡 Solución

* Integrar todas las tablas en un **DataFrame consolidado**
* Limpiar y validar datos
* Generar reportes y KPIs: ventas, clientes, ingresos, top 5 clientes
* Identificar clientes sin compras

---

## 🟤 6. KPIs principales

* Clientes totales, activos e inactivos
* Ventas totales y ticket promedio
* Ingresos por categoría, medio de pago y ciudad
* Top 5 clientes por monto total

> 📊 Todos los KPIs se calculan a partir del DataFrame consolidado

---

## 🔴 7. Diagrama de flujo del proceso

```text
[Inicio] 
   │
   ▼
[Cargar archivos XLSX en DataFrames]
   │
   ▼
[EDA: inspección de columnas, tipos, nulos]
   │
   ▼
[Limpieza y validación]
   ├─ Validar formatos y tipos
   ├─ Corregir categorías
   └─ Recalcular importes
   │
   ▼
[Integración de datos: merges]
   │
   ▼
[Validación de integridad]
   │
   ▼
[Calcular KPIs y generar reportes]
   │
   ▼
[Exportar: CSV y consola]
   │
   ▼
[Fin]
```

---

## ⚡ 8. Pseudocódigo resumido

```text
INICIO_PROGRAMA

// Cargar datos
df_clientes = CARGAR_EXCEL("clientes.xlsx")
df_productos = CARGAR_EXCEL("productos.xlsx")
df_ventas = CARGAR_EXCEL("ventas.xlsx")
df_detalle_ventas = CARGAR_EXCEL("detalle_ventas.xlsx")

// Respaldo de datos originales
COPIAR(df_clientes, df_productos, df_ventas, df_detalle_ventas)

// EDA
INSPECCIONAR(df_clientes, df_productos, df_ventas, df_detalle_ventas)

// Limpieza y validación
CONVERTIR_FECHAS()
VERIFICAR_DUPLICADOS()
CORREGIR_CATEGORIAS()
RECALCULAR_IMPORTES()
VALIDAR_INTEGRIDAD()

// Integración
MERGE(df_ventas, df_detalle_ventas)
MERGE(result, df_productos)
MERGE(result, df_clientes)

// KPIs
CALCULAR_CLIENTES_ACTIVOS_INACTIVOS()
CALCULAR_TOTAL_VENTAS_INGRESOS_TICKET()
GENERAR_REPORTES()

// Exportación
GUARDAR_CSV(result)

FIN_PROGRAMA
```

---

## 📌 9. Notas finales

* Mantener los datos originales intactos
* Revisar las validaciones antes de generar análisis
* Actualizar este documento si se agregan nuevas tablas o KPIs

---

### 💬 Créditos

📌 **Autora:** Nancy Vargas
🎓 **Curso:** Fundamentos de Inteligencia Artificial – Guayerd & IBM SkillsBuild
📅 **Año:** 2025
💻 **Lenguaje:** Python 3.x
📚 **Temática:** Integración y análisis de datos de ventas

---
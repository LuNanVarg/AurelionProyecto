# -------------------------------------------------------
#   AurelionProyecto ==> leerArchivo.py
# -------------------------------------------------------
#  Este script carga archivos CSV del proyecto Aurelion,
#  muestra vistas previas, combina datos y guarda resultados.
# -------------------------------------------------------

import pandas as pd
import os

# ---------------------------
# Define la ruta base
# ---------------------------

ruta_base = r"C:\Users\Luna\Desktop\Guayerd\AurelionProyecto\Aurelion"

# Verificar que la carpeta exista
if not os.path.exists(ruta_base):
    print(f"❌ La carpeta '{ruta_base}' no existe.")
    exit()

# ---------------------------
# Lista los archivos disponibles
# ---------------------------
print("📁 Archivos disponibles en la carpeta Aurelion:")
csv_disponibles = [f for f in os.listdir(ruta_base) if f.endswith(".csv")]
if not csv_disponibles:
    print("⚠️ No se encontraron archivos CSV en la carpeta.")
    exit()
for archivo in csv_disponibles:
    print("  -", archivo)

# ---------------------------
# Función para leer CSV de forma segura
# ---------------------------
def leer_csv(nombre_archivo):
    ruta = os.path.join(ruta_base, nombre_archivo)
    if not os.path.exists(ruta):
        print(f"❌ Archivo no encontrado: {nombre_archivo}")
        return pd.DataFrame()  # Devuelve un DataFrame vacío
    try:
        df = pd.read_csv(ruta)
        if df.empty:
            print(f"⚠️ El archivo '{nombre_archivo}' está vacío.")
        return df
    except Exception as e:
        print(f"❌ Error al leer '{nombre_archivo}': {e}")
        return pd.DataFrame()

# ---------------------------
# Lee todos los CSV principales
# ---------------------------
clientes = leer_csv("clientes.csv")
productos = leer_csv("productos.csv")
ventas = leer_csv("ventas.csv")
detalle_ventas = leer_csv("detalle_ventas.csv")

# ---------------------------
# Muestra las vistas previas
# ---------------------------
def mostrar_preview(df, nombre):
    print(f"\n👀 Vista previa de {nombre}:")
    if df.empty:
        print("  (Sin datos)")
    else:
        print(df.head())  # Muestra primeras 5 filas

mostrar_preview(clientes, "Clientes")
mostrar_preview(productos, "Productos")
mostrar_preview(ventas, "Ventas")
mostrar_preview(detalle_ventas, "Detalle de Ventas")

# ---------------------------
# Combina datos: Clientes + Ventas
# ---------------------------
print("\n🔗 Combinando Clientes con Ventas...")
if not clientes.empty and not ventas.empty:
    clientes_ventas = pd.merge(ventas, clientes, on="id_cliente", how="left")
    mostrar_preview(clientes_ventas, "Clientes + Ventas")
else:
    clientes_ventas = pd.DataFrame()
    print("⚠️ No se puede combinar: falta datos en clientes o ventas.")

# ---------------------------
# Combina detalles de ventas + Productos + Ventas
# ---------------------------
print("\n🔗 Combinando Detalle de Ventas con Productos y Ventas...")
if not detalle_ventas.empty and not productos.empty and not ventas.empty:
    #Primero combinamos detalle_ventas con productos
    detalle_prod = pd.merge(detalle_ventas, productos, on="id_producto", how="left")
    # Despues Combinamos con ventas para obtener datos de cliente y fecha
    ventas_completo = pd.merge(detalle_prod, ventas, on="id_vent", how="left")
    # Finalmente, agregamos info del cliente
    if not clientes.empty:
        ventas_completo = pd.merge(ventas_completo, on="id_cliente", how="left")
    mostrar_preview(ventas_completo, "Informe completo de ventas")
else:
    ventas_completo = pd.DataFrame()
    print(" No se generar informe completo: falta detalle_ventas, productos o ventas.")    

# ---------------------------
# Guarda el resultado combinado
# ---------------------------
if not clientes_ventas.empty:
    salida_clientes_ventas = os.path.join(ruta_base, "clientes_ventas.csv")
    clientes_ventas.to_csv(salida_clientes_ventas, index=False)
    print(f"\n✅ Archivo 'clientes_ventas.csv' en: {salida_clientes_ventas}")

if not ventas_completo.empty:
    salida_ventas_completo = os.path.join(ruta_base, "ventas_completo.csv")
    ventas_completo.to_csv(salida_ventas_completo, index=False)
    print(f"\n✅ Archivo 'ventas_completo.csv' en: {salida_ventas_completo}")

      

# -------------------------------------------------------
#   Conclusión de este script:
# -------------------------------------------------------
# - Verifica que la carpeta exista antes de intentar leer.
# - Lista todos los CSV disponibles automáticamente.
# - Función lee_csv que maneja errores y archivos vacíos.
# - Vista previa (mostrar_preview) para todos los DataFrames.
# - Combina clientes con ventas solo si ambos archivos existen y tienen datos.
# - Guarda el archivo combinado de forma segura, con manejo de errores.
# - Comentarios paso a paso para aprender mientras lo usás.
# -------------------------------------------------------

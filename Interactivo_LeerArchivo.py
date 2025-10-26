# -------------------------------------------------------
#   AurelionProyecto ==> Interactivo_LeerArchivo.py
# -------------------------------------------------------
#  Script interactivo para explorar y combinar CSV del proyecto Aurelion
# -------------------------------------------------------

import pandas as pd
import os

# ---------------------------
# Definir la ruta base
# ---------------------------
ruta_base = r"C:\Users\Luna\Desktop\Guayerd\AurelionProyecto\Aurelion"

if not os.path.exists(ruta_base):
    print(f"❌ La carpeta '{ruta_base}' no existe.")
    exit()

# ---------------------------
# Funciones de utilidad
# ---------------------------

def listar_csv():
    """ Lista archivos CSV en la carpeta """
    csvs = [f for f in os.listdir(ruta_base) if f.endswith(".csv")]
    if not csvs:
        print("⚠️ No hay archivos CSV disponibles.")
    else:
        print("\n📁 Archivos CSV disponibles:")
        for i, f in enumerate(csvs, 1):
            print(f"  {i}. {f}")
    return csvs

def leer_csv(nombre_archivo):
    """ Lee un CSV y devuelve DataFrame """
    ruta = os.path.join(ruta_base, nombre_archivo)
    if not os.path.exists(ruta):
        print(f"❌ Archivo no encontrado: {nombre_archivo}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(ruta)
        if df.empty:
            print(f"⚠️ El archivo '{nombre_archivo}' está vacío.")
        return df
    except Exception as e:
        print(f"❌ Error al leer '{nombre_archivo}': {e}")
        return pd.DataFrame()

def mostrar_preview(df, nombre):
    """ Muestra las primeras filas de un DataFrame """
    print(f"\n👀 Preview de {nombre}:")
    if df.empty:
        print("  (Sin datos)")
    else:
        print(df.head())

def guardar_csv(df, nombre_archivo):
    """ Guarda un DataFrame en CSV """
    if df.empty:
        print(f"⚠️ No hay datos para guardar en '{nombre_archivo}'.")
        return
    ruta = os.path.join(ruta_base, nombre_archivo)
    df.to_csv(ruta, index=False)
    print(f"\n✅ Archivo guardado: {ruta}")

# ---------------------------
# Variables globales para DataFrames
# ---------------------------
clientes = pd.DataFrame()
productos = pd.DataFrame()
ventas = pd.DataFrame()
detalle_ventas = pd.DataFrame()
clientes_ventas = pd.DataFrame()
ventas_completo = pd.DataFrame()

# ---------------------------
# Función principal del menú
# ---------------------------
def menu():
    global clientes, productos, ventas, detalle_ventas, clientes_ventas, ventas_completo

    while True:
        print("\n" + "="*60)
        print(" 🚀 EXPLORADOR INTERACTIVO DE CSV - AURELION ")
        print("="*60)
        print("[1] Listar archivos CSV disponibles")
        print("[2] Ver preview de un archivo CSV")
        print("[3] Combinar Clientes + Ventas")
        print("[4] Combinar Detalle de Ventas + Productos + Ventas + Clientes")
        print("[5] Guardar archivos combinados")
        print("[0] Salir")
        print("-"*60)

        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "0":
            print("\n¡Hasta luego! 👋")
            break

        elif opcion == "1":
            listar_csv()

        elif opcion == "2":
            csvs = listar_csv()
            if csvs:
                try:
                    num = int(input("Número del archivo a mostrar: ").strip())
                    archivo = csvs[num-1]
                    df = leer_csv(archivo)
                    mostrar_preview(df, archivo)
                except (ValueError, IndexError):
                    print("Número inválido.")

        elif opcion == "3":
            # Leer archivos necesarios
            clientes = leer_csv("clientes.csv")
            ventas = leer_csv("ventas.csv")
            if not clientes.empty and not ventas.empty:
                clientes_ventas = pd.merge(ventas, clientes, on="id_cliente", how="left")
                mostrar_preview(clientes_ventas, "Clientes + Ventas")
            else:
                print("⚠️ No se puede combinar clientes y ventas.")

        elif opcion == "4":
            # Leer archivos necesarios
            detalle_ventas = leer_csv("detalle_ventas.csv")
            productos = leer_csv("productos.csv")
            ventas = leer_csv("ventas.csv")
            clientes = leer_csv("clientes.csv")

            if not detalle_ventas.empty and not productos.empty and not ventas.empty:
                detalle_prod = pd.merge(detalle_ventas, productos, on="id_producto", how="left")
                ventas_completo = pd.merge(detalle_prod, ventas, on="id_venta", how="left")
                if not clientes.empty:
                    ventas_completo = pd.merge(ventas_completo, clientes, on="id_cliente", how="left")
                mostrar_preview(ventas_completo, "Informe completo de ventas")
            else:
                print("⚠️ No se puede generar informe completo: falta detalle_ventas, productos o ventas.")

        elif opcion == "5":
            if not clientes_ventas.empty:
                guardar_csv(clientes_ventas, "clientes_ventas.csv")
            if not ventas_completo.empty:
                guardar_csv(ventas_completo, "ventas_completo.csv")
            if clientes_ventas.empty and ventas_completo.empty:
                print("⚠️ No hay archivos combinados para guardar.")

        else:
            print("Opción inválida. Intentá de nuevo.")

# ---------------------------
# Ejecutar menú
# ---------------------------
if __name__ == "__main__":
    menu()

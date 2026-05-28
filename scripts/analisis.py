import pandas as pd

def analizar_ventas():

    try:
        # Leer archivo CSV
        df = pd.read_csv("datos/ventas.csv")

        # Crear columna total
        df["total"] = df["cantidad"] * df["precio"]

        # Mostrar ventas totales
        ventas_totales = df["total"].sum()
        print("Ventas totales:", ventas_totales)

        # Buscar producto más vendido
        producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
        print("Producto más vendido:", producto_mas_vendido)

        # Mostrar cada producto
        print("\nListado de productos:")

        for producto in df["producto"]:
            print("-", producto)

        # Condicional simple
        if ventas_totales > 30000:
            print("\nLas ventas fueron altas")
        else:
            print("\nLas ventas fueron bajas")

    except Exception as e:
        print("Ocurrió un error:", e)

# Ejecutar función
analizar_ventas()

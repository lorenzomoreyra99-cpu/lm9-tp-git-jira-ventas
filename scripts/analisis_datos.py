import pandas as pd
import matplotlib.pyplot as plt

def analizar_ventas():
    try:
        # 1. Leer archivo CSV
        df = pd.read_csv("datos/ventas.csv")

        # 2. Crear columna total
        df["total"] = df["cantidad"] * df["precio"]

        # 3. Mostrar ventas totales
        ventas_totales = df["total"].sum()
        print("Ventas totales:", ventas_totales)

        # 4. Buscar producto más vendido
        producto_mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
        print("Producto más vendido:", producto_mas_vendido)

        # 5. Mostrar cada producto con un bucle
        print("\nListado de productos:")
        for producto in df["producto"]:
            print("-", producto)

        # 6. Condicional simple
        if ventas_totales > 30000:
            print("\nLas ventas fueron altas")
        else:
            print("\nLas ventas fueron bajas")

        # 7. Crear y guardar el gráfico (AQUÍ ADENTRO para que no de error)
        ventas_por_producto = df.groupby("producto")["cantidad"].sum()
        ventas_por_producto.plot(kind="bar")
        plt.title("Ventas de camisetas")
        
        # Guardar en la carpeta resultados
        plt.savefig("resultados/grafico_ventas.png")
        print("\nGráfico generado correctamente")

    except Exception as e:
        print("Ocurrió un error:", e)

# Ejecutar función
analizar_ventas()
# Script revisado por Luis - QA y documentacion


import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV desde una ruta relativa
df = pd.read_csv('datos/ventas.csv')

# Calcular el total de cada venta
df['total'] = df['cantidad'] * df['precio']

# Calcular ventas totales
ventas_totales = df['total'].sum()

# Obtener producto más vendido
producto_mas_vendido = (
    df.groupby('producto')['cantidad']
    .sum()
    .idxmax()
)

# Procesar fechas para agrupar ventas por mes
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
df['mes'] = df['fecha_venta'].dt.month

ventas_mes = (
    df.groupby('mes')['total']
    .sum()
)

# Generar gráfico
ventas_mes.plot()

plt.title('Ventas por mes')
plt.xlabel('Mes')
plt.ylabel('Monto')

plt.savefig('resultados/grafico_ventas.png')
plt.show()

print('Ventas totales:', ventas_totales)
print('Producto más vendido:', producto_mas_vendido)

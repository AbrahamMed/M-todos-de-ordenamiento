#seleccion
def clasificar_tiempos(arr):
    n = len(arr)
    # Recorrer
    for i in range(n):
        min_idx = i
        # Buscar mínimo
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Intercambio
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Datos para clasificar tiempos
tiempos_segundos = [12.4, 9.8, 14.2, 10.5, 11.1, 10.0]
print("Tiempos registrados (seg):", tiempos_segundos)

clasificar_tiempos(tiempos_segundos)
print("Tiempos clasificados (rápidos primero):", tiempos_segundos)
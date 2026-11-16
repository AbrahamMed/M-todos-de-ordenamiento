#burbuja
def ordenar_calificaciones(arr):
    n = len(arr)
    # Recorrer
    for i in range(n):
        # Comparar adyacentes
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Datos para ordenar las calificaciones
calificaciones = [85, 60, 92, 70, 100, 55, 78]
print("Calificaciones originales:", calificaciones)

ordenar_calificaciones(calificaciones)
print("Calificaciones ordenadas:", calificaciones)
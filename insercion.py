#insercion
def ordenar_precios(arr):
    # Elemento actual
    for i in range(1, len(arr)):
        precio_actual = arr[i]
        pos = i

        # Desplazar mayores
        while pos > 0 and arr[pos - 1] > precio_actual:
            arr[pos] = arr[pos - 1]
            pos -= 1

        # Insertar
        arr[pos] = precio_actual

# Datos para ordenar los precios
precios = [250.50, 15.00, 99.90, 45.00, 120.75]
print("Precios desordenados: $", precios)

ordenar_precios(precios)
print("Precios de menor a mayor: $", precios)
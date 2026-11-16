def shell_sort(arr):
  n = len(arr)
  brecha = n // 2
  print(f"\n[Paso a paso ShellSort] Lista inicial: {arr}")
  while brecha > 0:
    print(f"-> Intervalo (brecha) actual: {brecha}")
    for i in range(brecha, n):
      temporal = arr[i]
      j = i
      print(
          f"   Comparando e insertando el elemento {temporal} (posición {i}) con"
          f" brecha {brecha}"
      )
      while j >= brecha and arr[j - brecha] > temporal:
        print(
            f"      Moviendo {arr[j - brecha]} desde la posición {j - brecha}"
            f" hacia la posición {j}"
        )
        arr[j] = arr[j - brecha]
        j -= brecha
      arr[j] = temporal
      print(f"   Estado parcial de la lista: {arr}")
    brecha //= 2
  return arr


def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivote = arr[len(arr) // 2]
  print(f"\n[Paso a paso Quicksort] Sublista a dividir: {arr} | Pivote: {pivote}")
  izquierda = [x for x in arr if x < pivote]
  medio = [x for x in arr if x == pivote]
  derecha = [x for x in arr if x > pivote]
  print(
      f"   Menores que {pivote}: {izquierda} | Iguales: {medio} | Mayores:"
      f" {derecha}"
  )

  izquierda_ordenada = quick_sort(izquierda)
  derecha_ordenada = quick_sort(derecha)
  resultado = izquierda_ordenada + medio + derecha_ordenada
  print(f"   Sublista unida: {resultado}")
  return resultado


def heapify(arr, n, i):
  mayor = i
  izq = 2 * i + 1
  der = 2 * i + 2

  if izq < n and arr[izq] > arr[mayor]:
    mayor = izq
  if der < n and arr[der] > arr[mayor]:
    mayor = der

  if mayor != i:
    print(
        f"   [Heapify] Intercambiando padre {arr[i]} con hijo mayor {arr[mayor]}"
    )
    arr[i], arr[mayor] = arr[mayor], arr[i]
    heapify(arr, n, mayor)


def heap_sort(arr):
  n = len(arr)
  print(f"\n[Paso a paso Heapsort] Construyendo montículo inicial: {arr}")
  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)
  print(f"-> Montículo máximo construido: {arr}")

  for i in range(n - 1, 0, -1):
    print(
        f"-> Intercambiando raíz {arr[0]} con el último elemento {arr[i]} y"
        " reduciendo heap"
    )
    arr[i], arr[0] = arr[0], arr[i]
    print(f"   Estado parcial: {arr}")
    heapify(arr, i, 0)
  return arr


def counting_sort_radix(arr, exp):
  n = len(arr)
  salida = [0] * n
  conteo = [0] * 10

  for i in range(n):
    indice = arr[i] // exp
    conteo[indice % 10] += 1

  for i in range(1, 10):
    conteo[i] += conteo[i - 1]

  i = n - 1
  while i >= 0:
    indice = arr[i] // exp
    salida[conteo[indice % 10] - 1] = arr[i]
    conteo[indice % 10] -= 1
    i -= 1

  for i in range(n):
    arr[i] = salida[i]
  print(f"   Ordenado según el dígito actual (exp={exp}): {arr}")


def radix_sort(arr):
  if not arr:
    return arr
  print(f"\n[Paso a paso Radix Sort] Lista inicial: {arr}")
  valor_maximo = max(arr)
  exp = 1
  while valor_maximo // exp > 0:
    print(f"-> Procesando por posición de dígito (exp={exp}):")
    counting_sort_radix(arr, exp)
    exp *= 10
  return arr


def solicitar_datos():
  while True:
    try:
      total_numeros = int(input("\n¿Cuántos números deseas ingresar?: "))
      if total_numeros > 0:
        break
      print("Ingresa un número mayor a 0.")
    except ValueError:
      print("Error: Ingresa un número entero válido.")

  lista_datos = []
  print(f"Ingresa los {total_numeros} números:")
  for i in range(total_numeros):
    while True:
      try:
        lista_datos.append(int(input(f"  Número {i + 1}: ")))
        break
      except ValueError:
        print("Error: Ingresa un valor numérico válido.")
  return lista_datos


def main():
  while True:
    print("\n====================")
    print(" MÉTODOS DE ORDENAMIENTO ")
    print("====================")
    print("1. ShellSort")
    print("2. Quicksort")
    print("3. Heapsort")
    print("4. Radix Sort")
    print("5. Salir")

    opcion = input("\nElige una opción (1-5): ")

    if opcion == "5":
      print("\nSaliendo del programa...")
      break

    if opcion in ["1", "2", "3", "4"]:
      datos = solicitar_datos()
      print(f"\nLista original: {datos}")
      datos_copia = list(datos)

      if opcion == "1":
        resultado, nombre = shell_sort(datos_copia), "ShellSort"
      elif opcion == "2":
        resultado, nombre = quick_sort(datos_copia), "Quicksort"
      elif opcion == "3":
        resultado, nombre = heap_sort(datos_copia), "Heapsort"
      elif opcion == "4":
        resultado, nombre = radix_sort(datos_copia), "Radix Sort"

      print(f"\n=== Resultado Final con {nombre} === \n{resultado}\n")
    else:
      print("\nOpción no válida. Elige entre 1 y 5.")


if __name__ == "__main__":
  main()
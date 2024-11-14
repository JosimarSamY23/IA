import random
import time
from os import system

def limpiar_pantalla(apretar=False, limpiar=True):
    if apretar:
        input("Ingresa una tecla para continuar...")

    if limpiar:
        system('cls')

# METODOS DE ORDENAMIENTO #
# Aumentar el rango de numeros para ver con mayor precisión el tiempo empleado en realizar el ordenamiento
def generar_lista(tamano=100, limite=20):
    return [random.randint(1, limite) for _ in range(tamano)]

def burbuja(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista) -i -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def seleccion(lista):
    for i in range(len(lista)):
        min_index = i

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j

        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > key:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key

    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    centro = [x for x in lista if x == pivot]
    derecha = [x for x in lista if x > pivot]

    return quicksort(izquierda) + centro + quicksort(derecha)

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    result = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            result.append(izquierda[i])
            i += 1
        else:
            result.append(derecha[j])
            j += 1

    result.extend(izquierda[i:])
    result.extend(derecha[j:])
    return result

def shell_sort(lista):
    gap = len(lista) // 2

    while gap > 0:
        for i in range(gap, len(lista)):
            temp = lista[i]
            j = i

            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap

            lista[j] = temp
        gap //= 2

    return lista

def heapify(lista, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] < lista[l]:
        largest = l
        
    if r < n and lista[largest] < lista[r]:
        largest = r

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest)

def heap_sort(lista):
    for i in range(len(lista) // 2 - 1, -1, -1):
        heapify(lista, len(lista), i)

    for i in range(len(lista) - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

    return lista

def counting_sort(lista):
    max_val = max(lista)
    m = max_val + 1
    count = [0] * m

    for a in lista:
        count[a] += 1

    i = 0

    for a in range(m):            
        for _ in range(count[a]):  
            lista[i] = a
            i += 1

    return lista

def radix_sort(lista):
    RADIX = 10
    max_digit = max(lista)
    exp = 1

    while max_digit // exp > 0:
        counting_sort_radix(lista, exp, RADIX)
        exp *= RADIX

    return lista

def counting_sort_radix(lista, exp, RADIX):
    output = [0] * len(lista)
    count = [0] * RADIX

    for i in lista:
        index = i // exp
        count[index % RADIX] += 1

    for i in range(1, RADIX):
        count[i] += count[i - 1]

    for i in range(len(lista) - 1, -1, -1):
        index = lista[i] // exp
        output[count[index % RADIX] - 1] = lista[i]
        count[index % RADIX] -= 1

    for i in range(len(lista)):
        lista[i] = output[i]

def bucket_sort(lista):
    bucket = []
    num_buckets = round(len(lista) ** 0.5)

    for i in range(num_buckets):
        bucket.append([])

    max_val = max(lista)

    for j in lista:
        index_b = min(j * num_buckets // (max_val + 1), num_buckets - 1)
        bucket[index_b].append(j)

    for i in range(num_buckets):
        bucket[i] = insercion(bucket[i])

    return [item for sublist in bucket for item in sublist]

def gnome_sort(lista):
    index = 0

    while index < len(lista):
        if index == 0:
            index += 1
        if lista[index] >= lista[index - 1]:
            index += 1
        else:
            lista[index], lista[index - 1] = lista[index - 1], lista[index]
            index -= 1

    return lista
# FIN METODOS DE ORDENAMIENTO #

# METODOS FUNCION PRINCIPAL #
def medir_tiempo(funcion, lista, ordenamiento):
    start = time.time()
    resultado = funcion(lista[:])  # Usamos lista[:] para pasar una copia y no modificar la original
    end = time.time()

    print(ordenamiento)
    print("Resultado:", resultado)
    print(f"Tiempo de ejecución: {end - start:.6f} segundos")

def menu():
    print("\nSelecciona un método de ordenamiento:")
    print("\t1. Burbuja")
    print("\t2. Selección")
    print("\t3. Inserción")
    print("\t4. QuickSort")
    print("\t5. MergeSort")
    print("\t6. Shell Sort")
    print("\t7. Heap Sort")
    print("\t8. Counting Sort")
    print("\t9. Radix Sort")
    print("\t10. Bucket Sort")
    print("\t11. Gnome Sort")
    print("\t12. Salir")

def main():
    lista = generar_lista()

    while True:
        print("Lista original:", lista)

        menu()
        opcion = input("Elige una opción: ")
        print()

        if opcion.isdigit():
            opc = int(opcion)

            if 0 < opc < 12:
                limpiar_pantalla()

        if opcion == "1":
            medir_tiempo(burbuja,lista,"Ordenando por Burbuja...")
        
        elif opcion == "2":
            medir_tiempo(seleccion,lista,"Ordenando por Selección...")
        
        elif opcion == "3":
            medir_tiempo(insercion,lista,"Ordenando por Inserción...")
        
        elif opcion == "4":
            medir_tiempo(quicksort,lista,"Ordenando por QuickSort...")
        
        elif opcion == "5":
            medir_tiempo(mergesort,lista,"Ordenando por MergeSort...")

        elif opcion == "6":
            medir_tiempo(shell_sort,lista,"Ordenando por Shell Sort...")

        elif opcion == "7":
            medir_tiempo(heap_sort,lista,"Ordenando por Heap Sort...")

        elif opcion == "8":
            medir_tiempo(counting_sort,lista,"Ordenando por Counting Sort...")

        elif opcion == "9":
            medir_tiempo(radix_sort,lista,"Ordenando por Radix Sort...")

        elif opcion == "10":
            medir_tiempo(bucket_sort,lista,"Ordenando por Bucket Sort...")

        elif opcion == "11":
            medir_tiempo(gnome_sort,lista,"Ordenando por Gnome Sort...")

        elif opcion == "12":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")

        limpiar_pantalla(True)
# FIN METODOS FUNCION PRINCIPAL #

if __name__ == "__main__":
    limpiar_pantalla()
    main()

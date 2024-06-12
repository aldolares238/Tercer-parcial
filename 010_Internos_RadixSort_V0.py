#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: RadixSort

import matplotlib.pyplot as plt

def counting_sort(arr, exp):
    # Inicializar el tamaño del array
    n = len(arr)
    
    # Inicializar el output array
    output = [0] * n
    
    # Inicializar el array de conteo
    count = [0] * 10
    
    # Contar ocurrencias de los dígitos en el lugar exp
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Actualizar count[i] para contener la posición real de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Construir el output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copiar el output array a arr[], para que arr[] contenga los números ordenados según el dígito actual
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar el número máximo para saber el número de dígitos
    max1 = max(arr)
    
    # Hacer counting sort para cada dígito. En lugar de pasar el número del dígito, exp es 10^i
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Datos de entrada para el algoritmo RadixSort
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Imprimir el array original
print("Array original:")
print(arr)

# Llamar a la función radix_sort
radix_sort(arr)

# Imprimir el array ordenado
print("Array ordenado:")
print(arr)

# Visualizar los resultados usando matplotlib
plt.bar(range(len(arr)), arr, color='blue')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Resultado de RadixSort')
plt.show()

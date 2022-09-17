def selection_sort(massiv):
    for num in range(len(massiv)):
        min_value = num
        for item in range(num, len(massiv)):
            if massiv[min_value] > massiv[item]:
                min_value = item
                print("После очередной итерации:", massiv)
        massiv[num], massiv[min_value] = massiv[min_value], massiv[num]
    return (massiv)# выводится массив на каждой итерации ( нужен только для наглядности)
massiv = [62, 34, 25, 14, 77, 23, 11, 5, 68]
print("Исходный массив", massiv)
resultat = selection_sort(massiv)
print("Результат", resultat)
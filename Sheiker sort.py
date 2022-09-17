array = [22, 13, 444, 5, 7, 3, 2, 74]
left = 0
right = len(array) -1
while left <= right:
    for i in range(left, right, +1): # +1 это шаг ( можно было не писать)
        print(array) # выводится массив на каждой итерации ( нужен только для наглядности)
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    right -= 1
    for i in range(right, left, -1):# -1 это шаг ( начинается с конца )
        if array[i-1] > array[i]:
            array[i], array[i-1] = array[i-1], array[i]
    left += 1
print(array)
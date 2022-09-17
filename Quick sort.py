import random
a = [9, 5, 111, 115, 112, 43, 65, -98, 543, 687, 4, 7, 8, 3, -8]
def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a)-1)]      # случайное пороговое значение (для разделения на малые и большие)
        low = [u for u in a if u < x] # разделение массива
        eq = [u for u in a if u == x]
        hi = [u for u in a if u > x]
        a = quick_sort(low) + eq + quick_sort(hi)# рекурсия
    return a
a = quick_sort(a)
print(a)
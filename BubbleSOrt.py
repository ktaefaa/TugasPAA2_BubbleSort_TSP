def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Melakukan iterasi sebanyak n-1 kali
        for j in range(n - 1 - i):
            # Membandingkan elemen saat ini dengan elemen sebelahnya
            if arr[j] > arr[j + 1]:
                # Jika elemen saat ini lebih besar, tukar posisinya
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Array setelah diurutkan menggunakan Bubble Sort:")
print(sorted_arr)
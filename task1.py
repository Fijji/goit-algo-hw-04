import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [random.randint(0, 1000) for _ in range(10000)]

# Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах.
merge_sort_time = timeit.timeit(stmt='merge_sort(arr.copy())', globals=globals(), number=1)
insertion_sort_time = timeit.timeit(stmt='insertion_sort(arr.copy())', globals=globals(), number=1)
timsort_time = timeit.timeit(stmt='sorted(arr.copy())', globals=globals(), number=1)

print(f"Merge Sort Time: {merge_sort_time}")
print(f"Insertion Sort Time: {insertion_sort_time}")
print(f"Timsort Time: {timsort_time}")

# Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим
winner = min(merge_sort_time, insertion_sort_time, timsort_time)
if winner == merge_sort_time:
    print("Найшвидший: Merge Sort")
elif winner == insertion_sort_time:
    print("Найшвидший: Insertion Sort")
else:
    print("Найшвидший: Timsort")
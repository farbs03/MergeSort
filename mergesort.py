import random
import time

nums = [random.randint(1, 10000) for i in range(10000)]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

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


time1 = time.perf_counter()
mergeSort(nums)
time2 = time.perf_counter()
elapsed = time2 - time1

print('Time elapsed: ', round(elapsed, 8))
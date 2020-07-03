def QuickSort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array if i < pivot]
        greater = [j for j in array if j > pivot]

        Sorted_array = QuickSort(less) + [pivot] + QuickSort(greater)

        return Sorted_array


print(QuickSort([3, 1, 2, 5, 4]))

def selection_sort(array):
    for i in range(0, len(array)):
        smallest_index = i
        for j in range(i, len(array)):
            if array[smallest_index] > array[j]:
                smallest_index = j
        temp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = temp
    return array

print(selection_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
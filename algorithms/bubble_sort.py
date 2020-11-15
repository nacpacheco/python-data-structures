def bubble_sort(array):
    not_sorted = True
    while (not_sorted):
        changes = 0
        for n in range(0, len(array)-1):
            if array[n] <= array[n+1]:
                continue
            else:
                current_number = array[n]
                array[n] = array[n+1]
                array[n+1] = current_number
                changes += 1
                not_sorted = True
        if changes == 0:
            not_sorted = False
        print(array)
    return array

def bubble_sort_course(array):
    lenght = len(array)
    for i in range(0, lenght-1):
        for j in range(0, lenght-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

print(bubble_sort_course([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))

def merge_sort(array):
    if len(array) == 1:
        return array

    middle = len(array)//2
    left = array[:middle]
    right = array[middle:]
    print("left: {}".format(left))
    print("right: {}".format(right))

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    left_i = 0
    right_i = 0
    while(left_i < len(left) and right_i < len(right)):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i +=1
        else:
            result.append(right[right_i])
            right_i += 1
    merged = result + left[left_i:] + right[right_i:]
    print("merged: {}".format(merged))
    return merged

print(merge_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
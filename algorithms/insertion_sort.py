def insertion_sort(arr):
  length = len(arr)
  i = 1
  end = arr[0]
  while i < length:
    if arr[i] < end:
      x = arr.pop(i)
      for j in range(0,i):
        if x < arr[j]:
          arr.insert(j,x)
          break
    end = arr[i]
    i += 1
  return arr




print(insertion_sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]))
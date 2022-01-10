def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2

def heapify(array, n, i):
    largest = i
    l = left(i)
    r = right(i)
    if l < n and array[l] > array[i]:
        largest = l
    if r < n and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapsort(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


def heapifyReverse(array, n, i):
    largest = i
    l = left(i)
    r = right(i)
    if l < n and array[l] < array[i]:
        largest = l
    if r < n and array[r] < array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapsortReverse(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapifyReverse(array, len(array), i)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapifyReverse(array, i, 0)

array = [1,21,2,53,213]
heapsort(array)
print(array)
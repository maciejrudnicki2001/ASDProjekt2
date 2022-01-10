def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2

def heapify(array, n, i):
    smallest = i
    l = left(i)
    r = right(i)
    if l < n and array[l].freq < array[i].freq:
        smallest = l
    if r < n and array[r].freq < array[smallest].freq:
        smallest = r
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, n, smallest)


def heapsort(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, len(array), i)
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

def buildHeap(array):
    for i in range(len(array), -1, -1):
        heapify(array, len(array), i)



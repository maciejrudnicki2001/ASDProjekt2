import heapSortAlgoritm


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq

        self.symbol = symbol

        self.left = left

        self.right = right

        self.huff = ''


def calcFreq(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols

values = dict()

def printNodes(node, val=''):

    newVal = val + str(node.huff)

    if(node.left):
        printNodes(node.left, newVal)
    if(node.right):
        printNodes(node.right, newVal)
    if(not node.left and not node.right):

        values[node.symbol] = newVal

nodes = []

f = open('InputFile.txt', 'r')
text = f.read()
freqAndLetters = calcFreq(text)
for x in freqAndLetters:
    nodes.append(node(freqAndLetters[x], x))
while len(nodes) > 1:
    heapSortAlgoritm.buildHeap(nodes)
    left = nodes.pop(0)

    heapSortAlgoritm.buildHeap(nodes)
    right = nodes.pop(0)

    left.huff = 0
    right.huff = 1

    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    nodes.append(newNode)

dictionary = printNodes(nodes[0])


def writeFileByte(filenamewrite):
    with open("encryptedData", "ab") as f:
        f.write(bitstring_to_bytes(filenamewrite))

def bitstring_to_bytes(s):

    w = [int(s[i:i+8],2) for i in range(0, len(s), 8)]
    return(bytes(w))

def encryptDataWithSaving(data, dictionary):

    symbols = ""
    for element in data:
        symbols = symbols + dictionary[element]

    with open('encryptedData', 'w') as f:
        for x in dictionary:
            f.write(x + ": " + dictionary[x] + "\n")
    writeFileByte(symbols)
    return symbols

text = encryptDataWithSaving(text, values)


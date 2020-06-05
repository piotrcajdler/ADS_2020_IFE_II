


def parent(i):
    return int(i / 2)


def left(i):
    return int(2 * i)


def right(i):
    return int(2 * i + 1)

def heaptify(A, i):
    global heap_size
    heap_size = len(A) - 1
    l = left(i)
    r = right(i)
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        heaptify(A, largest)


def buildheap(A):
    global heap_size
    heap_size = len(A) - 1
    i = int((len(A) - 1) / 2)
    while i > -1:
        heaptify(A, i)
        i -= 1
        if i == 0:
            heaptify(A, i)
            break

# priority queue


def extract_max(A):
    global heap_size
    heap_size = len(A) - 1
    if len(A) < 1:
        print("HEAP UNDERFLOW")
        return 1
    max_val = A[0]
    A[0] = A[heap_size]
    heap_size -= 1
    heaptify(A, 0)
    return max_val

def insert_element(A,arg):
    global heap_size
    heap_size = len(A) - 1
    A += [arg]
    heap_size += 1
    i = heap_size

    while i > 0 and A[parent(i)] < arg:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = arg


def heappop(A):
    if len(A) == 0: return False
    global heap_size
    heap_size = len(A) - 1
    a = A[heap_size]
    del A[heap_size]
    heap_size -= 1
    return a

class huffnode:

    def __init__(self,character,freq):
        self.character = character
        self.freq = freq
        self.right = None
        self.left = None

    def __eq__(self, other):
        if other is None:
            return self.freq == other
        return self.freq == other.freq

    def __ne__(self, other):
        if other is None:
            return self.freq != other
        return self.freq != other.freq

    def __le__(self, other):
        if other is None:
            return self.freq <= other
        return self.freq <= other.freq

    def __lt__(self, other):
        if other is None:
            return self.freq < other
        return self.freq < other.freq

    def __gt__(self, other):
        if other is None:
            return self.freq > other
        return self.freq > other.freq

    def __ge__(self, other):
        if other is None:
            return self.freq >= other
        return self.freq >= other.freq


class huffman_coding:

    def __init__(self):
        self.heap = []
        self.codes = {}

    def freqdict(self, text):
        freq = {}
        for char in text:
            if not char in freq:
                freq[char] = 0
            freq[char] += 1
        return freq

    def build_heap(self,freq):
        for i in freq:
            node = huffnode(i, freq[i])
            insert_element(self.heap, node)

    def merge_heaps(self):
        while len(self.heap) > 1:
            fnode = heappop(self.heap)
            secnode = heappop(self.heap)

            connected = huffnode(None,fnode.freq + secnode.freq)
            connected.left = fnode
            connected.right = secnode

            insert_element(self.heap, connected)

    def add_0_or_1(self,root,code):

        if root is None:
            return

        if root.character is not None:
            self.codes[root.character] = code
            return

        self.add_0_or_1(root.left, code + "0")
        self.add_0_or_1(root.right, code + "1")

    def coding(self):
        root = heappop(self.heap)
        code = ""
        self.add_0_or_1(root, code)

    def code_txt(self,text):
        freq_dict = self.freqdict(text)
        self.build_heap(freq_dict)
        self.merge_heaps()
        self.coding()

        txt = ""
        for c in text:
            txt += self.codes[c]
        return txt





if __name__ ==  "__main__":
    ob1 = huffman_coding()
    text = input("STRING: ")
    print(ob1.code_txt(text))
    print(ob1.codes)
    try:
        print(len(text) * 8 / len(ob1.code_txt(text)))
    except ZeroDivisionError:
        print("Cant divide by 0 ")
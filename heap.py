import math

def swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]

class Min_Heap:
    def __init__(self):
        self.size = 0
        self.array = []

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def parent(self, i):
        return (i-1)//2

    def extract_min(self):
        if self.size != 0:
            lowest = self.array[0]
            self.array[0] = self.array[self.size-1]
            self.size -= 1
            self.min_heapify(0)
            return lowest

    def insert(self, key):
        if self.size >= len(self.array):
            self.array.append(math.inf)
        else:
            self.array[self.size] = math.inf

        self.decrease_key(self.size, key)
        self.size += 1

    def decrease_key(self, pos, key):
        self.array[pos] = key
        dad = self.parent(pos)
        while pos>1 and self.array[dad] > self.array[pos]:
            swap(self.array, pos, dad)
            pos = dad
            dad = self.parent(pos)

    def min_heapify(self, index):
        left = self.left(index)
        right = self.right(index)

        if left < self.size and self.array[left] < self.array[index]:
            lowest = left
        else:
            lowest = index

        if right < self.size and self.array[right] < self.array[lowest]:
            lowest = right

        if lowest != index:
            swap(self.array,index,lowest)
            self.min_heapify(lowest)

    def build_heap(self):
        for i in range(self.size//2, -1, -1):
            self.min_heapify(i)

    def search_key(self, key):
        for i in range(len(self.array)):
            if self.array[i] == key:
                return i
        return None

    def __str__(self):
        out = "["
        for i in range(self.size-1):
            out += str(self.array[i]) + ", "

        out += str(self.array[self.size-1]) + "]" + " size: " + str(self.size)
        return out

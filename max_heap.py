# Heap
# A Binarty Heap is a data structure where a perfect binary tree contains a given node less than or equal to its parent
# IS NOT AN ADT

# Peek: O(1)
# Insert: O(log n)
# Removal: O(log n)

# get parent -> i / 2
# get left -> i * 2
# get right -> (i * 2) + 1


class Heap():
    import operator

    def __init__(self, heap=[], compare=operator.lt):
        self.heap = heap
        if len(heap) < 1:
            self._fill_heap()
        self.compare = compare

    def __repr__(self):
        return 'Heap({!r}, {!r})'.format(self.heap, self.compare)

    # region Private Methods
    def _fill_heap(self):
        from create_array import create_array
        a = create_array()
        self.heap = a

    def _swap(self, child_index, parent_index):
        self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]

    # starts from bottom to root
    def heapify_down(self, child_index):
        while child_index > 0:
            parent_index = child_index // 2
            if self.compare(self.heap[parent_index], self.heap[child_index]):
                return
            self._swap(parent_index, child_index)
            child_index = parent_index

    def heapify_up(self, parent_index):
        while parent_index * 2 < len(self.heap):
            child_index = parent_index * 2
            if child_index + 1 < len(self.heap) and self.compare(self.heap[child_index + 1], self.heap[child_index]):
                child_index += 1
            if self.compare(self.heap[parent_index], self.heap[child_index]):
                return
            self._swap(parent_index, child_index)
            parent_index = child_index


# CALLS
h = Heap()
print(h.heap)

h.heapify_down(len(h.heap) - 1)
print(h.heap)

h.heapify_up(1)
print(h.heap)
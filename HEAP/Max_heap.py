import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

    def peek(self):
        return -self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

# Example usage:
max_heap = MaxHeap()

max_heap.push(4)
max_heap.push(1)
max_heap.push(7)
max_heap.push(3)

print("Max Heap:", [-x for x in max_heap.heap])

print("Pop:", max_heap.pop())
print("Max Heap after pop:", [-x for x in max_heap.heap])

print("Peek:", max_heap.peek())
print("Heap size:", max_heap.size())

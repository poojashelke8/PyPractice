import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

# Example usage:
min_heap = MinHeap()

min_heap.push(4)
min_heap.push(1)
min_heap.push(7)
min_heap.push(3)

print("Min Heap:", min_heap.heap)

print("Pop:", min_heap.pop())
print("Min Heap after pop:", min_heap.heap)

print("Peek:", min_heap.peek())
print("Heap size:", min_heap.size())

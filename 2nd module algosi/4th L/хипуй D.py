class Heap:
    def __init__(self, a):
        self.heap = a

    def insert(self):
        counter = 0
        for k in range(len(self.heap) - 1, -1, -1):
            if k % 2 == 0:
                while k > 0 and (self.heap[(k - 1) // 2] < max(self.heap[k],self.heap[k-1])):
                    self.heap[(k - 1) // 2], self.heap[k] = self.heap[k], self.heap[(k - 1) // 2]
                    k = (k - 1) // 2
                    counter += 1
            else:
                while k > 0 and self.heap[(k - 1) // 2] < max(self.heap[k],self.heap[k+1]):
                    self.heap[(k - 1) // 2], (max(self.heap[k],self.heap[k+1])) = max(self.heap[k],self.heap[k+1]), self.heap[(k - 1) // 2]
                    k = (k - 1) // 2
                    counter += 1
        return counter


n = int(input())
a = list(map(int, input().split()))
h = Heap(a)

print(h.insert())

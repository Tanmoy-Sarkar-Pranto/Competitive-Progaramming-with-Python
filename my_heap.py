import sys

class MyHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.Heap = [0]*(self.maxsize+1)
        self.size = 0
        self.Heap[0] = -1 * self.maxsize
        self.FRONT = 1
    
    def parentIndex(self, index):
        return index//2
    
    def leftChildIndex(self, index):
        return 2*index
    
    def rightChildIndex(self, index):
        return 2*index + 1
    
    def isLeaf(self, index):
        return index*2 > self.size
    
    def swap(self, index1, index2):
        self.Heap[index1], self.Heap[index2] = self.Heap[index2], self.Heap[index1]

    def minHeapify(self, index):

        if not self.isLeaf(index):
            if self.Heap[index] > self.Heap[self.leftChildIndex(index)] or self.Heap[index] > self.Heap[self.rightChildIndex(index)]:
                if self.Heap[self.leftChildIndex(index)] < self.Heap[self.rightChildIndex(index)]:
                    self.swap(index, self.leftChildIndex(index))
                    self.minHeapify(self.leftChildIndex(index))
                else:
                    self.swap(index, self.rightChildIndex(index))
                    self.minHeapify(self.rightChildIndex(index))
    
    def insert(self, data):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = data
        current = self.size

        while self.Heap[current] < self.Heap[self.parentIndex(current)]:
            self.swap(current, self.parentIndex(current))
            current = self.parentIndex(current)
    

    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap using 
    # the minHeapify function 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 
  
# Driver Code 
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = MyHeap(15) 
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.remove())) 
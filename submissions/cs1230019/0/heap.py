'''
Python Code to implement a heap with general comparison function
'''
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.heap = init_array.copy()
        self.comparator = comparison_function
        self.size = len(init_array)
        for i in range (self.size):
            self.down_heap(i)
        pass
        
    def down_heap(self,index):
        # Write your code here
        i = index
       
        while True:
           
            parent = i
            left = 2*i + 1
            right = 2*i + 2
            min = parent
            if(right >= self.size):
                if(left >= self.size):
                    break
                else:
                    min = left
                    if self.comparator(self.heap[min],self.heap[parent]):
                        temp = self.heap[parent]
                        self.heap[parent] = self.heap[min]
                        self.heap[min] = temp
                    break
                break
            
            if self.comparator(self.heap[left],self.heap[min]):
                min = left
            if self.comparator(self.heap[right],self.heap[min]):
                min = right
            if min != parent:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[min]
                self.heap[min] = temp
                i = min
            else:
                break
        
        pass
    
    def up_heap(self,index):
        
        i = index
        
        while True:
            cur = i
            
            if(cur == 0):
                break
            
            parent = (cur-1)//2
            
            if self.comparator(self.heap[cur],self.heap[parent]):
                temp = self.heap[parent]
                self.heap[parent] = self.heap[cur]
                self.heap[cur] = temp
                i = parent
            else:
                return None
        
        pass
    
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.heap.append(value)
        self.size += 1
        self.up_heap(self.size-1)
        # Write your code here
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        ans = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.heap.pop()
        self.down_heap(0)
        
        return ans
        # Write your code here
        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if self.size == 0:
            return None
        else:
            return self.heap[0]
        # Write your code here
        pass
    
    def to_sorted_list(self):
        '''
        Arguments:
            None
        Returns:
            List[Any] : The elements of the heap in a sorted list
        Description:
            Returns the elements of the heap in a sorted list
        Time Complexity:
            O(n log(n)) where n is the number of elements in the heap
        '''
        # Make a deep copy of the heap
        copied_heap = Heap(self.comparator, self.heap[:])
        
        sorted_list = []
        while copied_heap.size > 0:
            sorted_list.append(copied_heap.extract())
        
        return sorted_list
    # You can add more functions if you want to
    
    
    
# # Test case to check the Heap implementation
# def test_heap():
#     # Comparison function for min-heap
#     min_comparator = lambda x, y: x < y
#     # Initialize the heap with some elements
#     min_heap = Heap(min_comparator, [1,2,5,10,20,30,40])

#     print("Min-Heap after initialization:", min_heap.heap)  # Should be organized as a min-heap

#     # Insert a new element
#     min_heap.insert(11)
#     print("Min-Heap after inserting 11:", min_heap.heap)  # Should maintain heap property
#     # Extract the top element
#     extracted_min = min_heap.extract()
#     print("Extracted min:", extracted_min)  # Should be the smallest element (0)
#     print("Min-Heap after extraction:", min_heap.heap)  # Should maintain heap property

#     # Get the top element
#     top_min = min_heap.top()
#     print("Current top element:", top_min)  # Should be the next smallest element

#     # Test max-heap
#     max_comparator = lambda x, y: x > y
#     max_heap = Heap(max_comparator, [3, 5, 1, 10, 2])

#     print("\nMax-Heap after initialization:", max_heap.heap)  # Should be organized as a max-heap

#     # Insert a new element
#     max_heap.insert(15)
#     print("Max-Heap after inserting 15:", max_heap.heap)  # Should maintain heap property

#     # Extract the top element
#     extracted_max = max_heap.extract()
#     print("Extracted max:", extracted_max)  # Should be the largest element (15)
#     print("Max-Heap after extraction:", max_heap.heap)  # Should maintain heap property

#     # Get the top element
#     top_max = max_heap.top()
#     print("Current top element:", top_max)  # Should be the next largest element

# # Run the test case
# test_heap()

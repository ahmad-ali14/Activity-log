# Python3 program for building Heap from Array 
  
# To heapify a subtree rooted with node i  
# which is an index in arr[]. N is size of heap 
def heapify(swaps, arr, n, i): 
    
    largest = i; # Initialize largest as root 
    l = 2 * i + 1; # left = 2*i + 1 
    r = 2 * i + 2; # right = 2*i + 2 
  
    # If left child is larger than root 
    if (l < n and arr[l] < arr[largest]): 
        largest = l; 
  
    # If right child is larger than largest so far 
    if (r < n and arr[r] < arr[largest]): 
        largest = r; 
  
    # If largest is not root 
    if (largest != i): 
        swap = arr[i]; 
        swaps.append((i,largest))
        arr[i] = arr[largest]; 
        arr[largest] = swap; 
  
        # Recursively heapify the affected sub-tree 
        heapify(swaps, arr, n, largest); 

# Function to build a Max-Heap from the given array 
def buildHeap(arr, n): 
    swaps = []
    # Index of last non-leaf node 
    startIdx = int((n / 2)) - 1; 
  
    # Perform reverse level order traversal 
    # from last non-leaf node and heapify 
    # each node 
    for i in range(startIdx, -1, -1): 
        heapify(swaps , arr, n, i); 
  
    return swaps


# A utility function to print the array 
# representation of Heap 
def printHeap(arr, n): 
    print("Array representation of Heap is:"); 
    print('swaps')
    for i in range(n): 
        print(arr[i], end = " "); 
    print(); 
  
# Driver Code 
if __name__ == '__main__': 
      
   # arr = [ 1, 3, 5, 4, 6, 13,  10, 9, 8, 15, 17 ];
    arr = [5,4,3,2,1] 
  
    n = len(arr); 
  
    r = buildHeap(arr, n);

    print('r', r) 
  
    printHeap(arr, n); 
      
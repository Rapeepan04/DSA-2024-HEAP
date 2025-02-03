import heapq

def insert_to_max_heap(heap, values):
    for value in values:
        heapq.heappush(heap, -value) 

def print_max_heap(heap):
    print("Max Heap:", [-x for x in heap])

def remove_max(heap):
    if heap:
        return -heapq.heappop(heap)  
    return None

def is_max_heap(arr):
    n = len(arr)
    for i in range(n // 2):  
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True

values = [5, 3, 8, 1, 2, 7, 6, 4]

max_heap = []
insert_to_max_heap(max_heap, values)

print_max_heap(max_heap)

for i in range(3):
    removed_value = remove_max(max_heap)
    print(f"Removed: {removed_value}")
    print_max_heap(max_heap)

arr = [8, 6, 7, 4, 2, 5, 3, 1]
print(f"Is max heap: {is_max_heap(arr)}")

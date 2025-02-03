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

values = [5, 3, 8, 1, 2, 7, 6, 4]

max_heap = []
insert_to_max_heap(max_heap, values)

print_max_heap(max_heap)

for i in range(3):
    removed_value = remove_max(max_heap)
    print(f"Removed: {removed_value}")
    print_max_heap(max_heap)
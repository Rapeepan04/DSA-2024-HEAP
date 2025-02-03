import heapq

def insert_to_max_heap(heap, values):
    for value in values:
        heapq.heappush(heap, -value)  # ใช้ค่าลบเพื่อให้ heapq ทำงานเป็น Max Heap

def print_max_heap(heap):
    print("Max Heap:", [-x for x in heap])

# ค่าที่ต้องการเพิ่มลงใน Max Heap
values = [5, 3, 8, 1, 2, 7, 6, 4]

# สร้าง Max Heap
max_heap = []
insert_to_max_heap(max_heap, values)

# แสดงค่า Max Heap ที่ได้
print_max_heap(max_heap)
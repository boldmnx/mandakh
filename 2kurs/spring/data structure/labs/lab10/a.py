# class BinaryHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, i):
#         return (i - 1) // 2

#     def left_child(self, i):
#         return 2 * i + 1

#     def right_child(self, i):
#         return 2 * i + 2

#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def insert(self, priority, task):
#         self.heap.append((priority, task))
#         self.heapify_up(len(self.heap) - 1)

#     def heapify_up(self, i):
#         while i != 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
#             self.swap(i, self.parent(i))
#             i = self.parent(i)

#     def extract_min(self):
#         if len(self.heap) == 0:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()

#         min_task = self.heap[0]
#         self.heap[0] = self.heap.pop()
#         self.heapify_down(0)
#         return min_task

#     def heapify_down(self, i):
#         left = self.left_child(i)
#         right = self.right_child(i)
#         smallest = i

#         if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
#             smallest = right

#         if smallest != i:
#             self.swap(i, smallest)
#             self.heapify_down(smallest)

# # Example usage:
# if __name__ == "__main__":
#     tasks = BinaryHeap()

#     # Insert tasks with priorities
#     tasks.insert(2, "Task 1")
#     tasks.insert(1, "Task 2")
#     tasks.insert(3, "Task 3")
#     tasks.insert(4, "Task 4")
#     tasks.insert(2, "Task 5")

#     # Extract tasks in priority order
#     print(tasks.extract_min())  # Output: (1, 'Task 2')
#     print(tasks.extract_min())  # Output: (2, 'Task 1')
#     print(tasks.extract_min())  # Output: (2, 'Task 5')
#     print(tasks.extract_min())  # Output: (3, 'Task 3')
#     print(tasks.extract_min())  # Output: (4, 'Task 4')
#     print(tasks.extract_min())  # Output: None (Queue is empty)

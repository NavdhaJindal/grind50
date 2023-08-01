class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else: 
            if val > self.minStack[-1]:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.heap = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         heapq.heappush(self.heap, val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.heap = [i for i in self.stack]
#         heapq.heapify(self.heap)

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         min_element = heapq.heappop(self.heap)
#         heapq.heappush(self.heap, min_element)
#         return min_element
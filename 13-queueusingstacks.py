class MyQueue:

    def __init__(self):
        self.original_stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        self.original_stack.append(x)
        
    def pop(self) -> int:
        self.peek()   
        return self.reverse_stack.pop()

    def peek(self) -> int:   
        if not self.reverse_stack:
            while self.original_stack:
                self.reverse_stack.append(self.original_stack.pop())
        return self.reverse_stack[-1]

    def empty(self) -> bool:
        return (not self.original_stack and not self.reverse_stack)

# class MyQueue:

#     def __init__(self):
#         self.original_stack = []
#         self.reverse_stack = []

#     def push(self, x: int) -> None:
#         self.original_stack.append(x)
#         self.reverse_stack = []
#         for el in reversed(self.original_stack):
#             self.reverse_stack.append(el)
        

#     def pop(self) -> int:
#         popped_element = self.reverse_stack.pop()
#         self.original_stack = []
#         for el in reversed(self.reverse_stack):
#             self.original_stack.append(el)
#         return popped_element
        

#     def peek(self) -> int:
#         return self.original_stack[0]

#     def empty(self) -> bool:
#         if len(self.original_stack) == 0:
#             return True
#         else:
#             return False
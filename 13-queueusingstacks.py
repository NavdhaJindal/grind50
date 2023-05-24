class MyQueue:

    def __init__(self):
        self.original_stack = []
        self.reverse_stack = []

    def push(self, x: int) -> None:
        self.original_stack.append(x)
        self.reverse_stack = []
        for el in reversed(self.original_stack):
            self.reverse_stack.append(el)
        

    def pop(self) -> int:
        popped_element = self.reverse_stack.pop()
        self.original_stack = []
        for el in reversed(self.reverse_stack):
            self.original_stack.append(el)
        return popped_element
        

    def peek(self) -> int:
        return self.original_stack[0]

    def empty(self) -> bool:
        if len(self.original_stack) == 0:
            return True
        else:
            return False
class Stack:
    def __init__(self, supply_stack: list):
        self.stack = supply_stack

    def check_if_empty(self):
        return len(self.stack) == 0

    def check_stack(self):
        return self.stack

    def push(self, item):
        self.stack.append(item)

        # optional printing of added element
        # print(f'{item} was added')

    def pop(self):
        if self.check_if_empty():
            print('Stack is empty')
            return None
        popped = self.stack.pop()

        # optional printing of removed element
        # print(f'{popped} was removed')

        return popped

    def peek(self):
        return self.stack[-1]

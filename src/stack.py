class Stack:

    def __init__(self, stack=[]):
        self.stack = stack

    def push_value(self, new_value):
        self.stack.append(new_value)

    def empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def pop_value(self):
        if not self.empty():
            return self.stack.pop(-1)
        return 'The stack is empty. NO TOP'

    def show_top(self):
        if not self.empty():
            return self.stack[-1]


if __name__ == "__main__":
    stack = Stack()
    # for i in range(1, 11):
    #     stack.push_value(i)
    # print(f"Stack: {stack.stack}")
    # for j in range(1, 5):
    #     remove = stack.pop_value()
    #     if remove:
    #         print(f"Pop: {remove}")
    #     else:
    #         print('There is nothing in the stack')
    # print(f"Stack: {stack.stack}")
    # stack.show_top()


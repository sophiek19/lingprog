from stack import Stack


def check(seq):
    stack = Stack()
    stack.push_value(seq[0])
    for i in seq[1:]:
        top = stack.show_top()
        if i == ')' and top == '(':
            stack.pop_value()
        elif i == '}' and top == '{':
            stack.pop_value()
        elif i == ']' and top == '[':
            stack.pop_value()
        else:
            stack.push_value(i)
    return stack.empty()

def sort_stack(stack):
    tmp = Stack()
    tmp.stack.clear()
    sort = sorted(stack.stack)
    for el in sort:
        tmp.push_value(el)
    return tmp.stack

def sort(stack):
    tmp = Stack()
    tmp.stack.clear()
    while not stack.empty():
        el = stack.pop_value()
        while tmp.stack and tmp.stack[-1] > el:
            stack.push_value(tmp.pop_value())
        tmp.push_value(el)
    return tmp.stack

print(sort(Stack([1, 4, 3, 8])))
print(sort(Stack([5, 7, 2])))
print(sort(Stack([2, 5, 7])))
print(sort(Stack([7, 5, 2])))
print(sort(Stack([1, 5, 6, 2, 8])))

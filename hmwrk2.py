class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_text(text):
    stack = Stack()
    for ch in text:
        stack.push(ch)

    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()

    stack = Stack()
    for ch in cleaned:
        stack.push(ch)

    for ch in cleaned:
        if ch != stack.pop():
            return False
    return True



print(reverse_text("Python"))
print(reverse_text("გამარჯობა"))
print(is_palindrome("ანა ანა"))
print(is_palindrome("Level"))
print(is_palindrome("Hello"))
# Neetcode
# Last Updated: 08-03-2025 - 08:53 PM
# Difficulty: Medium
# Status: Solved
# Tags: Stack, Design
# Time Complexity: O(1)
# Space Complexity: O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# My Solution
# Last Updated: 08-03-2025 - 08:53 PM
# Difficulty: Medium
# Status: Solved
# Tags: Stack, Design
# Time Complexity: O(1)
# Space Complexity: O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if top == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None


# One Stack
# Last Updated: 08-03-2025 - 08:53 PM
# Difficulty: Medium
# Status: Solved
# Tags: Stack, Design
# Time Complexity: O(1)
# Space Complexity: O(n)

class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

# 스택 사용
# 연결 리스트 사용하여 풀이

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        return node.data
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None

def solution(s):
    answer = -1
    
    stack = Stack()
    
    for i in s:
        if stack.peek() == i:
            stack.pop()
        else:
            stack.push(i)
            
    if stack.is_empty():
        answer = 1
    else:
        answer = 0
        
    return answer


# 간단한 코드
def solution(s: str) -> int:
    stack = []
    for ch in s:
        if stack and (ch == stack[-1]):
            stack.pop()
        else:
            stack.append(ch)
    return 0 if stack else 1
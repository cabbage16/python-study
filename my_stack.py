class ArrayStack:
    def __init__(self, capacity = 10) -> None:
        self.capacity = capacity
        self.list = [None]*capacity
        self.top = -1

    def isEmpty(self) -> bool:
        return self.top == -1
    
    def isFull(self) -> bool:
        return self.top == self.capacity-1
    
    def push(self, item) -> None:
        if self.isFull():
            print("Error: Stack is full")
            return
        
        self.top += 1
        self.list[self.top] = item
    
    def pop(self) -> int:
        if self.isEmpty():
            print("Error: Stack is empty")
            return
        
        temp = self.list[self.top]
        self.list[self.top] = None
        self.top -= 1
        return temp
    
    def peek(self) -> int:
        if self.isEmpty():
            print("Error: Stack is empty")
            return
        
        return self.list[self.top]
        
    def delete_all(self) -> None:
        while not self.isEmpty():
            self.pop()
    
    def reverse(self) -> None:
        self.list[:self.top+1] = self.list[self.top::-1]
    
    def __str__(self) -> str:
        result = ""
        
        for i in reversed(range(self.capacity)):
            result += "| {0} |".format(self.list[i])
            result += " <- top\n" if i == self.top else "\n"

        return result

def init():
    print('-' * 30)
    print("""push: 삽입
pop: 삭제 후 반환
peek: 반환
clear: 스택 초기화
reverse: 스택 역순으로 배열
print: 스택 출력
exit: 시스템 종료
------------------------------""")

stack = ArrayStack(3)

init()
print(">>> ", end="")

while True:
    c = input()
    
    if c == 'push':
        stack.push(int(input("정수를 입력해주세요: ")))
        init()
    
    elif c == 'pop':
        print(stack.pop())
    
    elif c == "peek":
        print(stack.peek())
    
    elif c == "clear":
        stack.delete_all()
        init()
    
    elif c == "reverse":
        stack.reverse()
        init()
    
    elif c == 'print':
        print(stack)
    
    elif c == 'exit':
        break

    else:
        print("Error: Invalid input")
    print(">>> ", end="")
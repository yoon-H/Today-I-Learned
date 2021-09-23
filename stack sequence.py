import sys
class Stack:
    # make stack
    def __init__ (self):
        self.top = []
    
    # print stack size
    def __len__(self):
        return len(self.top)

    # swap data type to str in stack and print
    def __str__(self):
        return str(self.top[::1])
    
    # clear stack
    def clear(self):
        self.top=[]

    # PUSH
    def push (self, item):
        self.top.append(item)

    # POP
    def pop(self):
        # if Stack is not empty
        return self.top.pop(-1)
    
    # return if stack has element
    def isContain(self, item):
        return item in self.top
    
    # read the value of top in stack
    def peek(self):
        if not self.isEmpty(self):
            return self.top[-1]
        else:
            return 0
            exit()

    # check stack is empty
    def isEmpty(self):
        return len(self.top)==0
    

    

n= int(input())
seq=[0]*n
for i in range(n) :
    seq[i]=int(sys.stdin.readline())
    
com=[0]*n
for i in range(n) :
    com[i] = i+1

result = []

stack = Stack
stack.__init__(stack)

index=0
for i in seq :
    if (i !=stack.peek(stack)) & (i != com[i-1]) :
        print('NO')
        break
    else :
        while(1) :
            if i == stack.peek(stack) :
                stack.pop(stack)
                result.append('-')
                break
            elif i == com[i-1] :
                stack.push(stack,com[index])
                com[index] = 0
                index+=1
                result.append('+')
                continue
           

if len(result) == n*2:
    s = ""  
    for i in result:
        s += (str(i) + '\n')
    print(s)
                

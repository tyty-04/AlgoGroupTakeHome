class IntStack:
    #Creates the stack with nothing on top
    def __init__(self):
        self.top = None
    
    #Creates a new element and puts it on top of the stack
    def push(self, value):
        ele = Element(value, self.top)
        self.top = ele
        
    #Returns the value of the top of the stack and sets the top as the next element
    def pop(self):
        if self.top == None:
            raise ValueError("Top is None, no elements in stack")
        val = self.top.value
        self.top = self.top.next
        return val
    
    #Returns the value of the top of the stack
    def peek(self):
        if self.top == None:
            raise ValueError("Top is None, no elements in stack")
        return self.top.value
    
    #Returns the size of the stack
    def size(self):
        size = 0
        cur = self.top
        while(cur != None):
            size += 1
            cur = cur.next
            
        return size
            
             
#Element class functions a linked list for the stack
#Stores the value and the next element
class Element: 
    def __init__(self, value, next):
        self.value = value
        self.next = next
  
#Main function for testing
def main():
    stack = IntStack()
    stack.push(10)
    print("Pushed 10")
    stack.push(5)
    print("Pushed 5")
    stack.push(0)
    print("Pushed 0")
    print("Size: ", stack.size()) #3
    print("Peek: ", stack.peek()) #0
    num = stack.pop() #num = 0
    print("Popped and assigned to var num")
    print("Pop: ", stack.pop()) #5
    print("num: ", num) #0
    print("Peek: ", stack.peek()) #10
    print("Size: ", stack.size()) #1
    num = stack.pop() #num = 10
    print("Popped and assigned to var num")
    print("Size: ", stack.size()) #0
    print("Testing pop with nothing in stack: ")
    try:
        num = stack.pop() #Raise a ValueError
    except ValueError as e:
        print(e)

    
if __name__ == "__main__":
    main()
    
#Not being able to use any actual containers I went with a linked list
#as it is easy to track everything while adding and removing from them
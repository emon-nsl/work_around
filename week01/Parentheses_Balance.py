class Stack:
    def __init__(self, max_size): #initialize a stack of max_size
        self.top_pointer = -1 #Keep track of top element using this
        self.stack = [None for x in range(max_size)]  #create a list of max_size
    
    def push(self, new_element):
        self.top_pointer = self.top_pointer + 1 #Move the pointer
        self.stack[self.top_pointer] = new_element #Add the new_element to the top
    
    def pop(self):
        last_element = self.stack[self.top_pointer]
        self.top_pointer = self.top_pointer - 1 #Move the pointer
        return last_element #Pop the last element
    
    def peek(self):
        return self.stack[self.top_pointer]

    def is_empty(self):
        return self.top_pointer == -1

def checkBalance(s):
	mystack=Stack(len(s))
	if s=="":
		return True
	for c in s:
		if c=="(" or c=="{": 
			mystack.push(c) #push the opening bracket
		else:
			if mystack.is_empty(): 
				return False
			if c=="{" and mystack.peek()!="}": #the brackets dont match
				return False
			if c=="(" and mystack.peek()!=")": #the brackets dont matchs
				return False
			mystack.pop() #pop matching brackets
	if mystack.is_empty(): #stack must be empty at the end
		return True
	return False

t = int(input())
for i in range(t):
    cp = input()
    if checkBalance(cp):
        print('Yes')
    else:
        print('No')
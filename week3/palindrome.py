class stack:

    def __init__(self):
        self.items = []

    # push(e) – Adds the element ‘e’ to the top of the stack
    def push(self, e):
        self.items.append(e)

    # pop() – Deletes the top most element of the stack and return its
    def pop(self):
        return self.items.pop()

    # isEmpty() – Returns whether the stack is empty
    def isEmpty(self):
        return self.items == []

    # peek() – Returns a reference to the top most element of the stack value. Does not remove the element.
    def peek(self):
        return self.items[len(self.items) -1]

class queue:
    def __init__(self):
        self.items = []

    # enqueue(e) - Adds the element 'e' to the queue. 
    def enqueue(self, e):
        self.items.insert(0, e)
    
    # dequeue() - Removes an item from the queue and return it.
    def dequeue(self):
        return self.items.pop()

    # size() - Returns the size of the queue
    def size(self):
        return len(self.items)

    # isEmpty() - Returns whether the queue is empty
    def isEmpty(self):
        return self.items == []

    # peek() - Returns a reference to the front item in the queue. Does not remove the element.
    def peek(self):
        return self.items[len(self.tiems)-1]

# accepts a string as a parameter and returns either True or False if the string is a Palindrome
# This function must use both the Stack and Queue class
def isPalindrome(myString):
    myStack = stack()
    myQueue = queue()
    stringReverse = ''

    for char in myString:
        myStack.push(char)

    while not myStack.isEmpty():
        myQueue.enqueue(myStack.pop())

    while not myQueue.isEmpty():
        stringReverse += myQueue.dequeue()

    if(myString == stringReverse):
        return True

    return False

print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))


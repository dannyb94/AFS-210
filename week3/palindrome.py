class stack:

    def __init__(self):
        self.items = []

    # push(e) – Adds the element ‘e’ to the top of the stack
    def push(self, e):
        self.items.append(e)


    # def push(self, data):
    #     node = Node(data) 
    #     if self.top: 
    #         node.next = self.top 
    #         self.top = node                 
    #     else: 
    #         self.top = node 
    #         self.size += 1 

    # pop() – Deletes the top most element of the stack and return its
    def pop(self):
        return self.items.pop()
    # def pop(e):
    #     if e.delElmt:
    #         data = e.delElmt.data 
    #         # size() – Returns the size of the stack
    #         self -= 1   
    # isEmpty() – Returns whether the stack is empty
    def isEmpty(self):
        return self.items == []
    # peek() – Returns a reference to the top most element of the stack value. Does not remove the element.
    def peek(self):
        return self.items[len(self.items) -1]

class queue:
    # enqueue(e) - Adds the element 'e' to the queue. 
    # dequeue() - Removes an item from the queue and return it.
    # size() - Returns the size of the queue
    # isEmpty() - Returns whether the queue is empty
    # peek() - Returns a reference to the front item in the queue. Does not remove the element.

isPalindrome()
# accepts a string as a parameter and returns either True or False if the string is a Palindrome
# This function must use both the Stack and Queue class
class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        fstNode = Node(data)
        self.head = fstNode
        self.count += 1
        if self.count == 1:
            self.tail = self.head


    def addLast(self, data) -> None:
        # Add a node at the end of the list
        lstNode = Node(data)
        lstNode.prev = self.tail
        self.tail.next = lstNode
        self.tail = lstNode
        self.count += 1
  

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        indxNode = Node(data)
        
        if(index > self.count):
            return
        if(index == self.count):
            self.addLast(indxNode)
        else:
            crnt = self.head
            for i in range(1, index):
                if(crnt != None):
                    crnt = crnt.next
            if(crnt != None):
                indxNode.next = crnt.next
                crnt.next = indxNode

        self.count += 1

        # if(index == 0):
        #     self.addFirst(indxNode)
        # elif(index == self.count):
        #     self.addLast(indxNode)
        # # If index is greater than the length, the data will not be inserted.    
        # elif(index > self.count):
        #     print("Error with input.")
        # # This function does not replace the data at the index, but pushes everything else down.
        # else:
        #     crnt = self.head
        #     for _ in range(index):
        #         crnt = crnt.next
        #     if(crnt == index-1):
        #         indxNode.next = crnt.next
        #         indxNode.prev = crnt
        #         crnt.next = indxNode
        #         crnt.next.prev = indxNode
        #         self.count += 1  


    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        searching = self.head
        dataFound = 0
        #i = 0

        while(searching != None):
            if(searching.data == data):
                return dataFound

            dataFound += 1
            searching = searching.next

        return -1

        # if(searching != None):
        #     while(searching != None):
        #         i += 1
        #         if(searching.data == data):
        #             dataFound += 1
        #             break
        #         searching.next
        #     if(dataFound == 1):
        #         print(i)
        #     else:
        #         print(-1)
        # else:
        #     print("NULL")


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr


words = DoublyLinkedList()
words.addFirst("May")
words.add("the")
words.add("Force")
words.add("be")
words.add("with")
words.add("you")
words.addLast("!")
print(words)

print(words.indexOf("with"))

words.delete("you")
words.addAtIndex("us", 5)
words.addAtIndex("all", 6)
print(words)

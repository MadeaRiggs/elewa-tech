#######CREARING LINKED LISTS FOR INTEGERS
#Node of a Singly Linked List
class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next = None
    #method for setting the data field of the node
    def setData(self,data):
        self.data = data
    #method for getting the data field of the node
    def getData(self):
        return self.data
    #method for setting the next field of the node
    def setNext(self, next):
        self.next = next
    #method for getting the next field of the node
    def getNext(self):
        return self.next
    #returns true if the node points to another node
    def hasNext(self):
        return self.next != None
    
    #checking the list length to help with deleting data items
    def listLength(self):
        current= self.head
        count= 0
        #algorithm 1: looping structure
        while current != None:
            count = count + 1
            current= current.getNext()
        return count

    #method for inserting a new node at the beginning of the Linked List (at the head)
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)

        #algorithm 2: Selection structure
        if self.length == 0:
            self.head= newNode
        else:
            newNode.setNext(self. head)
            self. head = newNode
        self.length += 1

    #method for inserting a new node at the end of a Linked List
    def insertAtEnd(self,data):
        newNode= Node()
        newNode.setData(data)
        current= self.head

    #algorithm 3: Looping structure
        while current.getNext() != None:
            current = current.getNext()
            current.setNext(newNode)
            self.length += 1

    #Method for inserting a new node a t a ny position in a Linked List
    def insertAtPos(self,pos,data):

        #algorithm 4: Selection structure
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos ==self.length :
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode. setData(data)
                    count= 0
                    current= self.head

                    #algorthim 6: loop which will add the nodes
                    while count< pos-1:
                        count += 1
                        current = current.getNext()
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1


    #method to delete the first node of the linked list
    def deleteFromBeginning(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    #Method to delete the last node of the linked list
    def deleteLastNodefromSinglyLinkedList(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
        while currentnode.getNext() != None:
            previousnode = currentnode
            currentnode = currentnode.getNext()
            
        previousnode.setNext(None)
        self.length -= 1

    ##Delete with node from immediate linked list
    def deleteFromLinkedListWithNode(self, node):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current= self.head
            previous = None
            found = False
        while not found:
            if current == node:
                found = True
            elif current is None:
                raise ValueError("Node not in Linked List")
            else:
                previous = current
                current= current.getNext()

        if previous is None:
            self.head= current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

    #Delete with data from linked list
    def deleteValue(self, value):
        currentnode= self.head
        previousnode= self.head
        while currentnode.next != None or currentnode.value != value:
            if currentnode.value == value:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode = currentnode
                currentnode= currentnode.next
        print("The value provided is not present")

    #Method to delete a node at a particular position
    def deleteAtPosition(self,pos):
        count = 0
        currentnode =self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position") 
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count== pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next 
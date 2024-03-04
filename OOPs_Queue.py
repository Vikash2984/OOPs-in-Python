class Node:
    def __init__(self, info):
        self.__data = info
        self.__next = None
    def get_data(self):       # getter method
        return self.__data
    def set_data(self, info): # setter method
        self.__data = info
    def get_next(self):       # getter method
        return self.__next
    def set_next(self, next_node): # setter method
        self.__next = next_node
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
    def get_head(self):
        return self.__head
    def set_head(self, node):
        self.__head = node
    def get_tail(self):
        return self.__tail
    def set_tail(self, node):
        self.__tail = node

    def enqueue(self, info):
        # if the queue does not pre-exist then create a queue
        # otherwise append an element at the end of the queue
        new_node = Node(info)
        if (self.get_head() is None):
            new_node.set_next(None)
            self.set_head(new_node)
            self.set_tail(new_node)
            print ("Creating a Queue...")
        else:
            self.get_tail().set_next(new_node)
            self.set_tail(new_node)
        ptr = self.get_head()
        print ("\nDisplaying current content in the Queue...")
        while (ptr is not None):
            print (ptr.get_data(), end = " ")
            ptr = ptr.get_next()

    def dequeue(self):
        ptr = self.get_head()
        if (ptr == None):
            print ("U N D E R F L O W !!!")
        else:
            self.set_head(ptr.get_next())
            print (f"\nDeleting the most Prior element i.e. {ptr.get_data()}")
            del(ptr)
            
    def queue_display(self):
        ptr = self.get_head()
        print ("\nDisplaying current content in the Queue...")
        while (ptr is not None):
            print (ptr.get_data(), end = " ")
            ptr = ptr.get_next()

#Main function
queue = LinkedList()
while(True):
    op = int(input("\n\n1 -> INSERT\n2 -> DELETE\n3 -> DISPLAY\n0 -> EXIT\nChose an operation to perform : "))
    if(op == 1):
        val = int(input("Enter a number to Insert : "))
        queue.enqueue(val)
    elif(op == 2):
        queue.dequeue()
    elif(op == 3):
        queue.queue_display()
    elif(op == 0):
        break
    else :
        print("\nPlease input a valid option...")
# Implementing Stack using a Linkedlist class 
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
        
    def push(self, info):
        # if the stack does not pre-exist then create a stack
        # otherwise insert an element on top of the stack
        new_node = Node(info)
        if (self.get_head() is None):
            new_node.set_next(None)
            self.set_head(new_node)
            self.set_tail(new_node)
            print ("Initializing Stack...")
        else:
            self.get_tail().set_next(new_node)
            self.set_tail(new_node)
        ptr = self.get_head()
        print ("Displaying the current content in stack...")
        while (ptr is not None):
            print (ptr.get_data(), end = "\n")
            ptr = ptr.get_next()
    def peek(self):
        ptr = self.get_tail()
        print(f"{ptr.get_data()} is on top of the stack")


#Yet to be defined :-
#_____________________________________________________________________________________________________________________________________________#
    def pop(self):
        ptr = self.get_tail()
        if (self.get_head() == None):
            print ("U N D E R F L O W !!!")
        else:
            #set element prior to ptr as tail
            print (f"\nPoped element : {ptr.get_data()}")
            del(ptr)
#_____________________________________________________________________________________________________________________________________________#

    
# Defining class object stack under LinkedList class
#Looping through main menu for data processing
stack = LinkedList()
while(True):
    op = int(input("\n1 -> PUSH\n2 -> POP\n3 -> PEEK\n0 -> EXIT\nChose an operation to perform : "))
    if(op == 1):
        val = int(input("Enter a number to push : "))
        stack.push(val)
    elif(op == 3):
        stack.peek()
    elif(op == 0):
        break
    
    elif(op == 2):
        stack.pop()
        # print(link_list)

    else :
        print("\nPlease input a valid option...")

# Creating a Linkedlist as a Python class object 
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
    def ll_append(self, info):
        # if the linked list does not pre-exist then create the linked list
        # otherwise append a new node at the end of the linked list
        new_node = Node(info)
        if (self.get_head() is None):
            new_node.set_next(None)
            self.set_head(new_node)
            self.set_tail(new_node)
            print ("Creating a linked list with a new node...")
        else:
            self.get_tail().set_next(new_node)
            self.set_tail(new_node)
            # print ("Appending the new node at the end of the linked list...")
    def ll_display(self):
        ptr = self.get_head()
        if (ptr == None):
            print ("Linked list is not pre-existing...")
        else:
            print ("Displaying the current content of the linked list...")
            while (ptr is not None):
                # print (f"Info = {ptr.get_data()} and link = {ptr.get_next()}...")
                print (ptr.get_data(), end = ", ")
                ptr = ptr.get_next()
        print ("\nEnd of the display operation...")
    def __str__(self):
        ptr = self.get_head()
        all_info = []
        while (ptr is not None):
            all_info.append(str(ptr.get_data()))
            ptr = ptr.get_next()
        message = ", ".join(all_info)
        return "Linked list from Head to Tail: " + message
    def ll_insert(self, data_new, data_before):
        ptr = self.get_head()
        while (ptr is not None):
            if (ptr.get_data() == data_before):
                break
            ptr = ptr.get_next()
        if (ptr is None):
            print (f"Unsuccessful searching for info {data_before}...")
        else:
            new_node = Node(data_new)
            new_node.set_next(ptr.get_next())  # new_node->next = ptr->next
            ptr.set_next(new_node)   # ptr->next = new_node
            if (ptr == self.get_tail()):   # if (ptr == tail):
                self.set_tail(new_node)   # tail = new_node
    def ll_delete(self, data_old):
        ptr = self.get_head()
        if (ptr == None):
            print ("U N D E R F L O W !!!")
            return
        if (ptr.get_data() == data_old):
            self.set_head(ptr.get_next())
            del(ptr)
            print ("Deleting the Header Node...")
            return
        ptr_next = ptr.get_next()
        while (ptr_next != None and ptr_next.get_data() != data_old):
            ptr = ptr.get_next()  # ptr = ptr_next
            ptr_next = ptr_next.get_next() # ptr_next->next
        if (ptr_next != None and ptr_next.get_data() == data_old):
            ptr.set_next(ptr_next.get_next())
            del ptr_next
            print ("Successful Deletion...")
        else:
            print ("Unsuccessful Deletion...")



    def ll_search(self,data_search):
        ptr = self.get_head()
        while(ptr != None):
            if (ptr.get_data()==data_search):
                break
        if (ptr == None):
            print ("Unsuccessful")
        else:
            print(f"{data_search} was found")
    
    def ll_reverse(self):
        curr = self.get_head()
        if (curr is None):
            print ("Linked list does not pre-exist...")
            return
        else:
            prev = None
            self.set_tail(curr)
            while (curr is not None):
                curr_next = curr.get_next()
                curr.set_next(prev)
                prev = curr
                curr = curr_next
            self.set_head(prev)
    def ll_split_list(self):
        linked_list_even = LinkedList()
        linked_list_odd = LinkedList()
        ptr = self.get_head()
        while (ptr != None):
            if (ptr.get_data() % 2 == 0):
                linked_list_even.ll_append(ptr.get_data())
            else:
                linked_list_odd.ll_append(ptr.get_data())
            ptr = ptr.get_next()
        return linked_list_even, linked_list_odd
    
    def ll_merge_two_sorted_lists(self, lnk_list1, lnk_list2):
        curr1 = lnk_list1.get_head()
        curr2 = lnk_list2.get_head()
        if (curr1 == None and curr2 == None):
            print ("Both linked lists are empty...")
            return lnk_list1
        if (curr1 == None):
            return lnk_list2
        if (curr2 == None):
            return lnk_list1
        main_list = LinkedList()
        while (curr1 != None and curr2 != None):
            if (curr1.get_data() == curr2.get_data()):
                main_list.ll_append(curr1.get_data())
                main_list.ll_append(curr2.get_data())
                curr1 = curr1.get_next()
                curr2 = curr2.get_next()
            elif (curr1.get_data() < curr2.get_data()):
                main_list.ll_append(curr1.get_data())
                curr1 = curr1.get_next()
            else:
                main_list.ll_append(curr2.get_data())
                curr2 = curr2.get_next()
        while (curr2 != None):
            main_list.ll_append(curr2.get_data())
            curr2 = curr2.get_next()
        while (curr1 != None):
            main_list.ll_append(curr1.get_data())
            curr1 = curr1.get_next()
        return main_list
    
    def ll_aggregation(self):
        ptr = self.get_head()
        if (ptr == None):
            print ("Linked list is not pre-existing...")
        else:
            print ("Displaying the current content of the linked list...")
            while (ptr is not None):
                # print (f"Info = {ptr.get_data()} and link = {ptr.get_next()}...")
                print (ptr.get_data(), end = ", ")
                ptr = ptr.get_next()

data_list = [11,9,12,10]
link_list = LinkedList()
for info in data_list:
    link_list.ll_append(info)

print(link_list)

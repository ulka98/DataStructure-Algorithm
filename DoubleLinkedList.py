class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoubleLinkedList:
    def __inint__(self): # Constructor
        self.head = None # Head is the first node in the DLL

    def print_forward(self):
        dllstr = ""
        itr = self.head
        print("Printing Forward linked list:")
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            while itr:
                dllstr += str(itr.data) + "--->"
                itr = itr.next
            print(dllstr)

    def print_backward(self):
        dllstr = ""
        itr = self.head
        print("Printing Backward linked list:")
        if self.head is None:
            print("Linked list is empty")
            return
        while itr.next: # traverse to the end of the list
            itr = itr.next
        while itr: # traverse back to the beginning of the list
            dllstr += str(itr.data) + "--->"
            itr = itr.prev
        print(dllstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beginning (self,data):
        # When the list is empty
        if self.head is None:
            node = Node(data, self.head, None) # Create a new node and point it to the current head
            self.head = node  # Update the head to the new node
        # When the list is not empty
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None: 
            self.head = Node(data,None,None) # If the list is empty, create a new node and assign it to the head
            return
        # Traverse to the end of the list
        itr = self.head 
        while itr.next: 
            itr = itr.next 
        # Insert at the end once we reach the end
        itr.next = Node(data,None,itr)

    def insert_values(self, data_list): # Insert a list of values into the linked list
        self.head = None # Clear the linked list
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        i = 0
        itr = self.head
        while itr:
            i += 1
            itr = itr.next
        return i

    def remove_at(self, index):
        if index <0 or index >= self.get_length(): # Check if the index is valid
            raise Exception("Invalid index")

        if index == 0: # If we are removing the first element
            self.head = self.head.next # Update the head to the next element
            self.head.prev = None
            return
        
        itr = self.head
        counter = 0
        while itr:
            if counter == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    break
            itr = itr.next
            counter += 1


    def insert_at(self, index, data):
        # check for valid index
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        #insert at the beginning
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                newNode = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = newNode
                itr.next = newNode
                break
            itr = itr.next
            counter += 1
     

if __name__ == '__main__':
    '''
    ll = LinkedList()
    #ll.insert_at_beginning(5)
    #ll.insert_at_beginning(89)  
    #ll.print()
    #ll.insert_at_end(69)
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    ll.insert_values(fruits)
    ll.print()
    ll.remove_at(2) # Remove cherry
    ll.print()
    ll.insert_at(2, "cherry")
    ll.print()
    '''
    ############################## Exercise ##############################    
    ll2 = LinkedList()
    ll2.insert_values(["banana","mango","grapes","orange"])
    ll2.print()
    ll2.insert_after_value("mango","apple") # insert apple after mango
    ll2.print()
    ll2.remove_by_value("orange") # remove orange from linked list
    ll2.print()
    ll2.remove_by_value("figs")
    ll2.print()
    ll2.remove_by_value("banana")
    ll2.remove_by_value("mango")
    ll2.remove_by_value("apple")
    ll2.remove_by_value("grapes")
    ll2.print()

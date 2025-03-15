class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __inint__(self): # Constructor
        self.head = None # Head is the first node in the linked list

    def insert_at_beginning (self,data):
        node = Node(data, self.head) # Create a new node and point it to the current head
        self.head = node  # Update the head to the new node

    def print(self):
        llstr  = ""
        itr = self.head
        print("Printing linked list:")
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            while itr:
                llstr += str(itr.data) + "--->"
                itr = itr.next
            print(llstr)

    def insert_at_end(self, data):
        if self.head is None: 
            self.head = Node(data,None) # If the list is empty, create a new node and assign it to the head
            return
        # Traverse to the end of the list
        itr = self.head 
        while itr.next: 
            itr = itr.next 
        # Insert at the end once we reach the end
        itr.next = Node(data,None)

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
            return
        
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1: # Stop at the element before the element we want to remove
                itr.next = itr.next.next # Skip the next element (i.e., the element we want to remove)               
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
                newNode = Node(data, itr.next)
                itr.next = newNode
                break
            itr = itr.next
            counter += 1
    ############################## Exercise ##############################        
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        counter = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                #insert data_to_insert after data_after node 
                self.insert_at(counter+1, data_to_insert)
                break
            counter += 1
            itr = itr.next
    
    def remove_by_value(self, data):
        # Remove first node that contains data
        # Search for first occurance of data_after value in linked list
        counter = 0
        itr = self.head
        while itr:
            if itr.data == data:
                #insert data_to_insert after data_after node 
                self.remove_at(counter)
                break
            counter += 1
            itr = itr.next        

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

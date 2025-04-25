class Hashmap:

    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    #hash function using modulus operator
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    #insert function
    def __setitem__(self,key, value):
        h = self.get_hash(key)
        found = False
        # address collision using chaining
        for ix, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key: # check if the key already exists, then update the value
                self.arr[h][ix] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
            

    #get function
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if len(element)==2 and element[0]==key: 
                return element[1]
        return None
        
    
    #delete function
    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] == []:
            print("Key not found")
            return
        for ix, element in enumerate(self.arr[h]):
            # if the key is not found, we can stop searching
            if key not in element:
                print("Key not found")
                return
            # if the key is found, we can delete the element
            if len(element)==2 and element[0]==key:
                del self.arr[h][ix] 

class HashmapWithLinearProbing:

    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    #hash function using modulus operator
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    #insert function
    def __setitem__(self,key, value):
        h = self.get_hash(key)
        # address collision using linear probing
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            if self.arr[h][0] == key: # check if the key already exists, then update the value
                self.arr[h] = (key, value)
            else:
            # find the next empty slot
                h_next = h
                while self.arr[h_next] is not None:
                    h_next = (h_next + 1) % self.MAX # modulus operator to wrap around because of circular array
                    if h_next == h:
                        print("Hashmap is full")
                        return
                self.arr[h_next] = (key, value)
            
    #get function
    def __getitem__(self, key):
        # address collision using linear probing to fetch the value
        for ix, element in enumerate(self.arr):
            if element is None:
                return None
            if element[0] == key:
                return element[1]
        
    
    
    #delete function
    def __delitem__(self, key):
        h = self.get_hash(key)
        # address collision using linear probing to delete the value
        for ix, element in enumerate(self.arr):
            if element is not None and element[0] == key:
                self.arr[ix] = None
                break
            if ix == len(self.arr)-1  and (element is None or element[0] != key):
                print("Key not found")
                # if we reach the end of the array and the key is not found, we can stop searching
                # because the array is circular and we have already checked all the elements
                break
                


def main():
    print("handling collisions using chaining")
    t = Hashmap()
    t["march 6"] = 210
    t["march 7"] = 220
    t["march 8"] = 230
    print(t.arr)
    t["march 17"] = 180
    print(t.arr)
    del t["march 6"]
    print(t.arr)
    print(t["march 17"])
    del t["march 1"]
    print(t.arr)

    print("handling collisions using linear probing")
    lp = HashmapWithLinearProbing()
    lp["march 6"] = 210
    lp["march 7"] = 220
    lp["march 8"] = 230
    print(lp.arr)
    lp["march 17"] = 180
    print(lp.arr)
    del lp["march 6"]
    print(lp.arr)
    del lp["march 10"]
    print(lp["march 17"])
    print(lp["march 1"])

if __name__ == "__main__":
    main()
          

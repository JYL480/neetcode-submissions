"""
0. WHat do you need to do???
- THis question asks for a LRU for this hor
- Which will require to have a doubly linked list which is left and right loh, where  the right will most RU and left will be hte LRU


4. Note that with a doubly linked list, you will need to create 4 things yah
- Remove, insert the node class and the init

- Then to use get or put on the ndoeo, you will have to remove and insert again as it is "used"

- then for the LRU, we just note that to do lah hor


"""

class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key 
        # Creating a new linked list will need to assign the prev and next
        self.next = None 
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.hs = {}
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def remove(self,key):
        # Wdym by remove removae theat specific node
        node = self.hs[key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, key):#Here we will the right side yah this is the important art!!

        node = self.hs[key]
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

        # Should be correct LOL

    def get(self, key: int) -> int:
        # Get what is get, you willl return the value inside yah
        # if not it will be - 1
        
        if key in self.hs:
            self.remove(key)
            self.insert(key)
            return self.hs[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Will add the the hs map and also when put will update that shit yah if there is a new value

        # If want to update then...

        if key in self.hs:
            self.remove(key)

        self.hs[key] = Node(value, key)
        self.insert(key)


        if len(self.hs) > self.cap:
            lru = self.left.next
            self.remove(lru.key)
            del self.hs[lru.key]
        

        

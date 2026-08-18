"""
- This is a lined list question leh, 
- You would have to set up a linked list for htis?
- or doublly linked list what is this??
- I honestly dk, so we will l


- We will be using a doubly linker list


"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:


    def __init__(self, capacity: int):
        # Here we will init the things
        # hash map and the dummy nodes which points?
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.cap = capacity 
        self.cache = {}

        # Point the heads to each other first?
        self.left.next = self.right
        self.right.prev = self.left


    def insert(self, node):
        # How the fk do i insert, we need to inser to the left of this hsit
        prev, nex = self.right.prev, self.right

        prev.next = node
        nex.prev = node

        node.prev = prev
        node.next = nex


    
    def remove(self,node):


        # Urmm removeing uh 

        prev = node.prev
        nex = node.next
        prev.next = node.next
        nex.prev = node.prev


    def get(self, key: int) -> int:
        # So if you get then you will remove and then insert to the right
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 


    def put(self, key: int, value: int) -> None:
        # Put you have to add inside
        # So if there is aldy, you dont add, 
        # If thekey exisit, you will update the value, else add the new

        if key in self.cache:
            self.remove(self.cache[key])
        # You will remove and just update
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) >self.cap:
            # Remove the LRYU, whihc is the right most
            lru = self.left.next
            self.remove(lru)
            # Then delete from the cache
            del self.cache[lru.key]
        











        

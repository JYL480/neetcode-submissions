"""
0. Lets just restart this and then we will do read the limitatiosn and rest of figures first 
- Note taht are using doubly linked list for this yah!
- we have to create 4 things plus a hash for this 

1. 


"""

class Node: # We are trying to create a new node for ts
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # What are we ininti inside yah? IDK, lets see yah 
        # We will create a tail and head dumy nodes, because we are doing what doubly LL
        self.head, self.tail = Node(0,0), Node(0,0)
        # Then you will connect them 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # We return the value i nthe cache ig
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        # HEre er are create a new node to put in the cache or we update yah, so have to create new Node() and account for LRU
        if key in self.cache:
            # Then we will update the value
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.insert(node)
            return # We will break here
        
        if len(self.cache) == self.cap:
            lru = self.head.next
            self.delete(lru)
            del self.cache[lru.key]

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

    def insert(self, node): # LRU all the way to left, MRU all the way to the right
        # We will attach this current node first then to the rest 
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        # SHould be like this 

    def delete(self, node): # Not returnign anything yah
        node.prev.next = node.next
        node.next.prev = node.prev


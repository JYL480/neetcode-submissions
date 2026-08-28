"""
0. Immediately for this question, you have to use a doubly linked list yah 
- Where you will have left and right left iwll bet hehLRU and Right wiill the MRU 
- When creating a doubly LL, you need to create 4 things
- Which is the class Node, init, remove and insert. You have to note that you must amend the neighbours first then the node itself yah 

4. pattern-
- Like that loh


"""


class Node:

    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        # Combine them tgt
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(key)

            return self.cache[key].value
        else:
            return - 1
        

    def put(self, key: int, value: int) -> None:
        # Urm meaning you will create a new one or update the value yah 

        if key in self.cache:
            self.cache[key].value =value
            self.remove(key)
        else:
            self.cache[key] = Node(key, value)

        self.insert(key)


        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru.key)
            del self.cache[lru.key]


    def insert(self, key):
        node = self.cache[key]
        # When you insert, you will insert to the righ


        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next= node
        self.tail.prev = node

    def remove(self, key):
        node = self.cache[key]
        
        node.prev.next = node.next
        node.next.prev = node.prev

        # O think should be like this hor LOL













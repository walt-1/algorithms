# Least Recently Used Cache

# Cache Eviction Policy
# Cache has a set limit. 
#  - New items are prepended to cache which forces a pop of last item. 
#  - A call to an item sets it to the head or index 0

# Cache uses doubly linked list with dummy head and tail for constant access to node neighbors for fast removal
# Backed by a hashtable for fast lookups of items in the cache

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache: # SPACE: O(n) 
    # region Constructor
    def __init__(self, max_capacity=5):
        self.hash_table = dict()
        # cache structure
        self.max_capacity = max_capacity
        self.current_cache_size = len(self.hash_table)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    # endregion
    
    # region Public Methods
    def get_cache_state(self):
        print(f"\nTABLE: {self.hash_table}")
        print(f"CACHE SIZE: {self.current_cache_size}")
        print(f"CACHE MAX: {self.max_capacity}")
        print(f"HEAD: {self.head.next.key} {self.head.next.value}")
        print(f"TAIL: {self.tail.prev.key} {self.tail.prev.value}\n")

    def get(self, key): # O(1)
        if key not in self.hash_table:
            print(f"{key} not in cache \n")
        else:
            node = self.hash_table[key]
            self._move_to_head(node)

            return node.value

    def put(self, key, value): # O(1)
        if key not in self.hash_table:
            node = Node(key, value)
            self.hash_table[key] = node
            self._dll_append(node)
            self.current_cache_size = len(self.hash_table)

            if self.current_cache_size > self.max_capacity:
                self._execute_LRU_policy()

        else:
            self.hash_table[key] = value
            self._move_to_head(node)
    # endregion 
     
    # region Private Methods
    def _execute_LRU_policy(self):
        tail = self._pop_tail()

        print(f"Eviction Policy executed {tail.key} {tail.value} \n")
        del self.hash_table[tail.key]
        self.current_cache_size = len(self.hash_table)

    def _pop_tail(self):
        tail = self.tail.prev
        self._dll_remove(tail)

        return tail

    def _dll_remove(self, node):
        saved_prev = node.prev
        saved_next = node.next

        # [join] -> [removed] <- [join] = [joined] - [joined]
        saved_prev.next = saved_next
        saved_next.prev = saved_prev

    def _dll_append(self, node):
        # creates associations for new node
        node.prev = self.head
        node.next = self.head.next
        
        # creates associations for current doub link list with new node 
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node):
        self._dll_remove(node)
        self._dll_append(node)
    # endregion


# CALLS
cache = LRUCache()

for i in range(0, 6):
    cache.put(i, "value_" + str(i))

cache.get_cache_state()

cache.get(3)
cache.get_cache_state()

cache.get(7)


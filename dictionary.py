# ** DICTIONARIES **

# Compares dictionaries and lists
## Order : In dictionaries, there is no sorting or ordering based on when an item is inserted
## lists do order based on when an item is inserted 

# initializes empty list and empty dict
d = {}
l = []

# dicts can use multiple data types as keys
d[1] = 'yes'
d['1'] = 'no'

# test class 
class person():
  def __init__(self, name):
    self.name = name

# creates instance of person and assigns it as to key in dict
me = person("Luke")
d['object'] = me
print("NAME: " + d['object'].name)


# d.keys -> [ k, k ... ]
print("KEYS: " + str(d.keys()))
for key in d.keys():
  print(type(key))

# d.items() -> [ (k,v), (k,v) ... ]
# returns and array of kv pairs as tuples 
print("\n ITEMS: " + str(d.items()))
for (k, v) in d.items():
  print(v)


# performance benchmark
names = ["Luke", "Jenny", "David", "Lexie", "Russell", "Paula"]

# extend method
more_names = ["Sam", "Teig"]
names.extend(more_names[:len(more_names)])
print("\nEXTENDED: " + str(names))

# creates a dataset in txt file in this dir
def create_dataset():
  import random
  num_entries = 5000000
  f = open('data.txt', 'w')
  for i in range(num_entries):
    current = random.choice(names)
    f.write(current + "\n")
  f.close()

# reads file using list implementation
def list_read():
  name_count = []
  for n in names:
    name_count.append(0)
  with open('data.txt', 'r') as f:
    for line in f:
      line = line.strip()
      if line != '':
        # [(count of "luke") , (count of "jenny")]
        name_count[names.index(line)] += 1
  print(name_count)

# reads file using dictionary implementation
def dict_read():
  name_count = {}
  for n in names:
    name_count[n] = 0
  with open('data.txt') as f:
    for line in f:
      line = line.strip()
      if line != '':
        # []
        name_count[line] += 1
  print(name_count)

# create_dataset()

import time
print("\nStart time benchmarking ...\n")

# list time O(n)
t0 = time.time()
list_read()
t1 = time.time()
print("List took %0.1f seconds\n" % (t1-t0))

# dictionary time O(1)
t0 = time.time()
dict_read()
t1 = time.time()
print("Dictionary took %0.1f seconds\n" % (t1-t0))

def create_array(size = 10, max = 50):
  from random import randint
  list = [randint(0, max) for _ in range(size)]
  return list
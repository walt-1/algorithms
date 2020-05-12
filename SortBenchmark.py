from create_array import create_array
from time import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quicksort import quicksort

n = [10, 100, 1000, 10000]
times = {
  'quicksort':[],
  'merge_sort':[],
  'insertion_sort':[],
  'bubble_sort':[],
  'selection_sort':[]
}
samples = 5

for size in n:
  tot_time = 0
  for _ in range(samples):
    list = create_array(size, size)
    t0 = time()
    s = quicksort(list)
    t1 = time()
    tot_time+=(t1 - t0)
  times['quicksort'].append(tot_time/float(samples))
  
  ms_time = 0
  for _ in range(samples):
    list = create_array(size, size)
    t0 = time()
    s = merge_sort(list)
    t1 = time()
    ms_time += (t1 - t0)
  times['merge_sort'].append(ms_time/float(samples))
  
  ins_sort = 0
  for _ in range(samples):
    list = create_array(size, size)
    t0 = time()
    s = insertion_sort(list)
    t1 = time()
    ins_sort+=(t1 - t0)
  times['insertion_sort'].append(ins_sort/float(samples))
  
  bub_sort = 0
  for _ in range(samples):
    list = create_array(size, size)
    t0 = time()
    s = bubble_sort(list)
    t1 = time()
    bub_sort+=(t1 - t0)
  times['bubble_sort'].append(bub_sort/float(samples))
  
  tot_time = 0
  for _ in range(samples):
    list = create_array(size, size)
    t0 = time()
    s = selection_sort(list)
    t1 = time()
    tot_time+=(t1 - t0)
  times['selection_sort'].append(tot_time/float(samples))

print("\n\tSelectiont\tBubble\tInsertion\tMerge\tQuicksort")
print(90*"_")
for i, size in enumerate(n):
  print("%d\t%0.5f \t%0.5f \t%0.5f \t%0.5f \t%0.5f"%(
    size,
    times['selection_sort'][i],
    times['bubble_sort'][i],
    times['insertion_sort'][i],
    times['merge_sort'][i],
    times['quicksort'][i]
  ))
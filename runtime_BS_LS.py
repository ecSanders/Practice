'''
Create a list of 10,000 random numbers between 0 and 10,000. 
Run Linear Search 1,000 times (searching for a different random 
number each time) and keep track of how long it takes. Similarly, 
run Binary Search 1,000 times, keeping track of how long it takes. 
Which one is faster? By how much? What if we did 10,000 times? 
What about 100?
'''

import random
import time

# Set up
my_list = []
for i in range(1000):
  my_list.append(random.randint(1,10000))

# Linear Search
def linear_search(my_list, target):
  for i in my_list:
    if i == target:
      return True
  return False

# Binary Search
def binary_search(my_list, target):

  mid = len(my_list)//2

  if my_list[mid] == target:
    return True
  
  if len(my_list) == 1:
    return False

  if my_list[mid] > target:
    return binary_search(my_list[:mid], target)
  else:
    return binary_search(my_list[mid:], target)

my_list.sort()
l_start = time.time()
for i in range(1000):
  target = random.randint(1,10000)
  linear_search(my_list, target)
l_end = time.time()

b_start = time.time()
for i in range(1000):
  target = random.randint(1,10000)
  binary_search(my_list, target)
b_end = time.time()
linear_time = l_end - l_start
binary_time = b_end - b_start

print(f'Linear Search: {linear_time}')
print(f'Binary Search: {binary_time}')

print(f'Binary search is {linear_time - binary_time:.2f} seconds faster')
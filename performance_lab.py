# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    
    Numbers_count={}
    for i in numbers:
        if i in Numbers_count:
            Numbers_count[i]+=1
        else:
            Numbers_count[i]=1
    most_frequent_number= max(Numbers_count, key= Numbers_count.get)
    print(most_frequent_number)

#most_frequent([1, 3, 2, 3, 1, 1, 3])
"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
It iterates through the list once to count occurrences and uses a dictionary to store counts.
- Could it be optimized?
I don't think so, as we need to check all elements to find the most frequent one.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    Seen = set()
    result = []
    for i in nums:
        if i not in Seen:
            Seen.add(i)
            result.append(i)
    print(result)

#remove_duplicates([4, 5, 4, 6, 5, 7,7,8,6,2,43,6,7,7,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9])

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case:O(n)
- Average-case:O(n)
- Space complexity:O(n)
- Why this approach?
It uses a set to store the elements in the numbers, if the element is in the set it wont be added again, and then we change it to a list to print it out
- Could it be optimized?
I dont think so, as we need to check all elements to remove duplicates while preserving order.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    for i in nums:
        complement = target - i
        if complement in seen:
            print((complement, i))
        seen.add(i)
#find_pairs([1, 2, 3, 4], 5)
"""
Time and Space Analysis for problem 3:
- Best-case:O(n)
- Worst-case:O(n)
- Average-case:O(n)
- Space complexity:O(n)
- Why this approach?
Using a set to store the items and have a faster lookup time of (O(1)) for each complement check.
- Could it be optimized?
I don't think so, as we need to check all elements to find pairs that sum to the target.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity= 1
    size= 0
    
    for i in range(n):
        if size == capacity:
            capacity *=2
            print(f"Resizing: New capacity is {capacity}")
        size +=1
        print(f"Added item {i+1}, size is now {size}, capacity is {capacity}")
#add_n_items(6)

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
rezises happen when the current size equals the capacity of the list.
- What is the worst-case for a single append?
when a resize happens, the worst-case time for a single append is O(n) due to copying all elements to the new list.
- What is the amortized time per append overall?
The amortized time per append is O(1) because the cost of resizing is spread out over multiple appends.
- Space complexity:
O(n) because we may need to allocate additional space when resizing.
- Why does doubling reduce the cost overall?
because if you increase the capacity one by one, you would have to resize every time you add an element, leading to O(n^2) time complexity for n appends.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    print(result)
#running_total([1, 2, 3, 4,5,6,7,8,9,10])
"""
Time and Space Analysis for problem 5:
- Best-case:O(n)
- Worst-case:O(n)
- Average-case:O(n)
- Space complexity:O(n)
- Why this approach?
is efficient only iterates one time through the list, maintaining a running total and appending to the result list.
- Could it be optimized?
yes, we could do it in place if modifying the original list is acceptable, reducing space complexity to O(1).
"""
#Optimization of problem 5:
def running_total_inplace(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    print(nums)
running_total_inplace([1, 2, 3, 4,5,6,7,8,9,10])
#insted of creating a new lsit, we just modify the original one and have the same time complexity of O(n) but a space complexity of O(1), so we save space.

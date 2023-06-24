# Determining the factorial of any number. Factorial is multiplying the number with every 1unit less than the number until
# it's 0. for example, 5!= 5*4*3*2*1

# Hence, n!= n*(n-1)*(n-2)*...........2*1

#factorial
def factorial(n):
    if n==1:
        return n
    return n* factorial(n-1)
# print(factorial(5))

#permutation
def permute(string, pocket=' '):
    if len(string)==0:
        print(pocket)
    for i in range(len(string)):
        letter= string[i]
        front= string[0:i]
        back= string[i+1:]
        together= front+back
        permute(together, letter+pocket)
# print(permute('ABC', ''))


#binary search
def bin(arr, start, end, target):
    if end>=start:
        mid= (start+end)//2
        if arr[mid]==target:
            print('index of the target is ', mid)
        elif arr[mid]<target:
            return bin(arr, mid+1, end, target)
        elif arr[mid]>target:
            return bin(arr, start, mid-1, target)
arr= [1,2,3,4,5,6,7]
# bin(arr, 0, len(arr)-1, 3)

#linear search
def lin(arr, target):
    if len(arr)==0:
        return False
    if arr[0]==target:
        return True
    else:
        return lin(arr[1:], target)

arr= [1,2,3,4,5,6,7]
# print(lin(arr, 9))

#bubble sort is a kind of sort which can automatically detect if the array is sorted or not in a single iteration. No other sorting method
# contains this ability of detecting the sort at its first place. But the thing is bubble sorting is kind of worst sorting method because of 
# its repeated sorting and also very inefficient than other methods.

#bubble sort
def bubble(arr):
    iteration=0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            iteration+=1
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
    return arr, iteration

arr= [1,5,3,4,7,2,6]
# print(bubble(arr))

#insertion sort
def insertion(arr):
    for j in range(1, len(arr)):
        key= arr[j]
        i= j-1
        while i>=0 and arr[i]>key:
            arr[i+1]= arr[i]
            i-=1
        arr[i+1]= key
    return arr

arr= [1,5,3,4,7,2,6]
# print(insertion(arr))


#linked list
class Node:
    def __init__(self, data):
        self.data=data
        self.next= None
class LinkedList:
    def traversal(self):
        temp= self.head
        if temp.data=='Farhad':
                temp= Node('Dave')
                family.head= temp
                family.head.next= wife
        while temp!=None:
                print(temp.data)
                temp= temp.next

family= LinkedList()
family.head= Node('Farhad')
wife= Node('Nargis')
first_kid= Node('Rhythm')
second_kid= Node('Riha')
third_kid= Node('Najib')

family.head.next= wife
wife.next= first_kid
first_kid.next= second_kid
second_kid.next= third_kid

# family.traversal()

# Time complexity:
# ------time complexity for any constant is O(1)
# ------function: f(n)
# ------counts in unit time 



# Space omplexity:
# ------ function: s(n)
# ------counts in words
# ------ counts variables only

# time and space complexity have not to be the same always
    



# ternary search
# it slipts up the given array into 3 pieces. it is more efficient than binary search. there're two mid points in ternary search. 

#time complexity example:
swap(a,b){
    temp= a #-----------------1
    a=b#-----------------1
    b= temp
}

# we will assume that every single statement in an algorithm will take one
# unit of time.
# Here, 1+1+1=3. so f(n)=3, therefore the time complexity is o(1); constant time.
# the agorithm is not dependant on the input size.

# Again, #space complexity
# we have 3 variables here, temp, a and b. each variable = 1 word. 
# Here, 1+1+1=3. so s(n)=3. therefore, space complexity is O(1)


sum(A,n) {
    s=0 #------------1
    for(i=0, i<n, i++){ #------------(n+1)
        s= s+A[i] #------------n
    }
    return s #------------1
}
# here f(n)= 1+n+1+n+1= 2n+3. the degree of polynomial is 1.
#  degree of polynomial= the power of n
# thus, time complexity is O(n)
# 3 is not significant, and considering 2n and n is the same rather n 
# is more thoughtful.

# again
# here we have 4 variables: A=n words, n=1 word, s= 1 word, i= 1 word.
# thus s(n)= n+3. hence the space complexity is O(n)

add(A, B, n){
    for(i=0, i<n, i++){  #------------(n+1)
        for (j=0, j<n, j++) {  #------------nx(n+1)
            C[i,j]= A[i,j]+ b[i,j]  #------------nxnx1
        }
    }
}

# here f(n)= n+1+n2+n+n2 => n2 is most significant there
# so time complexity is O(n2)

again
we have 6 matrices and one variable.
A #------------n2
B #------------n2
c #------------n2
n #------------1
i #------------1
j #------------1
# s(n)= 3n2 +3. so the space complexity is O(n2)


# merge sort
def MergeSort(arr):
  if len(arr)<=1:
    return arr
  
  mid=(len(arr))//2
  
  left= MergeSort(arr[:mid])
  right= MergeSort(arr[mid:])
  
  return Merge(left, right)

def Merge(left, right):
  a=[]
  i,j=0,0

  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      a.append(left[i])
      i+=1
    else:
      a.append(right[j])
      j+=1
  
  while i<len(left):
    a.append(left[i])
    i+=1
  
  while j<len(right):
    a.append(right[j])
    j+=1
  
  return a

arr= [9,4,5,2,1,7,4,6]
# print(MergeSort(arr))
     

#quicksort
def quickSort(arr):
  if len(arr)<=1:
    return arr

  pivot= (len(arr))//2
  left= []
  right=[]
  middle=[]
  for i in range(len(arr)):
    if arr[i]<arr[pivot]:
      left.append(arr[i])
    if arr[i]>arr[pivot]:
      right.append(arr[i])
    if arr[i]==arr[pivot]:
      middle.append(arr[i])
  
  return quickSort(left)+ middle+ quickSort(right)

arr= [6,10,13,5,8,3,2,11]
# print(quickSort(arr))

# After working with the binary search algorithm, as a CS-221 student you want to explore its strength.
# You have several ideas in your mind. Try to modify the algorithm to implement your ideas. 

#a. Instead of just returning TRUE or FALSE, you want to return the index of the search key if it exists in the list.
# Return FALSE or –ve index in case it is not found. 
def binarySearch(arr, low, high, target):
  while low<=high:
    mid= (low+high)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]<target:
      return binarySearch(arr, mid+1, high, target)
    elif arr[mid]>target:
      return binarySearch(arr, low, mid-1, target)

  return False

items = [2, 3, 4, 10, 40, 44, 55, 70, 80, 90, 100]
# print(binarySearch(items, 0, len(arr), 400))

#b. What if you want to return the first index of the search key in case there are duplicates.
# For example: your search key is 13 and there are three 13s in the list. 
def binarySearch(arr, low, high, target):
  flag=False
  while low<=high:
    mid= (low+high)//2
    if arr[mid]==target:
      if int(arr[mid]) not in arr[:mid]:
        flag= True
        return mid
      else:
        return binarySearch(arr, low, mid-1, target)
    elif arr[mid]<target:
      if flag==True:
        break
      return binarySearch(arr, mid+1, high, target)
    elif arr[mid]>target:
      if flag==True:
        break
      return binarySearch(arr, low, mid-1, target)

  return False


items = [1, 3, 4, 7, 10, 13, 13, 13, 17, 20, 22, 25, 30, 35, 40]
# print(binarySearch(items, 0, len(items), 2))

#c. Now, along with the first index, you also want to return the number of times the key appears in the list.
# Say, the search key is 54 and it occurs 4 times in indices 6,7,8,9. Then you should return (6,4). 
def binarySearch(arr, low, high, target):
  flag=False
  while low<=high:
    mid= (low+high)//2
    if arr[mid]==target:
      if int(arr[mid]) not in arr[:mid]:
        flag= True
        return (mid, count(target))
      else:
        return binarySearch(arr, low, mid-1, target)
    elif arr[mid]<target:
      if flag==True:
        break
      return binarySearch(arr, mid+1, high, target)
    elif arr[mid]>target:
      if flag==True:
        break
      return binarySearch(arr, low, mid-1, target)
  return False

def count(n):
  count=0
  for i in range(len(items)):
    if items[i]==n:
      count+=1
  return count

items = [10, 20, 30, 40, 42, 50, 54, 54, 54, 54, 55, 56, 57, 58, 59, 60, 70, 80, 90, 100]
# print(binarySearch(items, 0, len(items), 54))

#d. You have a list of numbers that follows a wave-like pattern. First the numbers follow a decreasing pattern,
# then after a point, they start increasing again. So there is a minimum element in the list. Can you find that by modifying binary search? 
def waveSearch(arr):
  start= 0
  end= len(arr)-1

  while start<=end:
    mid= (start+end)//2

    if (mid!=arr[0] or arr[mid]<arr[mid-1]) and (mid!=arr[len(arr)-1] or arr[mid]<arr[mid+1]):
      return arr[mid]
    elif arr[mid]>arr[mid+1]:
      start= mid+1
    else:
      end= mid-1

arr=[5,4,3,2,1,6,7,8,9]
# print(waveSearch(arr))


# assignment task-1
# task-1
def binarySearch(arr, low, high, target):
  flag=False    #indicator
  while low<=high:
    mid= (low+high)//2

    if arr[mid]==target:
      if int(arr[mid]) not in arr[:mid]:  #checking if the target is already present before
        flag= True    #confirming very first index
        return mid   #returning index of the search key 
        return (mid, count(target))   #returning the index and total no of appearance of target
      else:
        return binarySearch(arr, low, mid-1, target)    #recursion call to find the very first index

    elif arr[mid]<target:
      if flag==True:  #already found very first index of target
        break
      else:
        return binarySearch(arr, mid+1, high, target)
    
    elif arr[mid]>target:
      if flag==True:  #already found very first index of target
        break
      return binarySearch(arr, low, mid-1, target)

  return False  #in case if the target is not found

def count(n):
  count=0
  for i in range(len(items)):
    if items[i]==n:
      count+=1  #counting the apprearance of target
  return count

def waveSearch(arr):
  start= 0
  end= len(arr)-1

  while start<=end:
    mid= (start+end)//2

    if (mid!=arr[0] or arr[mid]<arr[mid-1]) and (mid!=arr[len(arr)-1] or arr[mid]<arr[mid+1]):
      return arr[mid]   #smallest value
    elif arr[mid]>arr[mid+1]:
      start= mid+1
    else:
      end= mid-1

items = [2, 3, 4, 10, 40, 44, 55, 70, 80, 90, 100]
print(binarySearch(items, 0, len(items), 400))  #call for task-a

items = [1, 3, 4, 7, 10, 13, 13, 13, 17, 20, 22, 25, 30, 35, 40]
print(binarySearch(items, 0, len(items), 2))  #call for task-b

items = [10, 20, 30, 40, 42, 50, 54, 54, 54, 54, 55, 56, 57, 58, 59, 60, 70, 80, 90, 100]
print(binarySearch(items, 0, len(items), 54))   #call for task-c

arr=[5,4,3,2,1,6,7,8,9]
print(waveSearch(arr))    #call for task-d

# task-3
# 3-a
def find_peak(arr):
  start = 0
  end = len(arr) - 1

  while start < end:
    mid = (start+ end)//2
    if arr[mid] < arr[mid + 1]:
      start = mid + 1
    else:
      end = mid
    return arr[start]

array = [1, 3, 4, 5, 9, 6, 2, -1]
print(find_peak(array))

# 3-b
The time it takes for this algorithm to run gets slower in a very manageable
way as the size of the list of numbers increases. Imagine if you had a list
of 100 numbers. In the worst case, the algorithm would need to check about
7 numbers (actually fewer) before it found the highest one. If you doubled
the size of the list to 200 numbers, the algorithm would only need to check
one extra number, about 8 in total (actually fewer). This is much better than
having to potentially check every number in the list, which is what a slower
algorithm (with time complexity O(n)) would do. That's why we say this algorithm
has a time complexity of O(log n) - it's a technical way of saying it handles
bigger lists very efficiently!

# task-04
# 4-a
It's true that if only performing a single search, it's more efficient to just
do a linear search on an unsorted array, which takes O(n) time, rather than sorting the
array first in O(n log n) time and then doing a binary search in O(log n) time.

However, there are situations where sorting the array first can pay off:

1. **Multiple Searches:** If you need to perform multiple searches on the same array,
sorting it first and then using binary search can be more efficient. After the initial
sort, each subsequent search is done in O(log n) time, which can be a substantial savings
if you're doing a lot of searches.

2. **Need for Ordered Data:** If you need the data to be in sorted order for other parts
of your program, then you'd need to sort the array anyway. Once the array is sorted, using
binary search for any searches can be more efficient.

3. **Memory Considerations:** Linear search can be more memory-efficient as it does not
require the array to be sorted, thus not needing extra space. However, in scenarios where
space isn't a concern but time complexity is (like searching in a very large array), sorting
the array first might be beneficial.

# 4-b
count sort

# 4-c
count sort

# 4-d
In the described scenario where memory is a significant constraint, Quick Sort would
generally be a better choice than Merge Sort. Here's why:

**Space Complexity:** Quick Sort is an in-place sorting algorithm, which means it
sorts the data in the array it is given without needing to create additional significant
space. The space complexity of Quick Sort is O(log n) due to the recursion stack in the
worst case. On the other hand, Merge Sort requires additional space equal to the size of
the input array for merging operations, which means its space complexity is O(n). This
could potentially be a problem when memory is a major constraint.

# 4-e
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
This array is already sorted, so if QuickSort chooses the first element as the pivot at
each step, it will create partitions where one part contains one element (the pivot) and
the other contains the rest of the array, leading to the worst-case time complexity of O(n^2).

# 4-f
simulation

# task-05
# 5-a
# pseudo code for linear search
function of linearSearch(array, target)
  setting i=0
  when i<length of array
    if array[i] is target
      return i
    i+=1
  return -1

# 5-b
#  count sort

# 5-c
Yes, it's possible that the crash was a result of the counting sort algorithm. The reason lies in
the space complexity of counting sort.

The space complexity of counting sort is O(k), meaning it needs to create an auxiliary array of size
k, where k is the maximum element in the input array.

In this case, if a few users uploaded 1000 pictures each, the 'user post count' values could be in
the thousands. If you used these counts directly as indices for the count array, the algorithm would
try to create an array of size in the order of the maximum post count value.

For example, if the maximum post count is 1000, counting sort would create an array of size 1000, most
of which would be unused if there aren't many users with post counts close to that maximum. This can
result in a huge amount of wasted space. In a server environment where memory is often limited, trying
to allocate such large amounts of space can indeed lead to a server crash.

A potential solution could be to use a more space-efficient sorting algorithm like QuickSort or MergeSort,
both of which have a space complexity of O(n log n).

# 5-d
username= [Woof, Pupper, Max, Tuck, Rocky, Daisy]
# simulation of merge sort over this array

# 5-e
The searching algorithm you would use in this case is Binary Search. Binary Search works by repeatedly
dividing the search interval in half. If the target value is present in the list, it must lie within the
current search interval. This approach has a time complexity of O(log n) and is very efficient.

post count= [8, 12, 3, 5, 2, 17, 9, 14, 2, 3]
# simulate binary search in this array

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



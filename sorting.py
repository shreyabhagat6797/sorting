'''Selection sort
Using the swap() and find_next_min() functions, implement the selection sort algorithm to sort a list of numbers in ascending order.
'''


def swap(num_list, first_index, second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp


def find_next_min(num_list,start_index):
    mini = min(num_list[start_index::])
    return num_list.index(mini)

def selection_sort(num_list):
    for i in range(len(num_list)):
        index = find_next_min(num_list, i)
        swap(num_list, i,index)


#Pass different values to the function and test your program
num_list=[8,2,19,34,23, 67, 91]
print("Before sorting;",num_list)
selection_sort(num_list)
print("After sorting:",num_list)



'''
Bubble sort
Let’s compare selection sort and bubble sort algorithms in this exercise. 
Combine the selection sort and bubble sort programs as per the template code provided below and display the number of passes for each of them.
Invoke both the functions (selection_sort() and bubble_sort()) using the following two lists and observe the results.

Case 1: [8,2,19,34,23, 67, 91]
Case 2: [91,8,19,23,34,67,2]
'''


def swap(num_list, first_index, second_index):
    temp = num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp

def find_next_min(num_list,start_index):
    return num_list.index(min(num_list[start_index::]))

def selection_sort(num_list):
    for i in range(len(num_list)):
        index = find_next_min(num_list, i)
        swap(num_list, i, index)
    return i

def bubble_sort(num_list):
    total_no_of_passes=0
    end_index=len(num_list)
    for index1 in range(0, end_index-1):
        swapped=False
        total_no_of_passes+=1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2]>num_list[index2+1]):
                swap(num_list, index2, index2+1)
                swapped=True;
        if(swapped==False):
            break
    return total_no_of_passes

num_list=[8,2,19,34,23, 67, 91]
#num_list=[91,8,19,23,34,67,2]
print("Selection Sort - No. of passes:",selection_sort(num_list))
print(num_list)
num_list=[8,2,19,34,23, 67, 91]
#num_list=[91,8,19,23,34,67,2]
print("Bubble Sort - No. of passes:",bubble_sort(num_list))




'''
Merge sort
Implement the merge sort algorithm to sort a list of numbers in ascending order.
'''


def merge_sort(num_list):
    low=0
    high=len(num_list)-1
    if low==high:
        return num_list
    else:
        left_list=num_list[:(len(num_list)//2)]
        right_list=num_list[(len(num_list)//2):]
        list1=merge_sort(left_list)
        list2=merge_sort(right_list)
        sorted_list=merge(list1, list2)
        return sorted_list
def merge(left_list,right_list):
    i,j=0,0
    sorted_list=[]
    while(i<len(left_list) and j<len(right_list)):
        if left_list[i]<=right_list[j]:
            sorted_list.append(left_list[i])
            i+=1
        else:
            sorted_list.append(right_list[j])
            j+=1
    if i<len(left_list):
        sorted_list.extend(left_list[i::])
    if j<len(right_list):
        sorted_list.extend(right_list[j::])
    return sorted_list

num_list=[34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:",num_list)
sorted_list = merge_sort(num_list)
print("After sorting:",sorted_list)


'''
Quick sort
Try out the given code which implements quick sort algorithm. Observe how 
1. pivot is chosen and
2. elements in the list are partitioned such that
•	      values less than the pivot element are arranged to its left and
•	      values greater than the pivot are arranged to its right
3. the above steps are recursively repeated until the list is sorted
 def swap(num_list, first_index, second_index):
    temp=num_list[first_index]
    num_list[first_index]=num_list[second_index]
    num_list[second_index]=temp
  '''



def quick_sort(num_list,low,high):
    if(low>=high):
        return
    split_point=partition(num_list,low,high)
    quick_sort(num_list,low,split_point-1)
    quick_sort(num_list,split_point+1,high)
    
def partition(num_list,low,high):
    pivot=num_list[low]
    i=low+1
    j=high
    done=False
    while not done:
            while (i<=j and num_list[i]<=pivot):
                i=i+1
            while( num_list[j]>=pivot and j>=i):
                j=j-1
            if(j < i):
                done=True
            else:
                swap(num_list,i,j)
    swap(num_list,low,j)  
    return j

num_list=[3,1,0,4,2]
print("Before sorting;",num_list)
l=len(num_list)
quick_sort(num_list,0,l-1)
print("After sorting:",num_list)




'''
The central library at Mysore has a set of very interesting books and journals. The books are arranged in the alphabetical order of their author names. So it is very easy for the readers to search for the book.
 
The library has got a set of new books. The librarian wants to arrange them in order too. As some books are already arranged in the order, find a suitable way of arranging the new set of books amidst them.
 
Write a python program to arrange all the books in the alphabetical order of the author names.
sort_item_list_by_author(): Accepts the new list of books and returns it sorted in the alphabetical order of their author names.
 
add_new_items(): Accepts the new list of books, sorts it and merges it with the existing books in the library.
Hint - Use sort_item_list_by_author() method for sorting the books.
 
sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of their published years. If there are multiple items that are published in the same year, then sort them based on the alphabetical order of their author names.

Note: While sorting the author names in alphabetical order, ignore the special characters including space, if there are any.
'''



#Implement Item class here
class Item:
    def __init__(self, item_name, author_name, published_year):
        self.__item_name=item_name
        self.__author_name=author_name
        self.__published_year=published_year
    def get_item_name(self):
        return self.__item_name
    def get_author_name(self):
        return self.__author_name
    def get_published_year(self):
        return self.__published_year
    def __str__(self):
        return("{} by {} published in {}".format(self.__item_name, self.__author_name, self.__published_year))
#Implement Library class here
class Library:
    def __init__(self, item_list):
        self.__item_list=item_list
    def get_item_list(self):
        return self.__item_list
    def sort_item_list_by_author(self, new_item_list):
        new_item_list.sort(key=lambda x:''.join(e for e in x.get_author_name() if e.isalnum()))
        return new_item_list
    def add_new_items(self, new_item_list):
        self.__item_list.extend(new_item_list)
        self.sort_item_list_by_author(self.__item_list)
    def sort_items_by_published_year(self):
        self.sort_item_list_by_author(self.__item_list)
        self.__item_list.sort(key=lambda x:x.get_published_year())
        
#Use different values for item and test your program
item1=Item("A Mission In Kashmir","Andrew Whitehead",1995)
item2=Item("A Passage of India","E.M.Forster",2012)
item3=Item("A new deal for Asia","Mahathir Mohammad",1999)
item4=Item("A Voice of Freedom","Nayantara Sehgal",2001)
item5=Item("A pair of blue eyes","Thomas Hardy",1998 )

item_list=[item1,item2,item3,item4,item5]
library=Library(item_list)
print("The current items in the library are:")
for item in library.get_item_list():
    print(item)

item11=Item("Broken Wing","Sarojini Naidu",2012)
item12=Item("Guide","R.K.Narayanan",2001)
item13=Item("Indian Summers","John Mathews",2001)
item14=Item("Innocent in Death","J.D.Robb",2010)
item15=Item("Life of Pi","Yann Martel",2010 )
item16=Item("Sustainability","Johny",2016)
item17=Item("Look Ahead","E.M.Freddy",2012 )

new_item_list=[item11,item12,item13,item14,item15,item16,item17]
print()
print("The new items to be added are:")
for item in new_item_list:
    print(item)

new_item_list_sorted=library.sort_item_list_by_author(new_item_list)
print()
print("The new items after sorting based on the author name are:")
for item in new_item_list_sorted:
    print(item.get_author_name())

library.add_new_items(new_item_list_sorted)
print()
print("The final set of items after adding the new item list are:")
for item in library.get_item_list():
    print(item)

library.sort_items_by_published_year()
print()
print("The items sorted based on the increasing order of their published year:")
for item in library.get_item_list():
    print(item.get_author_name() +" "+ str(item.get_published_year()))



'''
Write a python function which accepts two sorted stacks and returns a new stack containing all the elements of input stacks in sorted order.
 
Note: The output stack should be of the size as that of the sum of the sizes of the input stacks.
 
Sample Input	Expected Output
Stack1 (top - bottom): 7,6,5
Stack2 (top - bottom): 3,2,1	Stack (top-bottom) : 7,6,5,3,2,1
Stack1 (top - bottom): 15,10,3
Stack2 (top - bottom): 21,9,7	Stack (top-bottom) : 21,15,10,9,7,3

'''



class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

def merge_stack(stack1,stack2):
    l=[]
    stack3=Stack(stack1.get_max_size()+stack2.get_max_size())
    while(not stack1.is_empty()):
        l.append(stack1.pop())
    while(not stack2.is_empty()):
        l.append(stack2.pop())
    l.sort()
    for element in l:
        stack3.push(element)
    return stack3
        

#Pass different values to the function and test your program
stack2=Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)
  
stack1=Stack(4)
stack1.push(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)
  
print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack=merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()
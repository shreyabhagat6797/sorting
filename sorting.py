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


'''The manager of an airport wants to generate various reports.
Details of the flights and passengers are stored as mentioned below:
1. Flight details are stored as a list of strings. Suppose "AI890:BAN:MUM:1400" is a string in the flight details list, it should be interpreted as follows: AI890 is the flight name , BAN is the source, MUM is the destination and 1400 is the departure time (24 hour format).
2. Passenger details are stored in a dictionary where key is the PNR number of the passenger and value is a list containing passenger details. 
   Suppose "LW101":["Amanda","AI678","C7",25] is an element in the dictionary, it should be interpreted as follows:
  LW101 is the PNR number of the passenger and  ["Amanda","AI678","C7",25] is the list in which the index 0, 1, 2 and  3  represents the passenger name, flight name, seat number and the baggage weight respectively.
Assume that we are considering only those flights which are departing between 0700hrs and 2000hrs.
Write a python program to perform the below mentioned functionalities.
find_flights(flight_time): This method accepts time in 24 hour format and returns the list of flights which are waiting to takeoff within another two hours starting from the given time (both inclusive).
sort_flight_list(flight_list): This method takes the flight details list as the input and returns the flight details list sorted based on the increasing order of their departure time.
get_passenger_details(flight_detail): This method takes a flight’s detail as input and returns the list of PNR numbers of the passengers who are waiting to board the given flight.
security_check(passenger_pnr_list): This method takes the list of PNR numbers of the passengers boarding a specific flight as the input and returns the list of PNR numbers of the passengers whose baggage has been cleared.
The baggage will be cleared if the baggage weight is between 0-25kg (both inclusive)
sort_passengers(passenger_pnr_list): This method takes the list of PNR numbers of the passengers whose baggage has been cleared as the input and returns the list of PNR numbers sorted based on the increasing order of their seat numbers. ( order of seats: A→J )
boarding(passenger_pnr_list): The passengers who have to board a flight should stand in a queue. This method takes the list of PNR numbers of the passengers sorted based on seat numbers as the input and returns the queue of PNR numbers of the passengers. The queue should be of the same size as that of the list. The first passenger in the list should be the first person to stand in the queue.
seating(passenger_queue):The flight has only one door which is at the back side. The passengers who board the flight are expected to occupy seats from the front. So the passenger who board last will be able to come out first from the flight. This method takes the queue of PNR numbers of the passengers as the input and returns the stack ( max size of the stack should be same as the size of the queue) which contains the PNR numbers of the passengers representing the seating.
'''

class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

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

#Global variables
flight_details=["AI890:BAN:MUM:1400","AI678:BAN:LON:1200","AI345:BAN:CAN:1410","AF780:BAN:AGF:1340","AI001:BAN:AUS:1500","AI404:BAN:NY:1220"]
 
passenger_details_dict=\
{"LW101":["Amanda","AI678","C7",25],"LW103":["John","AI345","A2",10],"LW107":["Alex","AI678","G5",12],\
"TW700":["Hary","AF780","D2",26],"LW167":["Kate","AI001","G3",25],"LT890":["Wade","AI404","G3",25],\
"TW677":["Preet","AF780","D3",25],"LA106":["Henry","AI001","B5",25.5],"LA104":["Ajay","AI001","A7",23],\
"LW202":["Amy","AI345","C3",24.5],"LT673":["Susan","AI404","J8",5],"TW709":["Tris","AF780","H5",22.5],\
"LA188":["Cameron","AI890","H4",22],"LA902":["Scofield","AI678","G4",23],"TW767":["Pom","AF780","H4",2],\
"LW787":["Burrows","AI890","B4",29],"LW898":["Sara","AI678","E4",14],"LW104":["Williams","AI890","C4",10] }

def find_flights(flight_time):
    l=[]
    for flight in flight_details:
        detail=flight.split(":")
        if int(detail[3]) in range(flight_time, flight_time+201):
            l.append(flight)
    return l

def sortMethod(val):
    val1=val.split(":")
    return int(val1[3])

def sort_flight_list(flight_list):
    flight_list.sort(key=sortMethod)
    return flight_list
        

def get_passenger_details(flight_detail):
    l=[]
    for key,value in passenger_details_dict.items():
        if value[1] in flight_detail:
            l.append(key)
    return l

def security_check(passenger_pnr_list):
    l=[]
    for pnr in passenger_pnr_list:
        if passenger_details_dict[pnr][3] in range(0,26):
            l.append(pnr)
    return l
            
def sortPassenger(value):
    '''Followed this method in C++ but cannot be used in python:
    # detail1=passenger_details_dict[value1]
    # detail2=passenger_details_dict[value1]
    # if detail1[2][0]==detail2[2][0]:
    #     if int(detail1[2][1:])>int(detail2[2][1:]):
    #         return int(detail2[2][1:])
    #     else:
    #         return int(detail1[2][1:])
    # elif detail1[2][0]>detail2[2][0]:
    #     return detail2[2][0]
    # else:
    #     return detail1[2][0]'''
    detail=passenger_details_dict[value]
    return detail[2]
def sort_passengers(passenger_pnr_list):
    passenger_pnr_list.sort(key=sortPassenger)
    return passenger_pnr_list

def boarding(passenger_pnr_list):  
    queue = Queue(len(passenger_pnr_list))
    for passenger in passenger_pnr_list:
        queue.enqueue(passenger)
    return queue

def seating(passenger_queue):
    stack=Stack(passenger_queue.get_max_size())
    while(not passenger_queue.is_empty()):
        stack.push(passenger_queue.dequeue())
    return stack
        

print("The flight details :")
print(flight_details)
print()
print("The passenger details at the airport:")
print(passenger_details_dict)
print()
time=1130
print("Details of the flight between the timings",time,"and",time+200,"are:")
flight_list=find_flights(time)
flight_list=sort_flight_list(flight_list)
print(flight_list)
print()
print("Details of the passengers boarding the flights between the timings ",time,"and",(time+200),"are:")
print()
for i in range(0,len(flight_list)):
    flight_data=flight_list[i].split(':')
    flight_name=flight_data[0]
    
    passenger_pnr_list=get_passenger_details(flight_list[i])
    print("PNR details of the passengers boarding the flight",flight_name,":")
    print(passenger_pnr_list)
    
    print()
    updated_passenger_pnr_list=security_check(passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," whose baggage has been cleared:")
    print(updated_passenger_pnr_list)
    
    sorted_passenger_pnr_list=sort_passengers(updated_passenger_pnr_list)
    print("PNR details of the passengers of flight",flight_name," sorted based on seating number:")
    print(sorted_passenger_pnr_list)
    
    print()
    print("The PNR details of the passengers at the queue",flight_name,":")
    passenger_queue=boarding(updated_passenger_pnr_list)
    passenger_queue.display()
    
    print()
    seating_stack=seating(passenger_queue)
    print("The PNR details of the passengers in the flight",flight_name,":")
    seating_stack.display()

#searching

'''Given a stack of boxes in different colors. Write a python function that accepts the stack of boxes and removes those boxes having color other than the primary colors (Red, Green and Blue) from the stack. The removed boxes should be en-queued into a new queue and returned. The original stack should have only the boxes having primary colors and the order must be maintained.
 
Perform case sensitive string comparison wherever necessary.
 
Note: Consider the queue to be of the same size as that of the original stack.'''


 class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

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

def separate_boxes(box_stack):
    box_color=['Red', 'Green', 'Blue']
    stack=Stack(8)
    queue=Queue(8)
    while(not box_stack.is_empty()):
        color=box_stack.pop()
        if color.title() in box_color:
            stack.push(color)
        elif color.title() not in box_color:
            queue.enqueue(color)
    while(not stack.is_empty()):
        box_stack.push(stack.pop())
    return queue

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()

'''The International Cricket Council (ICC) wanted to do some analysis of international cricket matches held in last 10 years.
 
Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in Champions Trophy 5 times and have won 2 times.
 
Write a python program which performs the following:
find_matches (country_name): Accepts the country_name and returns the list of details of matches played by that country.
 
max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have won the maximum number of matches in that championship as the value.
 
find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of matches in all championships. If both have won equal number of matches, return "Tie".
 
Perform case sensitive string comparison wherever necessary.
 
match_list – ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']
 
Sample Input	                   Expected Output
find_matches ("AUS")	              ['AUS':CHAM:5:2','AUS:WOR:2:1']
max_wins()	                          {'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}
find_winner("AUS","IND")	            IND
'''
   
def find_matches(country_name):
    l=[]
    for match in match_list:
        detail=match.split(":")
        if detail[0] == country_name:
            l.append(match)      
    return l

def max_wins():
    dictionary={}
    for match in match_list:
        detail = match.split(":")
        if detail[1] not in dictionary.keys():
            dictionary[detail[1]]=None
        if dictionary[detail[1]]==None:
            dictionary[detail[1]]=int(detail[3])
        elif dictionary[detail[1]]>=0:
            if dictionary[detail[1]]<int(detail[3]):
                dictionary[detail[1]]=int(detail[3])
    temp=dictionary.copy()
    for key, values in dictionary.items():
        dictionary[key]=[]
    for match in match_list:
        detail = match.split(":")
        if int(detail[3])==temp[detail[1]]:
            dictionary[detail[1]].append(detail[0])
    return dictionary

def find_winner(country1,country2):
    count1,count2=0,0
    for match in match_list:
        detail = match.split(":")
        if detail[0] == country1:
            count1+=int(detail[3])
        if detail[0] == country2:
            count2+=int(detail[3])
    if count1==count2:
        return "Tie"
    elif count1>count2:
        return country1
    else:
        return country2

#Consider match_list to be a global variable
match_list=['AUS:T20:5:3', 'IND:CHAM:5:3', 'AUS:WOR:2:0', 'CAN:CHAM:5:1', 'ENG:WOR:2:0', 'IND:T20:6:4', 'PAK:T20:4:3', 'IND:WOR:5:3', 'AUS:CHAM:1:0', 'PAK:CHAM:5:1', 'SA:CHAM:5:2', 'SA:T20:5:0', 'PAK:WOR:2:0']

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print(find_matches("AUS"))
print(max_wins())




'''Alice, a school teacher, has decided to take her 20 students to an exhibition. She got the tickets a week before (T1 to T20) and she was informed that students will be allowed only in groups of 10 inside the exhibition hall.
 
On the day of exhibition, few students did not turn up. So the teacher followed the below strategy to identify the first 10 students who were sent as group-1.
 
Suppose the ticket id of the students who turned up on that day is as follows:
T20, T5, T10, T1, T2, T8, T16, T17, T9, T4, T12, T13, T18
She made the students stand in a line in increasing order of their ticket numbers. They were asked to leave a vacant position, in case a student has not turned up.
Ex: T1, T2, V, T4, T5, V, V, T8, T9, T10, V, T12, T13, V, V, T16, T17, T18, V, T20 where V - indicates vacant position.
Grouped them into 2 groups of 10 each including vacant positions.
Ex: Group – 1 (T1, T2, V, T4, T5, V, V, T8, T9, T10), Group – 2 (V, T12, T13, V, V, T16, T17, T18, V, T20)
Filled the vacant positions with the students from the next group as shown in the example below.
Ex: Group – 1 (T1, T2, T12, T4, T5, T13, T16, T8, T9, T10) Group -2 (T17, T18, T20)
Write a python function which accepts the unsorted ticket id list and returns the list of ticket ids of the ten students who were finally sent inside as part of Group-1.
 
Sample Input	                                              Expected Output
['T20','T5','T10','T1','T2','T8','T16','T17',
'T9','T4','T12','T13', 'T18']	                        ['T1', 'T2', 'T12', 'T4', 'T5', 'T13', 'T16', 'T8', 'T9', 'T10']
'''


def arrange_tickets(tickets_list):
    new_list=[]
    for i in range(1,21):
        if "T"+str(i) in tickets_list:
            new_list.append("T"+str(i))
        else:
            if i<=10:
                new_list.append('V')
    print(new_list)
    counter=10
    for index,ticket in enumerate(new_list):
        if ticket=='V' and index<=10:
            new_list[index]=new_list[counter]
            counter+=1
    return new_list[:10]

tickets_list = ['T5', 'T17', 'T10', 'T2', 'T9', 'T15', 'T17', 'T19', 'T16', 'T1', 'T12', 'T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result=arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)

'''
Integer Sorter v1.0
Program description: This program contains distinct functions for 
sorting a list of integers. The program uses a command line interface. 
The program recieves a list of integers,sorts the list using a method 
specified by the user and prints the sorted list to the screen.
Made by WGDEV, some rights reserved, see license.txt for more info
'''

'''
Description: Implements binary searching to find the index of an integer within a list
Parameters:
	List: The specified list
	Value: The value of the integer to be found within the specified list
'''
def binSearch(List,Value):
    if len(List) == 0:
        return 0
    if len(List) == 1:
        if List[0] == Value:
            return 0
        elif List[0] > Value:
            return 0
        else:
            return 1

    mini = 0
    maxi = len(List)-1
    while(maxi-mini>1):
        mid = (int)((mini+maxi)/2)
        if(List[mid]==Value):
            return mid
        elif(List[mid] > Value):
            maxi = mid
        else:
            mini = mid

    if (List[mini] == Value):
        return mini
    elif (List[maxi] ==Value):
        return maxi
    elif (List[mini] > Value):
        return mini      
    elif (List[maxi] > Value):
        return maxi
    else:
        return maxi+1
'''
Description: Implements a binary sorting algorithm to sort a list
Parameters:
	List: The specified list
'''
def binSort(List):
    for i in range (1, len(List)):
        t = List.pop(i)
        List.insert(binSearch(List[:i],t),t)

'''
Description: Implements a bubble sorting algorithm to sort a list
Parameters:
	List: The specified list
'''
def bubSort(List):
    c = True
    while c:
        c = False
        for i in range(0,len(List)-1):
            if List[i+1]<List[i]:
                t = List[i]
                List[i] = List[i+1]
                List[i+1] = t
                c = True    

'''
Description: Merges two sorted lists into one sorted list
Parameters:
	List1: The first list
        List2: The second list
'''
def merge(List1,List2):
    t = list()
    while (len(List1)>0 and len(List2)>0):
        if (List1[0]<List2[0]):
            t.append(List1.pop(0))
        else:
            t.append(List2.pop(0))    
    if (len(List1)>0):
        t.extend(List1)
    elif (len(List2)>0):
        t.extend(List2)
    return t

'''
Description: Implements a merge sorting algorithm to sort a list
Parameters:
	List: The specified list
'''
def mergeSort(List):
    for i in range(0,len(List)):
        List.insert(i,[List.pop(i)])
    while (len(List) > 1):
        for i in range(0,len(List)//2):
            List.insert(i,merge(List.pop(i), List.pop(i)))
    
'''
Description: Implements an insertion sorting algorithm to sort a list
Parameters:
	List: The specified list
'''
def insSort(List):
    for i in range (1, len(List)):
        t = List.pop(i)
        for j in range (0,i):
            if t <= List[j]:
                List.insert(j,t)
                t = None
                break
        if (t != None):
            List.insert(i,t)

'''
Description: Implements the quick sorting algorithm to sort a list of at least 3 integers
Parameters:
	List: The specified list
'''
def quickSort(List):
    quickSortStep(List,0,len(List)-1)

'''
Description: Implements a step in the quick sorting algorithm
Parameters:
	List: The specified list being sorted in the algorithm
        Low: The lowest index on the list that will be affected by this step
        High: The highest index on the list that will be affected by this step        
'''
def quickSortStep(List,Low,High):
    if (High - Low < 2):
        if High - Low == 1 and List[High] < List[Low]:
            List.insert(Low,List.pop(High))
        return
    pivot = 0
    if (List[Low]-List[(Low+High)//2])* (List[Low]-List[High]) <= 0:
        pivot = Low
    elif (List[High]-List[(Low+High)//2])* (List[High]-List[Low]) <= 0:
        pivot = High
    else:
        pivot = (Low+High)//2

    mini = Low
    maxi = High

    while(mini <= maxi):
        if List[pivot] > List[mini]:
            if pivot < mini:
                List.insert(Low,List.pop(mini))
                pivot += 1
            mini += 1
        elif List[pivot] < List[mini]:
            if pivot > mini:
                List.insert(High,List.pop(mini))
                pivot -= 1
                maxi -= 1
            else:
                mini += 1
        else:
            mini += 1
    quickSortStep(List,Low,pivot-1)
    quickSortStep(List,pivot + 1,High)

#The actual program starts here
print("Welcome to IntegerSorter v1.0 copyright WGDEV 2015")
while(True):
    print("Enter \"bubble #1 #2 #3...\" to run bubble sort.")
    print("Enter \"binary #1 #2 #3...\" to run binary sort.")    
    print("Enter \"merge #1 #2 #3...\" to run merge sort.")    
    print("Enter \"insert #1 #2 #3...\" to run insertion sort.")    
    print("Enter \"quick #1 #2 #3...\" to run quick sort.")     

    inp = input().lower().split(' ')
    q = list()
    for i in inp:
        if (i != inp[0]):
            q.append(int(i))
    if (inp[0] == "bubble"):
        bubSort(q)
    elif (inp[0] == "binary"):
        binSort(q)
    elif (inp[0] == "merge"):
        mergeSort(q)
        q=q[0]
    elif (inp[0] == "insert"):
        insSort(q)        
    elif (inp[0] == "quick"):
        quickSort(q)
    else:
        print("Command rejected!")
        continue
    print ("Your list sorted is " + str(q) + ".")

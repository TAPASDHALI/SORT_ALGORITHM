## WHEN YOU TAKE A LAST NUMBER PIVOT NUMBER
## QUICK SORT ALGORITHM PART -1 [FUNCTION, RECURSIVE FUNCTION]
#ASCENDING

import random
# TO GET THE CURRECT POSITION OF THE PIVOT ELEMENT
def pivot_place(lt1,first,last):
    rindex = random.randint(first,last)
    lt1[rindex],lt1[last] = lt1[last],lt1[rindex]
    pivot = lt1[last]
    left = first 
    right = last - 1
    while True:
        while left <= right and lt1[left] >= pivot:
            left = left + 1
        while left <= right and lt1[right] <= pivot:
            right = right - 1
        if right < left:
            break
        else:
            lt1[left],lt1[right] = lt1[right],lt1[left]
    lt1[last],lt1[left] = lt1[left],lt1[last]
    return left

def quicksort(lt1,first,last):
    if first < last:
        p = pivot_place(lt1,first,last)
        quicksort(lt1,first,p-1)
        quicksort(lt1,p+1,first)

#main
lt1 = [56,26,93,17,31,44]
n = len(lt1)
quicksort(lt1,0,n-1)
print(lt1)

## WHEN YOU TAKE A FIRST NUMBER PIVOT NUMBER
## QUICK SORT ALGORITHM PART -1 [FUNCTION, RECURSIVE FUNCTION]
#ASCENDING
# TO GET THE CURRECT POSITION OF THE PIVOT ELEMENT
def pivot_place(lt1,first,last):
    pivot = lt1[first]
    left = first + 1
    right = last
    while True:
        while left <= right and lt1[left] <= pivot:
            left = left + 1
        while left <= right and lt1[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            lt1[left],lt1[right] = lt1[right],lt1[left]
    lt1[first],lt1[right] = lt1[right],lt1[first]
    return right

def quicksort(lt1,first,last):
    if first < last:
        p = pivot_place(lt1,first,last)
        quicksort(lt1,first,p-1)
        quicksort(lt1,p+1,first)

#main
lt1 = [56,26,93,17,31,44,33]
n = len(lt1)
quicksort(lt1,0,n-1)
print(lt1)

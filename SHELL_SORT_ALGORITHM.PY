## Ascending
def ShellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for index in range(gap, len(list1)):
            current_element = alist[index]
            pos = index
            while pos >= gap and current_element < alist[pos-gap]:
                alist[pos] = alist[pos-gap]
                pos = pos - gap
            alist[pos] = current_element
        gap = gap // 2

print("Sorted Ascending")
num = int(input("Enter List Of Length: "))
list1 = [int(input("Enter Elements Number: ")) for i in range(num)]
ShellSort(list1)
print(list1)


## Descending
def ShellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for index in range(gap, len(list1)):
            current_element = alist[index]
            pos = index
            while pos >= gap and current_element > alist[pos-gap]:
                alist[pos] = alist[pos-gap]
                pos = pos - gap
            alist[pos] = current_element
        gap = gap // 2

print("Sorted Descending")
num = int(input("Enter List Of Length: "))
list1 = [int(input("Enter Elements Number: ")) for i in range(num)]
ShellSort(list1)
print(list1)

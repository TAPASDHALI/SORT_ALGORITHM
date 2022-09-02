## ASCENDING
def InsertionSort(my_list):
    for index in range(1, len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element < my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos = pos - 1
        my_list[pos] = current_element

print("Ascending")
num = int(input("How many Elements you want in this List: "))
list1 = [int(input("Enter Elements Number: ")) for i in range(num)]
# list1 = [2,4,5,1,3]
InsertionSort(list1)
print(list1)


print()
## DESCENDING
def InsertionSort(my_list):
    for index in range(1, len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element > my_list[pos-1] and pos > 0:
            my_list[pos] = my_list[pos-1]
            pos = pos - 1
        my_list[pos] = current_element

print("Descending")
num = int(input("How many Elements you want in this List: "))
list1 = [int(input("Enter Elements Number: ")) for i in range(num)]
# list1 = [2,4,5,1,3]
InsertionSort(list1)
print(list1)

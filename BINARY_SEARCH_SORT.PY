#BINARY SEARCH SORTED ALGORITHM
def BinarySearch(list1, key):
    low = 0
    high = len(list1) - 1
    Found = False
    while low <= high and not Found:
        mid = (low + high) // 2
        if key == list1[mid]:
            Found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if Found == True:
        print("Key is Found")
    else:
        print("Key is Not Found")

num = int(input("How Many Elements You Want In This List: "))
list1 = [int(input("Enter Elements Nmuber: ")) for i in range(num)]
list1.sort()
print(list1)
key = int(input("Enter The Key: "))
BinarySearch(list1, key)
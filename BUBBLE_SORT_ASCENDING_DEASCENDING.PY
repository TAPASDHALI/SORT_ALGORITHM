# BUBBLE SORT ASCENDING AND DEASCENDING PROGRAM?
#DEASCENDING
# list1 = [10,20,24,33,4,45,0]
# print("Unsorted List",list1)
# for i in range(len(list1)-1):
#     for j in range(len(list1)-1):
#         if list1[j] < list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print(f'Sorted List: {list1}')


#ASCENDING
# list1 = [10,20,24,33,4,45,0]
# print("Unsorted List",list1)
# for i in range(len(list1)-1):
#     for j in range(len(list1)-1):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print(f'Sorted List: {list1}')




# # IF YOU WANT ALL THE SAWP STAPE WHEN NEED DOING?
# list1 = [10,20,24,33,4,45,0]
# print("Unsorted List",list1)
# for i in range(len(list1)-1):
#     # for j in range(len(list1)-1):
#     for j in range(len(list1)-1-i):
#         # if list1[j] < list1[j+1]:
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
#             print(list1)
#         else:
#             print(list1)
#     print()
# print(f'Sorted List: {list1}')



# IF YOU WANT ALL THE SAWP STAPE WHEN NEED DOING change method?
# list1 = [10,20,24,33,4,45,0]
# print("Unsorted List",list1)
# for i in range(len(list1)-1,0,-1):
#     for j in range(i):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
#             print(list1)
#         else:
#             print(list1)
#     print()
# print(f'Sorted List: {list1}')


list1 = []
num =int(input("How many number you want to enter: "))
print("Enter Values:-")
for i in range(num):
    list1.append(int(input("Enter Any Digit Number: ")))
print("Unorderd List: ",list1)
for j in range(len(list1)-1,0,-1):
    for k in range(j):
        # if list1[k] > list1[k+1]:
        if list1[k] < list1[k+1]:
            list1[k],list1[k+1] = list1[k+1],list1[k]
            print(list1)
        else:
            print(list1)
    print()
print(f'Sorted List: {list1}')



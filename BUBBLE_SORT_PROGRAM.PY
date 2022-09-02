# BUBBLE SORT PROGRAM?
# list1 = [10,20,24,33,4,45,0]
# print(f'Unorded List: {list1}')
# for i in range(len(list1)-1):
#     for j in range(len(list1)-1):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print(f'sorted list: {list1}')


list1 = [10,20,24,33,4,45,0]
print(f'Unorded List: {list1}')
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j] < list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
print(f'sorted list: {list1}')

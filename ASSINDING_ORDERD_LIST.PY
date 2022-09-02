# WAP TO  FIND OUT ASSINDING ORDER IN A ELEMENTS OF LIST ?
# list1  = [56,0,2,2,0,6]
# print(list1)
# for i in range(len(list1)):
#     min_val = min(list1[i:])
#     min_ind = list1.index(min_val, i)
#     list1[i], list1[min_ind] = list1[min_ind],list1[i]
# print(list1)



#WAP TO  FIND OUT DISASSINDING ORDER IN A ELEMENTS OF LIST ?
# list1  = [56,0,2,2,0,6]
# print(list1)
# for i in range(len(list1)):
#     max_val = max(list1[i:])
#     max_ind = list1.index(max_val, i)
#     list1[i], list1[max_ind] = list1[max_ind],list1[i]
# print(list1)



list1  = [56,0,2,2,0,6]
print("Unorderd List:-",list1)
for i in range(len(list1)-1):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val, i)
    if list[i] != list1[min_ind]:
        list1[i], list1[min_ind] = list1[min_ind],list1[i]
    print(list1)

# # WAP TO MOVE FIRST  INDEX TO LIST AND LAST INDEXT TO FIRST USING SWAP METHOD?
# list1 = [56,3,2,78,6,0]
# print(list1)
# min_val = min(list1)
# # print(min_val)
# min_ind = list1.index(min_val)
# # print(min_ind)
# list1[0],list1[min_ind] = list1[min_ind],list1[0]
# print(list1)




# # WAP TO FIND OUT MINIMUM T0 MAXIMUM VALUE IN A ELEMENTS OF LIST USING SWAP METHOD?
# list1 = [56,3,2,78,6,0]
# print(list1)
# for i in range(len(list1)):
#     min_val = min(list1[i:])
#     min_ind = list1.index(min_val)
#     list1[i],list1[min_ind] = list1[min_ind],list1[i]
# print(list1)


# WAP TO FIND OUT MAXIMUM T0 MINIMUM VALUE IN A ELEMENTS OF LIST USING SWAP METHOD?
list1 = [56,3,2,78,6,0]
print(list1)
for i in range(len(list1)):
    max_val = max(list1[i:])
    max_ind = list1.index(max_val)
    list1[i],list1[max_ind] = list1[max_ind],list1[i]
print(list1)


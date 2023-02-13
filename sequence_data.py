import random
list1= list(range(1,11))
list2=[random.randrange(5,21) for i in range(10)]
combined_list=list1+list2
combined_tuple=tuple(combined_list)
print(f"list1:{list1}\nlist2:{list2}\ncombined_list:{combined_list}\ncombined_tuple:{combined_tuple}")
print(22.5-11/4+1*2%14)
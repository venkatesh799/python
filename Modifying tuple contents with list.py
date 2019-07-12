# Modifying tuple contents with list
list1 = [('venky', 1), ('victory', 2), ('boom', 3)] 
list2 = [4, 5, 6]
res=[(i[0],j) for i,j in zip(list1,list2)]
print(res)          #[('venky', 4), ('victory', 5), ('boom', 6)]

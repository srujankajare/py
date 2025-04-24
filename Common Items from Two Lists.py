5. Common Items from Two Lists 

list1 = input("Enter first list: ").split() 
list2 = input("Enter second list: ").split() 
common = list(set(list1) & set(list2)) 
print("Common items are:", common) 

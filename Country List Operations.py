Country List Operations

countries = ["India", "USA", "Brazil", "Australia", "Canada"] 
 
print("Original Country List:") 
print(countries) 

countries.append("Germany") 
print("\nAfter Adding 'Germany':") 
print(countries) 

countries.insert(2, "Japan") 
print("\nAfter Inserting 'Japan' at index 2:") 
print(countries) 

countries.remove("Brazil") 
print("\nAfter Removing 'Brazil':") 
print(countries) 

removed_country = countries.pop() 
print(f"\nAfter Popping Last Country ('{removed_country}'):") 
print(countries) 
 
countries.sort() 
print("\nSorted Country List:") 
print(countries) 
 
countries.reverse() 
print("\nReversed Country List:") 
print(countries) 
 
index = countries.index("India") 
print(f"\nIndex of 'India': {index}") 
 
count = countries.count("India") 
print(f"Occurrences of 'India': {count}")
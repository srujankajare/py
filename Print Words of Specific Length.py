12. Print Words of Specific Length from File 


filename = input("Enter file name: ") 
length = int(input("Enter word length to find: ")) 
with open(filename, 'r') as file: 
	words = file.read().split() 
	for word in words: 
		if len(word) == length: 
			print(word)
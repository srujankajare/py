13. Append and Display File 


text = input("Enter text to add: ") 
file = open("myfile.txt", "a") 
file.write(text + "\n") 
file.close() 
file = open("myfile.txt", "r") 
print("File Content:") 
print(file.read()) 
file.close()
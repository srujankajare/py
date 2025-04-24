7. Student Records Dictionary 
students = { 
	"Amit": {"grade": "A", "attendance": 90}, 
	"Sara": {"grade": "B", "attendance": 85} 
} 
students["Ravi"] = {"grade": "A+", "attendance": 95} 
students["Amit"]["attendance"] = 92 

for name in students: 
	print(name, "->", students[name]) 

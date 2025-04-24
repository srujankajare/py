Date Class with Exception for Invalid Day Type 


class Date: 
	def  init (self, day, month, year): 
		if not isinstance(day, int): 
			raise ValueError("Day must be an integer") 
		self.day = day 
		self.month = month 
		self.year = year 
	def display(self): 
		print(f"Date: {self.day:02d}/{self.month:02d}/{self.year}") 
try: 
	d = Date(12, 4, 2025) 
	d.display() 
except ValueError as ve: 
	print("Error:", ve) 
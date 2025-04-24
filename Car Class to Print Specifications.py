 Car Class to Print Specifications 


class Car: 
	def  init (self, make, model, year, color): 
		self.make = make 
		self.model = model 
		self.year = year 
		self.color = color 
	def display_specs(self): 
		print(f"{self.year} {self.make} {self.model}, Color: {self.color}") 
c = Car("Toyota", "Camry", 2022, "Red") 
c.display_specs()
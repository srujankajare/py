MathOperation Class 


class MathOperation: 
	def add(self, a, b): 
		return a + b 
	def multiply(self, a, b): 
		return a * b 
	def factorial(self, n): 
		return 1 if n == 0 else n * self.factorial(n - 1) 
math_op = MathOperation() 
print("Addition:", math_op.add(5, 3)) 
print("Multiplication:", math_op.multiply(5, 3)) 
print("Factorial:", math_op.factorial(5))
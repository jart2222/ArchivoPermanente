import pickle
class Persona:
	def __init__(self,nombre,genero,edad):
		self.nombre=nombre;
		self.genero=genero;
		self.edad=edad;
		print("Se ha creado una nueva persona con el nombre ",self.nombre);
	def  __str__(self):
		return "\nNombre de la persona: {}\nGenero de la persona: {}\nEdad de la persona: {}\n".format(self.nombre,self.genero,self.edad);










		
	


	


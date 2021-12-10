from infoPermanente import Persona
class ListaPersonas:
	personas=[]
	def __init__(self):
		listaDePersonas=open("ficheroExterno","ab+");
		listaDePersonas.seek(0);
		try:
			self.personas=pickle.load(listaDePersonas);
			print("se cargaron {} personas del fichero externo".format(len(self.personas)));
		except:
			print("el fichero esta vacio");
		finally:
			listaDePersonas.close();
			del(listaDePersonas);

	def agregarPersonas(self,persona):
		self.personas.append(persona);

	def mostrarPersonas(self):
		for i in self.personas:
			print(i);

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno","wb");
		pickle.dump(self.personas,listaDePersonas);
		listaDePersonas.close();
		del(listaDePersonas);

	def mostarInfoFicheroExterno(self):
		print("la informacion del fichero es la siguiente ");

		for p in self.personas:
			print(p)



milista=ListaPersonas()
mipersona1=Persona("Sandra Lopez","Femenino",40)
milista.agregarPersonas(mipersona1)
mipersona2=Persona("Jose Valencia","Masculino",80)
milista.agregarPersonas(mipersona2)
milista.mostarInfoFicheroExterno()
class Carro
	def descrever
	  "Eu sou um carro normal."
	end
  end
  
  class CarroEsportivo < Carro
	def descrever
	  "Eu sou um carro esportivo, sou rapido."
	end
  end
  class CarroSedan < Carro
	def descrever
	  "Sou um carro sedan, grande e espaçoso."
	end
  end
  
  carro_generico = Carro.new
  carro_esportivo = CarroEsportivo.new
  carro_sedan = CarroSedan.new
  
  puts carro_generico.descrever
  puts carro_esportivo.descrever
  puts carro_sedan.descrever
  
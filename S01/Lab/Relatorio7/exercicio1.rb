class Carro
	def descrever
	  "Eu sou um carro genérico."
	end
  end
  
  class CarroEsportivo < Carro
	def descrever
	  "Eu sou um carro esportivo, feito para velocidade."
	end
  end
  class CarroSedan < Carro
	def descrever
	  "Eu sou um carro sedan, focado em conforto e espaço."
	end
  end
  
  carro_generico = Carro.new
  carro_esportivo = CarroEsportivo.new
  carro_sedan = CarroSedan.new
  
  puts carro_generico.descrever
  puts carro_esportivo.descrever
  puts carro_sedan.descrever

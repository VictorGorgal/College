class Carro
	def descrever
	  "Carro normal"
	end
  end
  
  class CarroEsportivo < Carro
	def descrever
	  "Carro esportivo"
	end
  end
  class CarroSedan < Carro
	def descrever
	  "Carro sedan"
	end
  end
  
  carro = Carro.new
  carroEsportivo = CarroEsportivo.new
  carroSedan = CarroSedan.new
  
  puts carro.descrever
  puts carroEsportivo.descrever
  puts carroSedan.descrever
  
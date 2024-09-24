from Database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import motoristaCLI

db = Database(database="ExercicioAvaliativo1", collection="Motoristas")

motorista = MotoristaDAO(database=db)
motoristaCLI = motoristaCLI(motorista)
motoristaCLI.run()

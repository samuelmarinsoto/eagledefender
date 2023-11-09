import DataBaseLocal as DBL


class Puntaje:

	def __init__(self, Username, pathimage, puntaje):
		self.Username = Username
		self.pathimage = pathimage
		self.puntaje = puntaje

	def update_Username(self, Username):
		self.Username = Username

	def update_pathimage(self, new_pathimage):
		self.pathimage = new_pathimage

	def update_puntaje(self, new_puntaje):
		self.puntaje = new_puntaje

	@staticmethod
	def update_hallfame():
		Top10 = DBL.get_top_10_scores()
		# Creamos una lista de instancias de Puntaje previamente para evitar referencias antes de asignación
		scores = [Puntaje("", "", 0) for _ in range(10)]  # Prepara 10 espacios para puntajes

		# Actualiza las instancias de Puntaje con los datos obtenidos
		for i, score_data in enumerate(Top10):  # Usar enumerate para obtener índice y valor
			if i < len(scores):  # Asegura que no se salga del rango de la lista 'scores'
				scores[i].update_Username(score_data[0])
				scores[i].update_pathimage(score_data[1])
				scores[i].update_puntaje(score_data[2])
			else:
				break  # Si no hay suficientes datos, rompe el ciclo

		# Devuelve la lista de puntajes actualizados
		return scores


# Crear una lista de puntajes vacíos para los top 10 espacios
scores_list = [Puntaje("", "", 0) for _ in range(6)]  # Asumiendo que solo necesitamos 6 objetos Puntaje

# Llama a la función para actualizar la lista de puntajes
updated_scores = Puntaje.update_hallfame()

# Asigna los puntajes actualizados a las variables si hay datos suficientes
if updated_scores:
	Score1, Score2, Score3, Score4, Score5, Score6 = updated_scores[
	                                                 :6]  # Asume que siempre hay al menos 6 puntajes, ajusta según sea necesario

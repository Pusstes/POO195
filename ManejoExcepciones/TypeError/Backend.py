class backend:
    def CadenaCaracter(self, dato):
        print(dato)
        nombres = ["Leo", "Aldo", "Luis", "Parra", "Fernando", "Adrian", "Pedro", "Marcos", "Maximiliano", "Ronaldo"]
        try:
            index = int(dato)
            if index < 0 or index >= len(nombres):
                return ValueError("El número debe ser mayor o igual a 0 y menor a " + str(len(nombres)) + ".")
            else:
                return nombres[index]
        except ValueError:
            return nombres[dato], ValueError
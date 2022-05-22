

class TypeOfGarbage:

    plastic = {"name": "Plástico", "color": "red"}
    glass = {"name": "Vidro", "color": "green"}
    organic = {"name": "Orgânico", "color": "brown"}
    paper = {"name": "Papel", "color": "blue"}
    metal = {"name": "Metal", "color": "yellow"}

    def get_type(self, type_name):
        if self.__getattribute__(type_name):
            return self.__getattribute__(type_name)
        return {}

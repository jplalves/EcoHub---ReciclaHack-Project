

class TypeOfGarbage:

    plastic = {"name": "Plastic", "color": "red"}
    glass = {"name": "Glass", "color": "green"}
    organic = {"name": "Organic", "color": "brown"}
    paper = {"name": "Paper", "color": "blue"}
    metal = {"name": "Metal", "color": "yellow"}

    def get_type(self, type_name):
        if self.__getattribute__(type_name):
            return self.__getattribute__(type_name)
        return {}

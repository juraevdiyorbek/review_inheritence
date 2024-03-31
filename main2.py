class Transport:
    def __init__(self,brand,model,type) -> None:
        self.brand = brand
        self.model = model
        self.type = type

class ElectroCars(Transport):
    def __init__(self, brand, model, type,batter_life,chargin_time) -> None:
        super().__init__(brand, model, type)
        self.batter_life = batter_life
        self.chargin_time = chargin_time

    def more_info(self):
        return f"""Brand : {self.brand}
Model: {self.model}
Type : {self.type}
Battery_life : {self.batter_life}
Chargin_time : {self.chargin_time}"""
    
class SportCras(Transport):
    def __init__(self, brand, model, type,motor,color) -> None:
        super().__init__(brand, model, type)
        self.motor = motor
        self.color = color

    def more_info(self):
        return f"""Brand : {self.brand}
Model: {self.model}
Type : {self.type}
Motor : {self.motor}
Color : {self.color}"""
    
class Truck(Transport):
    def __init__(self, brand, model, type,motor,height,long,wieght) -> None:
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.wieght = wieght
    def more_info(self):
        return f"""Brand : {self.brand}
Model: {self.model}
Type : {self.type}
Motor : {self.motor}
Height : {self.heigth}
Long : {self.long}
Wieght : {self.wieght}"""
    
sport = SportCras("Ferrari","Ferrari GT100","Sport","V6","RED")
print(sport.more_info())
    
class Dog ():
    # name = None
    # poroda = None
    # color = None
    
    def __init__(self,name,poroda) -> None:
        self.name = name
        self.poroda = poroda
    
    def fas(self):
        print("Гав-Гав")
    
dog_1 = Dog( "Бобик", "корги" )
# dog_1.name = "Шарик"
# dog_1.poroda = "дворняга"
print(f"{dog_1.name = }, {dog_1.poroda}")
dog_1.fas()

class Vehicle:

    def __init__(self, type):
        self.type = type

    def drive(self):
             print("vroooom")

    def turn(self, direction):
             print(f'The car turns {direction}')

    def stop(self):
             print(f"The {self.color} car has stopped")


class Car(Vehicle):
    def __init__(self, color):
        self.color = color
        super().__init__("car")

    def drive(self):
         print(f"the {self.color} car goes woosh")


tesla = Car("blue")
tesla.drive()
tesla.stop()
tesla.turn("right")

honda = Car("yellow")
honda.drive()
honda.stop()
honda.turn("left")





        
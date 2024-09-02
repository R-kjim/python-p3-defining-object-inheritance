from vehicle import Vehicle

class Car(Vehicle):
    pass
    # super()
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

subaru=Car(14,65)
print(subaru.go())